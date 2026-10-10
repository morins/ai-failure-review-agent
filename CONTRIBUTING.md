# 기여 안내 · Contributing

**EN** This repository collects AI failure cases as a shared asset. Add new cases in the same shape (symptoms · cause · how to check · prevention rule), keep every example synthetic or public, never target a product or a person, cite only sources you actually opened, and do not add any "auto pass/fail" feature to the tools. Short cases go at the end of the matching appendix, numbered from C-101. Open a pull request with a one-line "what and why" commit message. Korean details below.

이 저장소는 AI 실패 사례를 **공유 자산**으로 모은다. 고치는 것보다 먼저 **같은 양식으로 적는 것**이 기여다.

## 무엇을 보탤 수 있나

| 보탤 것 | 어디에 | 양식 |
|---|---|---|
| 새 실패 유형 | cases/NN_slug.md | [templates/failure-case-template.md](templates/failure-case-template.md) |
| 기존 유형의 새 예시 | 해당 cases/ 파일의 "실제 모습" 절 | 가상 예시 또는 공개 자료 |
| 짧은 가상 사례(한 장면) | 해당 cases/ 파일의 부록 끝 | `#### C-101 · 제목` + 상황(가상) · 증상 · 원인 · 확인 방법 · 예방 규칙 — 번호는 마지막 번호 다음 |
| 근거 자료 · 링크 | research/07-references.md | 열어 본 날짜와 결과(200 · 403 등)를 함께 |
| 체크리스트 항목 | checklists/ | 한 항목 = 무엇을 · 왜 · 어떻게 |
| 용어 | glossary/ai-glossary.md | 뜻 · 모르면 생기는 실수 · 예방 |
| 도구 개선 | tools/ | 표준 라이브러리만 · 판정 기능은 넣지 않는다 |
| 오타 · 깨진 링크 | 어디든 | 그냥 고치고 이유 한 줄 |

## 지켜야 할 것

1. **실제 자료를 넣지 않는다** — 사람 이름 · 기관 내부 사정 · 연락처 · 실제 수치 · 고객 자료. 예시는 가상으로 만들고 첫 줄에 "실습용으로 지어낸 예시"라고 적는다.
2. **특정 제품을 비난하지 않는다** — "어느 서비스가 이렇게 틀렸다"가 아니라 "이런 모양으로 틀린다"로 적는다. 실패 유형은 모든 언어 모델에 공통이다.
3. **출처는 공개 자료만** — 논문 · 공식 문서 · 공개 블로그. 제목 · 발행처 · 연도를 적고, 열어 보지 않은 자료는 인용하지 않는다(이 저장소의 원칙이다).
4. **네 칸을 비우지 않는다** — 증상 · 원인 · 확인 방법 · 예방 규칙. 모르는 칸은 〔확인 필요〕로 남기고 지어내지 않는다.
5. **도구는 판정하지 않는다** — tools/에 "자동으로 통과를 매기는" 기능은 넣지 않는다. 무엇을 확인할지 뽑고 모양을 검사하는 데까지만.

## 보내는 법

1. 저장소를 포크(fork)한다
2. 브랜치를 만든다 — 이름은 무엇을 고치는지 보이게(예: `case-table-numbers`)
3. 고치고 커밋한다 — 커밋 메시지는 **무엇을 왜** 한 줄(예: "표 형식 답변 사례 추가 — 표 줄은 건너뛰는 규칙 때문에 놓친 예시가 있어서")
4. 풀 리퀘스트를 연다 — 바뀐 줄 옆에 의견이 달리므로 작게 자주가 좋다

GitHub이 처음이면 [github-guide/github-for-non-developers.md](github-guide/github-for-non-developers.md)부터.

## 검토 기준

- 양식의 네 칸이 다 있는가 · 예시가 가상/공개인가 · 특정 제품을 겨냥하지 않는가 · 출처를 열어 봤는가
- tools/를 고쳤다면: `python tools/make_review_sheet.py raw/예시_AI답변_01_정책브리프.md` 와 `python tools/check_review_sheet.py …` 가 여전히 "통과"인가
