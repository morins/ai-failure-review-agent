#!/usr/bin/env python3
"""check_review_sheet.py — 검토표가 규칙대로 만들어졌는지 기계적으로 검사한다. 안 맞으면 멈춘다(종료 코드 1).

사용법:
    python tools/check_review_sheet.py raw/예시_AI답변_01_정책브리프.md out/검토표_예시01_정책브리프.md

검사 항목:
    1. 검토표 머리에 원문 파일 이름이 있다
    2. 표의 열이 규정된 7열이다
    3. 원문에서 다시 뽑은 주장 수 == 표의 행 수 (빠진 주장이 없다)
    4. 판정 칸의 값은 (비움) · 통과 · 미통과 · 〔확인 못 함〕 중 하나다
    5. 통과 · 미통과로 적힌 행은 근거 칸이 비어 있지 않다 — 확인하지 못한 것을 확인했다고 적지 않는다

이 스크립트는 "답이 맞는지"를 판단하지 않는다. 사람이 판정할 수 있는 모양인지만 본다.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from make_review_sheet import extract_claims  # noqa: E402

HEADER = "| 번호 | 원문 줄 | 확인할 주장 | 유형 | 확인 방법 | 판정 | 근거(원자료 위치 · 계산) |"
ALLOWED = {"", "통과", "미통과", "〔확인 못 함〕"}


def rows_of(sheet: str):
    rows = []
    for line in sheet.splitlines():
        if line.startswith("|") and not line.startswith("|---") and line != HEADER:
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
    problems = []

    # 1 원문 이름
    if src.name not in sheet.splitlines()[0]:
        problems.append(f"1 원문 이름 — 첫 줄에 '{src.name}'이 없음")
    # 2 열
    if HEADER not in sheet:
        problems.append("2 열 — 규정 7열 머리글이 없음(열 이름이나 순서가 다름)")
    rows = rows_of(sheet)
    # 3 행 수
    expected = len(extract_claims(text))
    if len(rows) != expected:
        problems.append(f"3 행 수 — 원문에서 뽑은 주장 {expected}건 ≠ 표의 행 {len(rows)}건")
    # 4 · 5 판정 값과 근거
    for cells in rows:
        if len(cells) < 7:
            problems.append(f"2 열 — {cells[0] if cells else '?'}번 행의 칸 수가 7이 아님({len(cells)})")
            continue
        no, verdict, basis = cells[0], cells[5], cells[6]
        if verdict not in ALLOWED:
            problems.append(f"4 판정 값 — {no}번 행 '{verdict}'는 허용되지 않음(비움 · 통과 · 미통과 · 〔확인 못 함〕만)")
        if verdict in {"통과", "미통과"} and not basis:
            problems.append(f"5 근거 — {no}번 행이 '{verdict}'인데 근거 칸이 비어 있음(확인 못 한 것을 확인했다고 적지 않는다)")

    judged = sum(1 for c in rows if len(c) >= 7 and c[5] in {"통과", "미통과"})
    unchecked = sum(1 for c in rows if len(c) >= 7 and c[5] == "〔확인 못 함〕")
    blank = sum(1 for c in rows if len(c) >= 7 and c[5] == "")
    print(f"검토표: {sheet_path.as_posix()} — 행 {len(rows)}건 · 판정됨 {judged} · 확인 못 함 {unchecked} · 비움 {blank}")
    if problems:
        print("멈춤 — 검사 실패:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("통과 — 다섯 검사 모두 맞음(이것은 모양 검사이며, 내용이 맞는지는 사람이 판정한다)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
