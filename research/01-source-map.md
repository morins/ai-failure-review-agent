# 01 · 권위 출처 맵 — 무엇에 쓰고 · 어떤 조건으로 · 무엇을 확인했나

> 저장소의 각 부분이 어떤 공개 자료에 기대는지, 그 자료를 옮겨 쓸 때 지킬 조건은 무엇인지, 그리고 **이 저장소가 2026-10-10에 실제로 무엇을 열어 확인했는지**를 한 표에 둔다. 확인하지 못한 것은 〔확인 못 함〕으로 남긴다 — 이 저장소의 규칙이다.

## 1 출처표

| 출처 | 발행 · 연도 | 이 저장소에서 쓰는 것 | 재사용 조건 | 확인(2026-10-10) |
|---|---|---|---|---|
| **NIST AI RMF 1.0** | 미국 NIST, 2023 | 신뢰할 수 있는 AI의 특성(유효 · 신뢰 · 안전 · 보안 · 책임 · 투명 · 설명 가능 · 프라이버시 · 공정)과 거버넌스 틀 — 체크리스트 A~E의 배경 | 미국 정부 간행물 — 요약 · 인용 자유, 출처 표기 | 링크 응답 200 · 본문 대조는 하지 않음 |
| **NIST AI 600-1** 생성형 AI 프로파일 | NIST, 2024-07 | 컨패뷸레이션(confabulation) 정의 · 생성형 AI 12개 위험 | 요약 · 인용 자유, 출처 표기 | PDF 64쪽 내려받아 정의 문장 확인 — 원문: "Confabulation: The production of confidently stated but erroneous or false content (known colloquially as "hallucinations" or "fabrications") by which users may be misled or deceived." |
| **OWASP Top 10 for LLM Applications 2025** | OWASP, 2024-11-18 | 항목 이름과 번호(LLM01 프롬프트 인젝션 ~ LLM10 무제한 소비) — 사례 09 · 10 · 용어 사전 | **CC BY-SA 4.0** — 출처 표기 + 파생물도 같은 조건. 이 저장소는 **이름 · 번호만** 인용하고 설명은 자체 작성 | PDF 45쪽 내려받아 라이선스 문구("licensed under Creative Commons, CC BY-SA 4.0")와 항목명(LLM01 Prompt Injection · LLM06 Excessive Agency · LLM10 Unbounded Consumption) 확인 |
| **MIT AI Risk Repository** | MIT, 2025 갱신 | AI 위험의 도메인 분류 — 유형 분류의 참고 | 공개 접근 — 인용 · 요약 시 출처 표기 | 사이트 열람 — "1,612개 분류된 위험으로 확장" 문구 확인 · 도메인 · 하위도메인 수는 〔확인 못 함〕 |
| **AI Incident Database** | Responsible AI Collaborative, 상시 | 실제 사고 사례의 존재 — 이 저장소는 개별 사례를 옮기지 않음 | 오픈 데이터 — 출처 표기, 개별 사례는 원문 링크 | 링크 응답 200 |
| **Stanford HAI AI Index** | Stanford HAI, 2025 | 실측 지표가 있는 보고서라는 사실 | 인용 · 요약, 출처 표기 | 링크 응답 200 · 리서치 컬렉션의 "모델 환각률 22~94%"는 첫 화면에서 찾지 못해 〔확인 못 함〕 → 이 저장소는 그 수치를 쓰지 않음 |
| **Stanford 법률 AI 연구 *Hallucination-Free?*** | Stanford(RegLab · HAI), 2024 | 법률 RAG 도구도 환각한다는 실측 — 사례 02의 배경 | 논문 인용(저자 · 연도 · 제목 · 링크) | PDF 27쪽 내려받아 수치 확인 — 법률 RAG 도구 **17~33%**, 선행연구(Dahl et al. 2024)의 범용 LLM **58~82%**. 리서치 컬렉션의 "58~88%"는 오기 → 정정 |
| **OECD AI 원칙** | OECD, 2019(2024 갱신) | 가치 기반 원칙 — 윤리 가이드의 배경 | 요약 · 인용, 출처 표기 | 링크 응답 200 · 본문 대조는 하지 않음 |
| **UNESCO AI 윤리 권고** | UNESCO, 2021-11 | 투명성 · 책임성 — 윤리 가이드의 배경 | 요약 · 인용, 출처 표기 | 링크 응답 200 · "193개 회원국 채택"은 이번에 본문 대조하지 않음 〔확인 못 함〕 |
| **EU AI 법 제50조**(투명성 의무) | EU, 적용 2026-08-02 | AI와의 상호작용 고지 · 합성 콘텐츠의 기계 판독 표시 · 딥페이크 라벨 — 사례 08 · 윤리 가이드 | 법령 인용, 출처 표기 | 페이지 열람 — "Comes into force 2 August 2026, according to Article 113" 확인 |
| **C2PA 콘텐츠 자격 증명** | C2PA, 사양 2.x | 콘텐츠 출처 · 편집 이력 표준 — 생성물 표시 방법 | 사양 공개 — 인용 · 요약, 버전 · 사이트 표기 | c2pa.org 응답 200 · 사양 사이트는 리디렉션 페이지만 받아 **버전(2.4)은 〔확인 못 함〕** |
| **ICMJE** AI 사용 권고 | ICMJE, 2023~ | AI는 저자 불가 · 사용 공개 — 윤리 가이드 8절 | 정책 요약 · 인용 | 링크 응답 200 · 본문 대조는 하지 않음 |
| **COPE** 저자와 AI 도구 입장 | COPE, 2023 | 같음 | 정책 요약 · 인용 | **자동 접근 403** 〔확인 못 함 — 브라우저로 직접 열 것〕 |
| **Nature Portfolio** AI 정책 | Nature, 2023~ | AI 저자 불가 · 생성 이미지 제한 · 방법 절에 공개 | 정책 요약 · 인용 | 링크 응답 200 · 본문 대조는 하지 않음 |
| **ACM** 저자 정책 | ACM, 2023~ | 생성형 AI 사용 정책 — 리서치 컬렉션은 "텍스트 작성 도움의 공개 의무 완화"라고 정리 | 정책 요약 · 인용 | **자동 접근 403** 〔확인 못 함 — 완화 여부는 원문으로 확인할 것〕 |
| **GitHub Docs** | GitHub, 상시 | 저장소 라이선스 · .gitignore · secret scanning · push protection · 민감정보 제거 · CITATION 파일 · 저장소 모범 사례 · 계정 · 2단계 인증 · 커밋 이메일 | 문서 인용, 출처 표기 | 링크 11건 응답 200 · 라이선스 페이지의 문장("You're under no obligation to choose a license. However, without a license, the default copyright laws apply … we strongly encourage you to include an open source license.") 확인 |
| **Kalai et al. (2025)** *Why Language Models Hallucinate* | OpenAI, 2025 | 모델이 모른다고 말하기보다 추측하도록 평가되어 온 구조 — 사례 01 | 논문 인용 | 제목 · 발행처로 인용 · 이번 자동 확인 범위 밖 〔링크 확인 못 함〕 |
| **Anthropic** *Building Effective Agents*(2024) · *Effective Context Engineering for AI Agents*(2025) · *Effective Harnesses for Long-Running Agents*(2025) · **Claude Code 문서** | Anthropic | 에이전트 · 컨텍스트 창 · 압축 · 완료 선언 · 권한 · 되돌리기 — 사례 05 · 06 · 07 · 10 | 문서 인용, 출처 표기 | 제목 · 발행처로 인용 · 이번 자동 확인 범위 밖 〔링크 확인 못 함〕 |

## 2 NIST AI 600-1이 드는 생성형 AI의 12개 위험

CBRN 정보 · 역량 / 컨패뷸레이션(환각) / 위험 · 폭력 · 증오 콘텐츠 / 데이터 프라이버시 / 환경 영향 / 유해 편향 · 동질화 / 인간-AI 구성 / 정보 무결성 / 정보 보안 / 지식재산 / 외설 · 모욕 콘텐츠 / 가치사슬 · 구성요소 통합 — 이 저장소의 10유형은 이 가운데 **컨패뷸레이션 · 정보 무결성 · 정보 보안 · 인간-AI 구성**과 맞닿는다. (목록 번호 2 · 3의 원문 문장을 PDF에서 확인 · 나머지 항목명은 리서치 컬렉션의 정리를 따름)

## 3 OWASP Top 10 for LLM Applications 2025 — 항목 이름만

LLM01 Prompt Injection · LLM02 Sensitive Information Disclosure · LLM03 Supply Chain · LLM04 Data and Model Poisoning · LLM05 Improper Output Handling · LLM06 Excessive Agency · LLM07 System Prompt Leakage · LLM08 Vector and Embedding Weaknesses · LLM09 Misinformation · LLM10 Unbounded Consumption — 문서 라이선스 CC BY-SA 4.0. **설명 문장은 옮기지 않았다.** 설명이 필요하면 원문을 연다.

## 4 출처별 재사용 규칙 — 한 줄씩

| 자료 유형 | 해도 되는 것 | 반드시 할 것 |
|---|---|---|
| 미국 정부 간행물(NIST) | 요약 · 표 변형 · 인용 · 재배포 | "출처: NIST AI 600-1 (2024)" 표기 |
| OWASP 문서(CC BY-SA 4.0) | 요약 · 각색 · 상업적 이용 | 출처 표기 + 파생물도 CC BY-SA 4.0 — 피하려면 이름 · 번호 · 링크만 |
| MIT AI Risk Repository · AI Incident Database | 분류 · 데이터 요약, 연구 인용 | 출처와 원문 링크 |
| OECD · UNESCO · EU 법령 | 원칙 · 조항 요약 · 인용 | 공식 문서명 · 연도 · 조문 |
| C2PA 사양 | 표준 개요 · 용어 설명 | 사양 버전 · 사이트 표기 — 버전을 모르면 "2.x" |
| 학술 논문 | 수치 · 결론 인용 | 저자 · 연도 · 제목 · 링크 — 수치는 원문에서 확인한 것만 |
| GitHub Docs · 제품 문서 | 절차 · 문구 인용 | 문서명 · 확인일 — 화면 문구는 바뀐다 |

## 5 확인 방법(재현용)

1. 링크 전수 — 각 주소를 자동으로 열어 응답 코드를 기록([07-references.md](07-references.md)의 로그)
2. 핵심 주장 대조 — 수치 · 정의 · 날짜가 걸린 자료(NIST 600-1 · OWASP · Stanford 법률 연구 · MIT 저장소 · GitHub 라이선스 페이지 · EU 제50조 · AI Index · C2PA)는 원문을 내려받아 그 문장을 검색
3. 못 찾은 것은 수치를 쓰지 않거나 〔확인 못 함〕으로 표시 — 리서치 컬렉션의 정리를 그대로 믿지 않았다
4. 자동 접근이 막힌 곳(403)은 사람이 브라우저로 열어야 한다 — 그 전까지 〔확인 못 함〕

출처 — 2026-10-10 리서치 컬렉션(ai-failure-patterns-research.pdf) 섹션 4 · 5를 바탕으로, 이 저장소가 같은 날 수행한 확인 결과를 더해 다시 작성.
