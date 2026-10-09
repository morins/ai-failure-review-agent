# AI Failure Patterns — AI 실패 사례와 검증 체크리스트

> AI가 유창하게 답한다고 해서 맞는 것은 아니다. 이 저장소는 AI가 **어디서 어떻게 틀리는지**, 사람이 **무엇을 확인해야 하는지**를 사례 · 체크리스트 · 용어 · 공개 가이드로 모은다. 코드를 몰라도 쓸 수 있다.

[English README](README.md) · 라이선스 MIT · 실제 자료 없음(가상 예시만)

## 왜 만들었나

AI에게 요약이나 초안을 맡기면 결과는 빨리 나온다. 문제는 그다음이다 — **어느 문장을 확인해야 하는지 기준이 없어** 매번 처음부터 다시 읽고, 그래도 틀린 수치와 없는 출처를 놓친다. 되묻기("확실해?")는 소용이 없다. 모델은 다시 한 번 그럴듯한 답을 고를 뿐 원문을 열어 보지 않기 때문이다.

이 저장소는 그 불편 한 문장에서 출발했다. 해결책은 "더 좋은 프롬프트"가 아니라 **무엇을 확인할지 뽑아 주는 표, 사람이 판정을 적는 칸, 그리고 그 표가 규칙대로 만들어졌는지 검사하는 장치**다. 실패 사례는 숨길 것이 아니라 공유 자산이다 — 같은 자리에서 같은 실수를 되풀이하지 않도록.

## 누구에게 필요한가

- 보고서 · 과제 · 논문 초안을 AI로 쓰고 **검토를 본인이 책임지는 사람**
- 팀원 · 학생 · 동료에게 "AI 결과를 이렇게 확인하라"고 **설명해야 하는 사람**
- 개발자가 아니어도 AI 에이전트에게 일을 맡기고 **결과를 판정해야 하는 사람**
- GitHub에 처음 무언가를 올려 보려는 **비개발자**

## 무엇이 들어 있나

| 폴더 | 내용 | 이런 때 연다 |
|---|---|---|
| [cases/](cases/) | AI 실패 유형 10가지 — 증상 · 원리 · 확인 방법 · 예방 규칙 + 짧은 가상 사례 100건(C-001 ~ C-100) | "왜 이렇게 틀리지?" |
| [checklists/](checklists/) | 믿기 전 10가지 · 검증과 확인 A~E · 출처 · 수치 · 맡기기 전 · 끝난 뒤 diff | 결과를 받았을 때 · 일을 맡기기 전 |
| [research/](research/) | 공개 기준 · 권위 출처 맵(재사용 조건) · 10유형 분류와 근거 · 참고 자료와 링크 확인 로그 | "무엇을 근거로 말하나?" · 공개하기 전 |
| [ethics/](ethics/) | AI 사용을 어디까지 어떻게 밝히나 · 책임은 누구 몫인가 | 과제 · 논문 · 보고서를 내기 전 |
| [glossary/](glossary/) | 용어 30여 개 — 뜻보다 "모르면 생기는 실수" 중심 | 설명서에 모르는 말이 나올 때 |
| [github-guide/](github-guide/) | 코드를 몰라도 GitHub에 올릴 수 있는 것 · 공개 전 점검 | 첫 저장소를 만들 때 |
| [license-guide/](license-guide/) | 라이선스를 왜 · 어떻게 고르나 | 공개하기 직전 |
| [templates/](templates/) | 실패 사례 양식 · 검토표 양식 · AI 사용 기록 양식 | 기록을 남길 때 |
| [tools/](tools/) | 검토표 생성기 · 모양 검사기(파이썬 표준 라이브러리만) | 답변 파일을 표로 바꿀 때 |
| [raw/](raw/) | 실습용 가상 AI 답변 2건(일부러 오류를 심음) | 연습할 때 |
| [out/](out/) | 위 예시의 검토표 — 사람이 판정을 적은 상태 | 완성된 모양을 볼 때 |

실습 과정 파일 — [01_페인포인트.md](01_페인포인트.md) · [02_기획안.md](02_기획안.md) · [plan.md](plan.md) · [기록.md](기록.md) · [CLAUDE.md](CLAUDE.md)는 이 저장소가 **어떤 불편에서 출발해 무엇을 검증 기준으로 삼았는지**를 남긴 과정 기록이다. 결과물만이 아니라 과정이 함께 올라간다.

## 빠른 시작 — 3분

1. [checklists/before-trusting-ai-answer.md](checklists/before-trusting-ai-answer.md)를 연다 — AI 답변을 믿기 전에 볼 열 가지
2. 답변 파일을 검토표로 바꾼다(파이썬 3 · 설치 없음)

```bash
python tools/make_review_sheet.py raw/예시_AI답변_02_통계요약.md
```

3. 생성된 `out/검토표_예시02_통계요약.md`를 열어 **판정**(통과 · 미통과 · 〔확인 못 함〕)과 **근거**를 적는다 — 도구는 판정하지 않는다
4. 규칙대로 적었는지 검사한다 — 통과 · 미통과인데 근거가 비어 있으면 멈춘다

```bash
python tools/check_review_sheet.py raw/예시_AI답변_02_통계요약.md out/검토표_예시02_통계요약.md
```

## 실패 유형 한눈에

| 번호 | 유형 | 겉으로 보이는 모습 | 가장 빠른 확인법 |
|---|---|---|---|
| [01](cases/01_hallucination.md) | 환각 | 없는 논문 · 법령 · 수치가 완성형 문장으로 | 제목 · 조문 번호로 실재부터 검색 |
| [02](cases/02_citation-failure.md) | 출처 오류 | 주소는 열리는데 그 문장이 거기 없음 | 열어서 찾기(Ctrl+F) · 쪽 확인 |
| [03](cases/03_context-failure.md) | 맥락 오류 | 다른 나라 · 지난 시점 · 다른 대상 기준으로 답함 | 국가 · 기준일 · 대상 · 단위 네 가지 |
| [04](cases/04_number-failure.md) | 수치 오류 | 합계 · 비율 합 · 단위 · 기간이 어긋남 | 다시 계산 · 비율 합 100 · %와 %p |
| [05](cases/05_prompt-failure.md) | 지시 실패 | 빈칸을 그럴듯한 기본값으로 메움 | 내가 정한 적 없는 선택 찾기 |
| [06](cases/06_completion-claim.md) | 완료 선언 | "다 됐다"는데 안 됐음 · 확인 못 한 것을 확인했다고 적음 | 완료 정의와 대조 · diff · 직접 열기 |
| [07](cases/07_context-loss.md) | 긴 대화 | 아침 규칙이 오후에 사라짐 · 같은 교정 반복 | 규칙이 파일에 있는지 · 새 대화 |
| [08](cases/08_visual-ai-failure.md) | 이미지 · 영상 | 손 · 글자 · 로고 · 차트 수치가 깨짐 | 확대해서 글자 · 손 · 수치 |
| [09](cases/09_security-failure.md) | 보안 실패 | 들어온 글이 지시가 되고, 넣은 것이 다시 나옴 · 키가 커밋됨 | 출력이 내 요청과 같은 일을 했는가 · 출력에서 키 검색 |
| [10](cases/10_excessive-agency.md) | 과잉 자율성 | 삭제 · 범위 밖 수정 · push · reset · 발송을 승인 없이 | 파일 목록 · 원격 이력 · 이력 그래프 |

유형마다 본문 한 편과 부록(짧은 가상 사례 C-001 ~ C-100)이 있다. 유형과 근거의 대응은 [research/02-failure-taxonomy.md](research/02-failure-taxonomy.md).

## 다섯 가지 원칙

1. **틀려도 유창하다** — 모델은 지식을 꺼내는 것이 아니라 가장 그럴듯한 다음 조각을 고른다. 문장이 매끄러운 것은 맞다는 증거가 아니다.
2. **"확실해?"는 소용없다** — 대조할 원문 · 근거의 범위 · 산출물 파일을 준다. 되묻기 대신 자료.
3. **검증과 확인은 다르다** — 검증은 요구대로 만들었는가(기계에 맡길 수 있다), 확인은 받는 사람의 필요를 채우는가(사람의 일). 하나를 통과해도 다른 하나는 남는다.
4. **맡기기 전에 커밋, 끝나면 diff** — 에이전트가 내 파일을 직접 고치므로 무엇이 · 언제 · 왜 바뀌었는지 남기는 장치가 필요하다. 받아들일지 되돌릴지는 사람이 판정한다.
5. **확인하지 못한 것은 확인했다고 적지 않는다** — 〔확인 못 함〕은 실패가 아니라 정직한 기록이다. 산출물의 책임은 검토하고 내보낸 사람에게 있다.

## 이 저장소가 하지 않는 것

- 특정 제품을 비난하지 않는다 — 실패 유형은 모든 언어 모델에 공통이다
- 실제 자료 · 개인정보 · 기관 내부 자료를 담지 않는다 — raw/의 예시는 모두 가상이며 첫 줄에 표시한다
- "이 도구가 맞는지 판정해 준다"고 말하지 않는다 — tools/는 무엇을 확인할지 뽑고 모양을 검사할 뿐이다

## 기여하기

새 실패 사례는 [templates/failure-case-template.md](templates/failure-case-template.md) 양식으로 cases/에 추가한다. 짧은 사례는 해당 유형 파일의 부록에 `C-101`부터 이어 붙인다. 증상 · 원인 · 확인 방법 · 예방 규칙 네 칸이 모두 있어야 하고, 예시는 가상이거나 공개 자료여야 한다. 자세한 규칙은 [CONTRIBUTING.md](CONTRIBUTING.md).

## 라이선스

MIT — 자유롭게 쓰고 고치고 나눌 수 있다. 문서를 옮겨 쓸 때는 이 저장소 주소를 출처로 적어 주면 고맙다. 왜 MIT인지는 [license-guide/choose-a-license.md](license-guide/choose-a-license.md). 공개 표준(OWASP 등)에서는 항목의 이름 · 번호 · 링크만 가져오고 설명은 자체 작성했으므로 다른 라이선스가 따라오지 않는다.

인용은 [CITATION.cff](CITATION.cff) — GitHub의 "Cite this repository"에서 그대로 복사할 수 있다.

## 근거로 삼은 공개 자료

이 저장소의 분류 · 용어 · 체크리스트는 아래 공개 자료의 **개념과 항목 이름**에 기대고, 설명은 모두 이 저장소의 말로 다시 썼다. 재사용 조건 · 확인 방법은 [research/01-source-map.md](research/01-source-map.md), 링크와 확인 로그는 [research/07-references.md](research/07-references.md).

- **AI 위험 · 신뢰성** — NIST AI RMF 1.0(2023) · NIST AI 600-1 생성형 AI 프로파일(2024, 컨패뷸레이션 정의) · OWASP Top 10 for LLM Applications 2025 · MIT AI Risk Repository · AI Incident Database · Stanford HAI AI Index · Stanford 법률 AI 연구(*Hallucination-Free?*)
- **원리 · 운용** — Kalai et al. (2025) *Why Language Models Hallucinate* · Anthropic (2024) *Building Effective Agents* · Anthropic (2025) *Effective Context Engineering for AI Agents* · Anthropic (2025) *Effective Harnesses for Long-Running Agents* · Claude Code 문서(best practices · memory · permissions · checkpointing)
- **윤리 · 정책 · 공개** — OECD AI 원칙(2019 · 2024 갱신) · UNESCO AI 윤리 권고(2021) · EU AI 법 제50조(투명성) · C2PA 콘텐츠 자격 증명 · ICMJE · COPE · Nature Portfolio · ACM 저자 정책
- **GitHub** — 저장소 라이선스 · .gitignore · secret scanning · push protection · 민감정보 제거 · CITATION 파일 · 커밋 이메일 비공개 · 2단계 인증

확인일 2026-10-10 — 링크 32건을 자동으로 열어 30건이 정상 응답, 2건(COPE · ACM)은 자동 접근이 차단(403)되어 브라우저로 직접 확인해야 한다고 표시했다. 세부 수치는 원문에서 확인한 것만 옮겼다 — 원문을 직접 여는 것이 이 저장소의 원칙이다.
