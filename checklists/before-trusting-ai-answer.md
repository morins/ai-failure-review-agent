# AI 답변을 믿기 전에 — 열 가지 · Before trusting an AI answer — ten checks

**EN** Right after you receive an answer and before you reuse it: numbers (recompute), sources (exist → attributed → cited correctly), links (open and find the sentence), dates ("now" is the model's training date), country · population · unit, absolute claims, totals and shares, what is missing, images and charts, and choices you never made. Anything that fails is 〔확인 못 함〕 (could not verify), not a pass. Korean table below.

> 답을 받은 직후, 옮겨 쓰기 전에. 한 항목 = 무엇을 · 왜 · 어떻게. 전부 보는 데 5분이면 되고, 하나라도 걸리면 그 문장은 〔확인 못 함〕이다.

| # | 무엇을 | 왜 | 어떻게 |
|---|---|---|---|
| 1 | **수치** — 숫자가 있는 문장 전부 | 숫자도 확률로 골라진 말이다. 계산 결과가 아니다 | 원자료를 열어 같은 값 · 같은 단위 · 같은 기간인지. 본문 안에 분자 · 분모가 있으면 직접 나눈다 → [number-check](number-check.md) |
| 2 | **출처** — 인용 · 참고문헌 · 법령 조문 | 출처 모양과 내용은 따로 만들어진다 | 실재(검색) → 귀속(그 쪽에 그 문장) → 표기(연도 · 쪽) → [citation-check](citation-check.md) |
| 3 | **주소** — URL · DOI | 열리는 주소에 그 내용이 없을 수 있다 | 연다 · 제목이 본문 설명과 같은지 · 그 문장을 Ctrl+F |
| 4 | **시점** — "현재" · "최근" · 기준 연월 | 모델의 "현재"는 학습 시점이다 | 자료 기준일과 문장의 시점이 같은지 · 개정 · 시행일 |
| 5 | **나라 · 대상 · 단위** | 적지 않은 맥락은 가장 흔한 기본값으로 채워진다 | 어느 나라 제도인지 · 분모가 무엇인지 · 천/만/억 · 원/달러 · %/%p |
| 6 | **단정** — "모든" · "확실히" · "입증됐다" | 근거 없이 붙는 흔한 조각이다 | 근거가 문장 옆에 있는가. 없으면 완화하거나 삭제 |
| 7 | **합계 · 비율 합** | 합계 문장은 값과 무관하게 붙는다 | 비중의 합이 100인지(반올림 ±0.2) · 합계를 다시 더한다 |
| 8 | **빠진 것** — 결과에 없는 것 | 결과가 나오면 빠진 것은 안 보인다 | 몇 건이어야 하는지 먼저 센다(원자료 행 수 · 질문의 항목 수) · 결과의 건수와 비교 |
| 9 | **그림 · 표 · 차트** | 생성된 그림은 데이터에서 그린 것이 아니다 | 확대해서 글자 · 손 · 로고 · 축 눈금 · 막대 높이 vs 숫자 → [08 사례](../cases/08_visual-ai-failure.md) |
| 10 | **내가 정한 적 없는 선택** | 빈칸은 추측으로 메워진다 | 분류 체계 · 형식 · 범위 · 끝난 시점 중 내가 정하지 않은 것 → [05 사례](../cases/05_prompt-failure.md) |

## 하지 말 것

- **"확실해?"라고 되묻기** — 같은 추측을 한 번 더 시키는 것이다. 대신 대조할 원문을 준다: "raw/표.md의 3행과 대조해서 다른 칸을 보여줘."
- **유창함을 근거로 삼기** — 매끄러운 문장은 맞다는 증거가 아니다. 틀려도 유창하다.
- **확인하지 못한 것을 통과로 적기** — 〔확인 못 함〕은 정직한 기록이다. 통과 · 미통과에는 근거를 적는다.
- **열 가지를 머릿속으로만 하기** — 표로 남긴다 → [templates/ai-output-review-sheet.md](../templates/ai-output-review-sheet.md) 또는 `python tools/make_review_sheet.py 파일`

## 끝나면

- 미통과 몇 건 · 확인 못 함 몇 건 · 이 답변을 그대로 쓸 수 있는가 — 세 줄을 검토표 아래에 적는다
- 같은 종류의 미통과가 두 번째면 → 결과물이 아니라 요청문 · 규칙 파일을 고친다
