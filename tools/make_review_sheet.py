#!/usr/bin/env python3
"""make_review_sheet.py — AI 답변(.md/.txt)에서 사람이 확인해야 할 주장을 뽑아 검토표를 만든다.

사용법:
    python tools/make_review_sheet.py raw/예시_AI답변_01_정책브리프.md
    python tools/make_review_sheet.py raw/파일.md --out out/검토표_이름.md

이 도구는 판정하지 않는다. 무엇을 확인할지만 뽑는다.
판정과 근거 칸은 사람이 원문을 열어 보고 채운다 — 확인하지 못한 것은 〔확인 못 함〕으로 남긴다.
표준 라이브러리만 쓴다(설치 없음).

뽑는 단위:
    - 본문 줄은 문장 단위. 머리글(#) · 인용(>) 줄은 건너뛴다.
    - 표(|) 줄은 행 단위 — 첫 행을 머리글로 삼아 "표 행 '라벨' — 머리글 값 · …" 한 문장으로 만들고,
      칸에 숫자가 있으면 수치 유형으로 뽑는다. 표 안의 합계 · 비율이 검토표에서 빠지지 않게 하기 위해서다.
"""
import argparse
import datetime
import pathlib
import re
import sys

# ── 주장 유형 규칙 ──────────────────────────────────────────────
NUM = re.compile(r"\d[\d,.]*\s*(?:%p|%|％|퍼센트|억|만|천|명|건|개|배|원|년|월|일|시간|분|초|회|개소|곳|쪽|p)")
KNUM = re.compile(r"(?:한|두|세|네|다섯|열|백|천)\s?(?:배|곱절|건|명|개)")
URL = re.compile(r"https?://\S+")
CITE = re.compile(r"\([^()]*(?:19|20)\d{2}[^()]*\)|「[^」]+」|『[^』]+』|제\s?\d+\s?조|에 따르면|보고서|논문|실태조사|조사 결과|인용")
DATE = re.compile(r"(?:19|20)\d{2}\s?년|(?:19|20)\d{2}\.\s?\d{1,2}|기준|현재|최근|지난해|지난달|전년|전월|연말까지|까지")
STRONG = re.compile(r"확실|분명|반드시|모든 |항상|입증|명백|틀림없|증명|사실상")
TABLE_NUM = re.compile(r"\d")  # 표의 칸은 단위가 머리글에 있으므로 숫자만 있어도 수치로 본다

TYPES = [
    ("수치", lambda s: bool(NUM.search(s) or KNUM.search(s)),
     "원자료 표 열기 → 같은 값 · 같은 단위 · 같은 기간인지 칸별로 대조 · 합계와 비율 합을 다시 계산"),
    ("출처", lambda s: bool(CITE.search(s)),
     "출처를 직접 열기 → 그 문서의 그 쪽에 그 문장이 실제로 있는지(귀속) · 표기가 맞는지"),
    ("주소", lambda s: bool(URL.search(s)),
     "주소를 열기 → 열리는지 · 제목이 본문 설명과 같은지 · 날짜가 맞는지"),
    ("시점", lambda s: bool(DATE.search(s)),
     "자료의 기준 시점과 문장의 시점이 같은지 · 어느 해 · 어느 달 자료인지"),
    ("단정", lambda s: bool(STRONG.search(s)),
     "근거 없이 단정한 표현인지 → 근거를 요구하거나 〔확인 필요〕로 완화"),
]

SKIP_MARK = "실습용으로 지어낸"
SPLIT = re.compile(r"(?<=[.!?。])\s+")
TABLE_SEP = re.compile(r"^\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?\s*$")  # |---|:---:| 구분선
ROW_MARK = "표 행 '"


def split_cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_row_sentence(header, cells):
    """표의 데이터 행 하나를 "표 행 '라벨' — 머리글 값 · …" 한 문장으로 만든다. 단위는 머리글에 있으므로 머리글 이름을 함께 적는다."""
    label = cells[0] if cells else ""
    pairs = []
    for i, cell in enumerate(cells[1:], start=1):
        name = header[i] if header and i < len(header) and header[i] else f"{i + 1}열"
        pairs.append(f"{name} {cell if cell else '(빈칸)'}")
    return f"{ROW_MARK}{label}' — " + " · ".join(pairs)


def iter_sentences(text: str):
    """(줄 번호, 문장, 표 행 여부)를 돌려준다. 머리글(#) · 인용(>) 줄은 건너뛰고, 표(|) 줄은 행 단위로 돌려준다."""
    header = None  # 지금 읽고 있는 표의 머리글 칸 — 표가 끝나면 None
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith(("#", ">")):
            header = None
            continue
        if SKIP_MARK in line:
            continue
        if line.startswith("|"):
            if TABLE_SEP.match(line):
                continue
            cells = split_cells(line)
            if header is None:
                header = cells  # 표의 첫 행은 칸 이름이지 주장이 아니다
                continue
            yield lineno, table_row_sentence(header, cells), True
            continue
        header = None
        line = re.sub(r"^(?:[-*•]|\d+[.)])\s+", "", line)  # 목록 기호 · 번호 제거
        for sent in SPLIT.split(line):
            sent = sent.strip()
            if sent:
                yield lineno, sent, False


def extract_claims(text: str):
    """[(줄, 문장, [유형...]), ...] — 유형이 하나도 없으면 주장으로 보지 않는다. 표 행은 칸에 숫자가 있으면 수치다."""
    claims = []
    for lineno, sent, is_row in iter_sentences(text):
        types = [name for name, test, _ in TYPES if test(sent)]
        if is_row and "수치" not in types and TABLE_NUM.search(sent):
            types.insert(0, "수치")
        if types:
            claims.append((lineno, sent, types))
    return claims


def how_to_check(types):
    guide = {name: how for name, _, how in TYPES}
    return " · ".join(guide[t] for t in types)


def build_sheet(src: pathlib.Path, claims, now=None) -> str:
    now = now or datetime.datetime.now()
    counts = {name: sum(1 for _, _, ts in claims if name in ts) for name, _, _ in TYPES}
    rows = sum(1 for _, s, _ in claims if s.startswith(ROW_MARK))
    lines = [
        f"# 검토표 — {src.name}",
        "",
        f"- 원문: {src.as_posix()}",
        f"- 생성: {now:%Y-%m-%d %H:%M} · tools/make_review_sheet.py",
        f"- 뽑은 주장: {len(claims)}건 (" + " · ".join(f"{k} {v}" for k, v in counts.items()) + f") · 표 행 {rows}건 포함",
        "- 규칙: 판정과 근거는 사람이 원문을 열어 보고 적는다 · 도구는 합격을 말하지 않는다 · 확인하지 못한 것은 〔확인 못 함〕으로 남긴다",
        "- 판정 칸에 쓸 수 있는 값: (비움) · 통과 · 미통과 · 〔확인 못 함〕 — 통과 · 미통과에는 근거가 있어야 한다",
        "",
        "| 번호 | 원문 줄 | 확인할 주장 | 유형 | 확인 방법 | 판정 | 근거(원자료 위치 · 계산) |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, (lineno, sent, types) in enumerate(claims, start=1):
        safe = sent.replace("|", "｜")
        where = f"L{lineno} (표)" if sent.startswith(ROW_MARK) else f"L{lineno}"
        lines.append(f"| {i} | {where} | {safe} | {' · '.join(types)} | {how_to_check(types)} |  |  |")
    lines += [
        "",
        "## 검토 요약 (사람이 적음)",
        "",
        "- 미통과: ",
        "- 확인 못 함: ",
        "- 판단 — 이 답변을 그대로 쓸 수 있나: ",
        "",
    ]
    return "\n".join(lines)


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("source", help="AI 답변 파일(.md/.txt)")
    p.add_argument("--out", help="검토표를 저장할 경로(기본: out/검토표_<원문 이름>.md)")
    a = p.parse_args(argv)

    src = pathlib.Path(a.source)
    if not src.is_file():
        print(f"멈춤 — 원문 파일이 없음: {src}")
        return 2
    text = src.read_text(encoding="utf-8")
    claims = extract_claims(text)
    rows = sum(1 for _, s, _ in claims if s.startswith(ROW_MARK))
    if a.out:
        out = pathlib.Path(a.out)
    else:
        out = pathlib.Path("out") / f"검토표_{src.stem.replace('예시_AI답변_', '예시')}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_sheet(src, claims), encoding="utf-8")
    print(f"검토표 저장: {out.as_posix()} — 확인할 주장 {len(claims)}건 · 표 행 {rows}건 포함 (판정 칸은 비어 있음 · 판정은 사람이)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
