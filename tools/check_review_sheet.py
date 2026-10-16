#!/usr/bin/env python3
"""check_review_sheet.py — 검토표가 규칙대로 만들어졌는지 기계적으로 검사한다. 안 맞으면 멈춘다(종료 코드 1).

사용법:
    python tools/check_review_sheet.py raw/예시_AI답변_01_정책브리프.md out/검토표_예시01_정책브리프.md
    python tools/check_review_sheet.py 내답변.md 검토표_2026-10-16-10-00.md   # 검토 페이지에서 내보낸 검토표도 같은 명령

검사 항목:
    1. 검토표 머리(첫 8줄)에 원문 파일 이름이 있다
    2. 표의 열이 규정된 7열이다 — 도구와 검토 페이지가 같은 머리글을 쓴다
    3. 원문에서 다시 뽑은 주장 수 == 표의 행 수 (빠진 주장이 없다)
       — 검토 페이지가 내보낸 검토표는 모델 · 데모의 지적이라 재추출과 비교할 수 없으므로 건너뛰고 그렇게 출력한다
    4. 판정 칸의 값은 (비움) · 통과 · 미통과 · 〔확인 못 함〕 중 하나다
    5. 통과 · 미통과로 적힌 행은 근거 칸이 비어 있지 않다 — 확인하지 못한 것을 확인했다고 적지 않는다
    6. 〔원문에 없음〕 표시가 붙은 행(모델이 든 인용을 원문에서 찾지 못함)은 '통과'가 될 수 없다

이 스크립트는 "답이 맞는지"를 판단하지 않는다. 사람이 판정할 수 있는 모양인지만 본다.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from make_review_sheet import extract_claims  # noqa: E402

HEADER = "| 번호 | 원문 줄 | 확인할 주장 | 유형 | 확인 방법 | 판정 | 근거(원자료 위치 · 계산) |"
ALLOWED = {"", "통과", "미통과", "〔확인 못 함〕"}
PAGE_MARK = "failure-peer-review-agent.html"  # 검토 페이지가 내보낸 검토표의 표식(머리 블록에 있음)
MISSING = "〔원문에 없음〕"
HEAD_LINES = 8


def rows_of(sheet: str):
    rows = []
    for line in sheet.splitlines():
        if line.startswith("|") and not line.startswith("|---") and line.strip() != HEADER:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) != 2:
        print(__doc__)
        return 2
    src, sheet_path = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    for f in (src, sheet_path):
        if not f.is_file():
            print(f"멈춤 — 파일이 없음: {f}")
            return 1
    text = src.read_text(encoding="utf-8")
    sheet = sheet_path.read_text(encoding="utf-8")
    head = "\n".join(sheet.splitlines()[:HEAD_LINES])
    from_page = PAGE_MARK in head
    problems, notes = [], []

    # 1 원문 이름 — 머리 블록 안에
    if src.name not in head:
        problems.append(f"1 원문 이름 — 검토표 머리(첫 {HEAD_LINES}줄)에 '{src.name}'이 없음")
    # 2 열
    if HEADER not in sheet:
        problems.append("2 열 — 규정 7열 머리글이 없음(열 이름이나 순서가 다름)")
    rows = rows_of(sheet)
    # 3 행 수 — 도구 검토표만 재추출과 비교한다
    if from_page:
        notes.append("3 행 수 — 검토 페이지에서 내보낸 검토표라 원문 재추출과 비교하지 않음(모델 · 데모의 지적은 도구의 추출과 다름 · 모양만 검사)")
    else:
        expected = len(extract_claims(text))
        if len(rows) != expected:
            problems.append(f"3 행 수 — 원문에서 뽑은 주장 {expected}건 ≠ 표의 행 {len(rows)}건")
    # 4 · 5 · 6 판정 값 · 근거 · 원문 대조
    for cells in rows:
        if len(cells) < 7:
            problems.append(f"2 열 — {cells[0] if cells else '?'}번 행의 칸 수가 7이 아님({len(cells)})")
            continue
        no, where, claim, verdict, basis = cells[0], cells[1], cells[2], cells[5], cells[6]
        if verdict not in ALLOWED:
            problems.append(f"4 판정 값 — {no}번 행 '{verdict}'는 허용되지 않음(비움 · 통과 · 미통과 · 〔확인 못 함〕만)")
        if verdict in {"통과", "미통과"} and not basis:
            problems.append(f"5 근거 — {no}번 행이 '{verdict}'인데 근거 칸이 비어 있음(확인 못 한 것을 확인했다고 적지 않는다)")
        if (MISSING in where or MISSING in claim) and verdict == "통과":
            problems.append(f"6 원문 대조 — {no}번 행은 모델이 든 인용이 원문에 없는데 '통과'로 적힘(〔확인 못 함〕 또는 미통과로, 근거와 함께)")

    judged = sum(1 for c in rows if len(c) >= 7 and c[5] in {"통과", "미통과"})
    unchecked = sum(1 for c in rows if len(c) >= 7 and c[5] == "〔확인 못 함〕")
    blank = sum(1 for c in rows if len(c) >= 7 and c[5] == "")
    missing = sum(1 for c in rows if len(c) >= 7 and (MISSING in c[1] or MISSING in c[2]))
    print(f"검토표: {sheet_path.as_posix()} — 행 {len(rows)}건 · 판정됨 {judged} · 확인 못 함 {unchecked} · 비움 {blank}"
          + (f" · 원문에 없음 {missing}" if missing else "") + (" · 페이지 검토표" if from_page else ""))
    for n in notes:
        print(f"  · {n}")
    if problems:
        print("멈춤 — 검사 실패:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("통과 — 검사 모두 맞음(이것은 모양 검사이며, 내용이 맞는지는 사람이 판정한다)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
