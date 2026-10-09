# research/ — 근거 자료와 공개 기준

이 폴더는 저장소의 본문(cases · checklists · glossary · ethics · license-guide)이 **무엇을 근거로 말하는지**와 **무엇을 공개해도 되는지**를 적어 둔 곳이다. 읽는 순서는 번호 순.

| 파일 | 내용 | 이런 때 연다 |
|---|---|---|
| [00-publication-criteria.md](00-publication-criteria.md) | GitHub 공개 가능 · 불가 기준, GitHub 공식 문서 근거, 이 저장소가 쓴 점검 절차 | 공개하기 전 · 무엇을 올려도 되는지 애매할 때 |
| [01-source-map.md](01-source-map.md) | 권위 출처 맵 — 출처마다 쓰는 것 · 재사용 조건 · 2026-10-10 확인 결과 | 인용할 때 · 라이선스가 따라오는지 볼 때 |
| [02-failure-taxonomy.md](02-failure-taxonomy.md) | 10유형 분류와 근거, 네 칸 요약, 리서치 컬렉션 8유형과의 대응 | 사례를 어느 유형에 넣을지 정할 때 |
| [07-references.md](07-references.md) | 전체 출처와 링크 확인 로그(응답 코드 · 본문 대조 여부 · 정정 사항) | 링크를 다시 확인할 때 · 출처를 추가할 때 |

번호 03~06은 따로 두지 않았다 — 체크리스트 · 공개 가이드 · 용어 사전 · 라이선스 가이드는 본문 폴더의 파일이 곧 쓸 수 있는 판이기 때문이다: [checklists/verification-vs-validation.md](../checklists/verification-vs-validation.md) · [ethics/ai-use-disclosure-guide.md](../ethics/ai-use-disclosure-guide.md) · [glossary/ai-glossary.md](../glossary/ai-glossary.md) · [license-guide/choose-a-license.md](../license-guide/choose-a-license.md).

## 어떻게 만들어졌나

1. **2026-10-10 리서치 컬렉션** — "AI Failure Patterns — 리서치 & 소스 컬렉션"(ai-failure-patterns-research.pdf, 14쪽)과 같은 내용의 마크다운 번들(28파일)을 받았다. 공개 기준 · 권위 출처 맵 · 8유형 분류 · 가상 사례 100건 · 체크리스트 · 공개 가이드 · 용어 · 라이선스 · 참고 자료가 들어 있었다.
2. **결합** — 이 저장소의 8유형 본문에 보안 실패(09) · 과잉 자율성(10)을 더해 10유형으로 맞추고, 가상 사례 100건은 유형별 파일의 부록으로 붙였다(번호 C-001 ~ C-100 유지). 체크리스트 A~E · 용어 · 공개 가이드의 출판처별 차이 · 라이선스 주의는 본문 파일에 녹였다.
3. **확인** — 링크 32건을 자동으로 열어 응답을 기록하고, 수치 · 정의 · 날짜가 걸린 자료 8건은 원문을 내려받아 그 문장을 찾았다. 못 찾은 것은 수치를 버리거나 〔확인 못 함〕으로 표시했다. 리서치 컬렉션이 정리한 내용을 **그대로 믿지 않았다** — 실제로 수치 하나(58~88% → 58~82%)를 정정했다.
4. **라이선스** — 리서치 컬렉션은 OWASP 자료 요약을 이유로 CC BY-SA 4.0을 권했지만, 이 저장소는 OWASP에서 항목 이름 · 번호 · 링크만 가져오고 설명을 자체 작성했으므로 MIT를 유지했다. 근거는 [../license-guide/choose-a-license.md](../license-guide/choose-a-license.md) 4절.

## 이 폴더의 규칙

- 출처는 **열어 본 것만** 적는다. 열지 못했으면 〔확인 못 함〕.
- 응답 코드 200은 "열린다"일 뿐 "그 문장이 있다"가 아니다 — 본문 대조를 했으면 그렇게 적는다.
- 수치는 원문에서 찾은 것만 옮긴다. 정책 · 법령 · 수치는 개정되므로 확인일을 적는다.
- 남의 원문을 옮기지 않는다 — 요약과 링크. 라이선스가 따라오는 자료는 이름 · 번호만.
