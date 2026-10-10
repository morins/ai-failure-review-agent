# ai-failure-review-agent — 실패 유형 기반 AI 검토 에이전트
### A failure-type-based review agent for AI output

> **KO** AI가 써 준 글 · 표 · 그림을 그대로 믿기 전에 **어디가 어떻게 틀릴 수 있는지**를 열 가지 유형으로 짚고, **무엇을 확인해야 하는지**를 표로 뽑아 주며, 그 확인 과정을 **다섯 단계 관문**으로 보여 주는 공개 학습형 프로젝트입니다. 코드를 몰라도 쓸 수 있고, 기본 모드에서는 올린 파일이 어디로도 가지 않습니다.
>
> **EN** Before you trust what an AI wrote, drew, or tabulated: this project names **the ten ways AI output goes wrong**, pulls out **exactly which sentences you must check**, and shows the checking process as a **five-gate review loop**. No coding needed. In the default mode, nothing you upload leaves your computer.

**ⓒ METACURATION · CC BY-NC 4.0** — 비영리 이용은 출처 표기만으로 자유, 상업적 이용은 별도 협의 / Free for non-commercial use with attribution; commercial use by separate agreement. · 모든 예시는 가상 / All examples are synthetic. · [한국어 전용 README](README.ko.md)

---

## 1. 이 프로젝트가 하는 일 · What this project does

| | **KO** | **EN** |
|---|---|---|
| **① 실패 유형 사례집**<br>Casebook | AI 답변이 틀리는 모양을 **열 가지**로 나누고, 유형마다 증상 · 원리 · 확인 순서 · 예방 규칙을 적었습니다. 짧은 가상 사례 100건(C-001 ~ C-100)이 부록으로 붙어 있습니다. → [cases/](cases/) | Ten ways AI answers fail, each with symptoms, mechanism, a checking order, and prevention rules, plus 100 short synthetic cases as appendices. |
| **② 체크리스트와 도구**<br>Checklists & tools | 답을 받았을 때 · 맡기기 전 · 끝난 뒤에 볼 체크리스트 6종. AI 답변 파일에서 확인할 문장을 뽑아 **검토표**를 만들고, 그 표가 규칙대로 적혔는지 검사하는 파이썬 도구 2개(설치 없음). → [checklists/](checklists/) · [tools/](tools/) | Six checklists for receiving output, delegating, and reviewing afterwards; two small Python tools that build a **review sheet** from an answer file and check that the sheet follows its own rules. |
| **③ 검토 에이전트 페이지**<br>Review-agent page | [failure-peer-review-agent.html](failure-peer-review-agent.html)을 브라우저에서 열어 파일을 끌어다 놓으면 "업로드 → 검토 → 감지 → 보완 → 통과" 다섯 단계와 열 가지 유형을 눈으로 보고, 결과를 검토표(.md) · JSON으로 내려받습니다. 기본은 데모, **본인 API 키를 넣으면(선택) 실제 모델이 텍스트 파일을 검토**합니다. | Open the page in a browser, drop a file, watch the five gates and ten types light up, and export a review sheet (.md) or JSON. Demo by default; **with your own API key (optional) a real model reviews your text files**. |

**한 줄로 / In one line** — "AI가 다 됐다고 해도, 통과 판정은 사람이 한다." / "Even when the AI says it's done, the pass verdict belongs to a human."

## 2. 76초 소개 영상 · 76-second intro video

[![소개 영상 미리보기 · Intro preview — 클릭하면 전체 영상(MP4) / click for the full MP4](media/intro-teaser.gif)](media/intro.mp4)

- **KO** 전체 영상(음성 포함) → [media/intro.mp4](media/intro.mp4) · 기획 · 장면 표 → [media/intro-storyboard.md](media/intro-storyboard.md). "AI는 틀려도 유창하다"는 한 문장에서 출발해 열 개의 함정과 다섯 개의 관문을 76초에 설명합니다. 내레이션은 신경망 음성, 음악 · 효과음은 코드로 합성했습니다(외부 음원 없음).
- **EN** Full video with narration → [media/intro.mp4](media/intro.mp4) · storyboard → [media/intro-storyboard.md](media/intro-storyboard.md). Starting from "AI is fluent even when wrong", it explains the ten traps and five gates in 76 seconds. Neural-voice narration; music and effects synthesized in code (no third-party audio).

## 3. 누구에게 필요한가요 · Who it is for

| 이런 분 · You | 이렇게 쓰세요 · Start here |
|---|---|
| 보고서 · 과제 · 논문 초안을 AI로 쓰고 검토를 본인이 책임지는 분 / Draft reports, assignments, or papers with AI and own the review | [믿기 전 열 가지 · Before trusting an answer](checklists/before-trusting-ai-answer.md) → 검토표 도구로 확인할 문장 뽑기 / build a review sheet with the tools |
| 팀 · 학생 · 동료에게 "AI 결과를 이렇게 확인하라"고 설명해야 하는 분 / Must explain to a team or class how to check AI output | 영상과 페이지를 보여 주고 [cases/](cases/)의 유형표를 나눠 주기 / show the video and page, hand out the type table |
| AI 에이전트에게 일을 맡기고 결과를 판정해야 하는 분 / Delegate work to AI agents and judge the result | [맡기기 전 · Before delegating](checklists/delegation-check.md) → [끝난 뒤 바뀐 줄 읽기 · Reading the diff](checklists/diff-review-check.md) |
| 공개 저장소를 처음 만드는 비개발자 / Publishing a first repository without code | [GitHub 가이드](github-guide/github-for-non-developers.md) → [라이선스 고르기](license-guide/choose-a-license.md) → [공개 기준](research/00-publication-criteria.md) |

## 4. 30초 체험 — 페이지 열기 · 30-second tour — the page

1. **KO** 저장소를 내려받거나 복제합니다(초록색 **Code** 단추 → Download ZIP). / **EN** Download or clone the repository (green **Code** button → Download ZIP).
2. **KO** `failure-peer-review-agent.html`을 더블클릭해 브라우저에서 엽니다. 서버 · 설치 · 로그인이 필요 없습니다. / **EN** Double-click `failure-peer-review-agent.html`. No server, install, or login.
3. **KO** 아무 파일이나 끌어다 놓고 **검토 시작**을 누릅니다. 다섯 단계가 차례로 켜지고, 의심 지점은 빨강, 보완 후보는 파랑으로 표시됩니다. / **EN** Drop any file and press **검토 시작** (Start review). The five stages light up; suspected issues show in red, repair candidates in blue.
4. **KO** **검토표 내보내기(.md)** 를 누르면 판정 칸이 비어 있는 검토표가 내려받아집니다. 판정은 직접 적습니다. / **EN** Press **검토표 내보내기 (.md)** to download a review sheet whose verdict column is empty — you fill it in.

**기본 모드 · Default mode** — **KO** 시뮬레이션입니다. 실제 AI 모델을 부르지 않고 파일 내용을 읽지 않으며(이름 · 크기만 사용) 외부 요청이 하나도 없습니다. / **EN** A simulation: it does not call an AI model, never reads file contents (only names and sizes), and makes zero external requests.

**실제 모델 연결(선택) · Optional real-model mode** — **KO** 페이지의 "실제 모델 연결" 칸에 제공자(OpenAI 호환 · Anthropic) · 엔드포인트 · 모델 · 본인 API 키를 넣으면 .txt · .md · .csv · .json 파일(앞 60,000자)을 실제 모델이 읽고 "확인할 지점"을 열 가지 유형으로 돌려줍니다. 키와 파일 내용은 브라우저에서 **본인이 지정한 제공자에게만** 전송되고, 이 페이지에는 서버가 없어 저장소 운영자에게는 아무것도 오지 않습니다. 개인정보 · 기관 내부 자료는 넣지 마세요. 모델의 답도 판정이 아니라 확인할 지점의 목록입니다. / **EN** Open the "실제 모델 연결(선택)" panel, choose a provider (OpenAI-compatible or Anthropic), and enter an endpoint, a model name, and your own API key. Text files (.txt · .md · .csv · .json, first 60,000 characters) are sent from your browser **directly to the provider you chose** and come back as "points to verify" by the ten types. No server sits behind the page, so nothing reaches the repository owner. Do not upload personal or internal data. The model's output is a list to verify, not a verdict.

## 5. 3분 실전 — 검토표 만들기 · 3-minute practice — build a review sheet

**KO** 파이썬 3만 있으면 됩니다(설치할 것 없음). 연습용으로 `raw/`에 일부러 오류를 심은 가상 답변 두 건이 있습니다. / **EN** Python 3 only, nothing to install. Two synthetic answers with planted errors are in `raw/` for practice.

```bash
python tools/make_review_sheet.py raw/예시_AI답변_02_통계요약.md
```

**KO** 생성된 `out/검토표_예시02_통계요약.md`를 열어 **판정**(통과 · 미통과 · 〔확인 못 함〕)과 **근거**를 적습니다. 도구는 판정하지 않습니다. 그다음 규칙대로 적었는지 검사합니다 — 통과 · 미통과인데 근거가 비어 있으면 멈춥니다. / **EN** Open the generated sheet in `out/`, write the **verdict** (통과 pass · 미통과 fail · 〔확인 못 함〕 could not verify) and the **evidence**. The tool never judges. Then check that the sheet follows its own rules — a pass or fail without evidence stops the check.

```bash
python tools/check_review_sheet.py raw/예시_AI답변_02_통계요약.md out/검토표_예시02_통계요약.md
```

완성된 모양 · A finished example: [out/검토표_예시01_정책브리프.md](out/검토표_예시01_정책브리프.md)

## 6. 무엇이 들어 있나 · What is inside

| 파일 · 폴더 / File · folder | KO | EN |
|---|---|---|
| [failure-peer-review-agent.html](failure-peer-review-agent.html) | 검토 에이전트 페이지 — 다섯 단계 관문 · 열 유형 · 내보내기 · 본인 키로 실제 모델 검토(선택) | Review-agent page — five gates, ten types, export, optional real-model review with your own key |
| [cases/](cases/) | 실패 유형 10가지 본문 + 짧은 가상 사례 100건 | Ten failure patterns + 100 short synthetic cases |
| [checklists/](checklists/) | 믿기 전 열 가지 · 검증과 확인 A~E · 출처 · 수치 · 맡기기 전 · 끝난 뒤 | Before trusting · verification vs validation (A–E) · citations · numbers · before delegating · reading the diff |
| [tools/](tools/) | 검토표 생성기 · 모양 검사기(표준 라이브러리만) | Review-sheet generator and shape checker (standard library only) |
| [raw/](raw/) · [out/](out/) | 연습용 가상 답변 2건과 그 검토표 | Two synthetic answers with planted errors and their sheets |
| [ethics/](ethics/) | AI 사용을 어디까지 어떻게 밝히나 · 책임 · 출판처별 차이 | How much AI use to disclose, who is responsible, how publishers differ |
| [glossary/](glossary/) | 용어 40여 개 — "모르면 생기는 실수" 중심 | ~40 terms, each with "the mistake you make if you don't know it" |
| [github-guide/](github-guide/) · [license-guide/](license-guide/) | 코드 없이 GitHub에 올리는 법 · 공개 전 점검 · 라이선스 고르기 | Publishing on GitHub without code · pre-publish security review · choosing a license |
| [research/](research/) | 공개 기준 · 근거 자료 맵(재사용 조건 · 확인 결과) · 10유형 분류 · 참고 자료와 링크 확인 로그 | What may be published · source map with reuse terms and verification results · taxonomy · references with a link-check log |
| [templates/](templates/) | 실패 사례 양식 · 검토표 양식 · AI 사용 기록 양식 | Failure-case form · review-sheet form · AI-use log |
| [media/](media/) | 소개 영상 · 미리보기 GIF · 스토리보드 | Intro video, teaser GIF, storyboard |
| `01_페인포인트.md` · `02_기획안.md` · `plan.md` · `기록.md` · `CLAUDE.md` | 이 프로젝트가 어떤 불편에서 출발해 무엇을 완료 기준으로 삼았는지 남긴 과정 기록과 에이전트용 규칙 | Process records (pain point, spec, plan, log) and the rules file for agents — in Korean |

## 7. 실패 유형 열 가지 · The ten failure types

| # | 유형 · Type | 겉으로 보이는 모습 · What you see | 가장 빠른 확인법 · Fastest check |
|---|---|---|---|
| [01](cases/01_hallucination.md) | 환각 · Hallucination | 없는 논문 · 법령 · 수치가 완성형 문장으로 / Papers, statutes, figures that do not exist, in polished sentences | 제목 · 조문 번호로 실재부터 검색 / Search the title or article number first |
| [02](cases/02_citation-failure.md) | 출처 오류 · Citation failure | 주소는 열리는데 그 문장이 거기 없음 / The link opens, but the claim is not on that page | 열어서 찾기(Ctrl+F) · 쪽 확인 / Open and find, check the page |
| [03](cases/03_context-failure.md) | 맥락 오류 · Context failure | 다른 나라 · 지난 시점 · 다른 대상 · 다른 단위 / Wrong country, date, population, or unit | 국가 · 기준일 · 대상 · 단위 / Country · as-of date · population · unit |
| [04](cases/04_number-failure.md) | 수치 오류 · Number failure | 합계 · 비율 합 · 단위 · 기간이 어긋남 / Totals, shares, units, periods do not add up | 다시 계산 · 비율 합 100 · %와 %p / Recompute · shares sum to 100 · % vs %p |
| [05](cases/05_prompt-failure.md) | 지시 실패 · Instruction failure | 빈칸을 그럴듯한 기본값으로 메움 / Blanks filled with plausible defaults | 내가 정한 적 없는 선택 찾기 / Find choices you never made |
| [06](cases/06_completion-claim.md) | 완료 선언 · False completion | "다 됐다"는데 안 됐음 · 확인 못 한 것을 확인했다고 / "Done" when it is not · "verified" when it could not be | 완료 정의와 대조 · 바뀐 줄 · 직접 열기 / Compare with the definition of done · diff · open it |
| [07](cases/07_context-loss.md) | 긴 대화 · Long conversation | 아침 규칙이 오후에 사라짐 · 같은 교정 반복 / Morning rules vanish by afternoon · same correction three times | 규칙이 파일에 있는지 · 새 대화 / Is the rule in a file? · start a new conversation |
| [08](cases/08_visual-ai-failure.md) | 이미지 · 영상 · Image & video | 손 · 글자 · 로고 · 차트 수치가 깨짐 / Hands, text, logos, chart values break | 확대해서 글자 · 손 · 수치 / Zoom in on text, hands, numbers |
| [09](cases/09_security-failure.md) | 보안 실패 · Security failure | 들어온 글이 지시가 되고 넣은 것이 다시 나옴 · 키가 커밋됨 / Pasted text becomes an instruction · inputs come back out · keys get committed | 출력이 요청과 같은 일을 했는가 · 출력에서 키 검색 / Did the output do what you asked? · search the output for secrets |
| [10](cases/10_excessive-agency.md) | 과잉 자율성 · Excessive agency | 삭제 · 범위 밖 수정 · 올리기 · 이력 삭제 · 발송을 승인 없이 / Deletes, edits out of scope, pushes, resets, sends — without approval | 파일 목록 · 원격 이력 · 이력 그래프 / File list · remote history · history graph |

유형과 근거의 대응 · Mapping between types and evidence: [research/02-failure-taxonomy.md](research/02-failure-taxonomy.md)

## 8. 다섯 가지 원칙 · Five principles

1. **매끄러움은 증거가 아닙니다.** 모델은 저장된 사실을 찾아 쓰는 것이 아니라 확률적으로 이어질 말을 고릅니다. 그래서 틀려도 유창합니다. / **Fluent is not evidence.** A model picks what is statistically likely to come next, so it is fluent even when wrong.
2. **"확실해?"는 소용없습니다.** 같은 추측을 한 번 더 시키는 것뿐입니다. 대조할 원문, 근거로 삼을 범위, 결과를 적을 파일을 줍니다. / **"Are you sure?" is useless.** It only asks for the same guess again. Give it the source, the allowed range of evidence, and a file to write to.
3. **검증과 확인은 다릅니다.** 검증은 요구대로 만들었는가(기계에 맡길 수 있음), 확인은 받는 사람의 필요를 채우는가(사람의 일). / **Verification ≠ validation.** Built as specified (a machine can check) vs. meets the reader's need (a human's job).
4. **맡기기 전에 저장점을 만들고, 끝나면 바뀐 줄을 읽습니다.** 받아들일지 되돌릴지는 사람이 정합니다. / **Make a save point before delegating, read the changed lines afterwards.** You decide whether to accept or revert.
5. **확인하지 못한 것은 확인했다고 적지 않습니다.** 〔확인 못 함〕은 정직한 기록입니다. 책임은 검토하고 내보낸 사람에게 있습니다. / **Never write "verified" for what you could not verify.** 〔확인 못 함〕 is an honest record. Responsibility belongs to the person who reviewed and shipped.

## 9. 자주 묻는 질문 · FAQ

- **진짜 AI가 들어 있나요? · Is there a real AI inside?** — **KO** 기본 모드에는 없습니다. 페이지는 절차를 보여 주는 시뮬레이션이고, 도구는 정규식으로 확인할 문장을 뽑을 뿐입니다. 본인 키를 넣으면(선택) 실제 모델이 텍스트 파일을 검토하지만 그 결과도 판정이 아닙니다. / **EN** Not in the default mode. With your own key (optional) a real model reviews text files, but its output is still a list to verify. A human judges.
- **올린 파일은 어디로 가나요? · Where do uploaded files go?** — **KO** 기본 모드에서는 어디로도 가지 않습니다. 실제 모델 모드에서는 본인이 지정한 제공자에게만 갑니다. 도구는 내 컴퓨터에서만 돌고 결과를 `out/`에 씁니다. / **EN** Nowhere in the default mode; only to the provider you configured in real-model mode. The tools run locally and write to `out/`.
- **사례는 실제 사건인가요? · Are the cases real incidents?** — **KO** 아니요. 100건 모두 실제 인물 · 기관 · 고객과 무관한 가상 예시이고, 특정 제품을 겨냥하지 않습니다. / **EN** No. All 100 are synthetic and unrelated to any real person, organization, or customer. No product is targeted.
- **왜 통과 · 미통과를 자동으로 매기지 않나요? · Why no automatic pass/fail?** — **KO** 만든 쪽이 스스로 채점하면 "됐다"로 기우는 것이 이 저장소가 다루는 실패 유형(06)이기 때문입니다. / **EN** Because self-grading drifting toward "done" is itself one of the failure types here (06).
- **수업 · 연구 · 회사에서 써도 되나요? · Can I use it in class, research, or at work?** — **KO** 학습 · 교육 · 연구 · 개인 이용은 출처(ⓒ METACURATION · 저장소 주소)만 적으면 자유롭습니다(CC BY-NC 4.0). **영리 목적 이용(기업 교육 · 유료 강의 · 유료 서비스 · 제품 포함)은 별도 협의** — 이슈로 문의해 주세요. / **EN** Non-commercial use is free with attribution under CC BY-NC 4.0. **Commercial use requires a separate agreement** — open an issue.

## 10. 이 저장소가 하지 않는 것 · What this repository does not do

- 특정 제품 · 개인을 비난하지 않습니다 — 실패 유형은 모든 언어 모델에 공통입니다. / No product or person is targeted — the failure types are common to all language models.
- 실제 자료 · 개인정보 · 기관 내부 자료를 담지 않습니다 — 공개 기준은 [research/00-publication-criteria.md](research/00-publication-criteria.md). / No real data, personal data, or internal documents — see the publication criteria.
- 기본 모드에서는 외부 서버 · 계정 · 설치를 요구하지 않습니다(실제 모델 연결은 선택). / No external server, account, or installation in the default mode (real-model mode is optional).

## 11. 기여하기 · Contributing

**KO** 새 실패 사례는 [templates/failure-case-template.md](templates/failure-case-template.md) 양식으로 cases/에 추가하고, 짧은 사례는 해당 유형 파일의 부록에 `C-101`부터 이어 붙입니다. 증상 · 원인 · 확인 방법 · 예방 규칙 네 칸이 모두 있어야 하고, 예시는 가상이거나 공개 자료여야 합니다. 규칙은 [CONTRIBUTING.md](CONTRIBUTING.md). / **EN** Add new cases with the template; short cases go at the end of the matching appendix, numbered from C-101. All four sections are required, and examples must be synthetic or public. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 12. 라이선스 · 인용 · License · Citation

**ⓒ METACURATION · CC BY-NC 4.0** — **KO** 출처를 표시하면 비영리 목적으로 자유롭게 쓰고 고치고 나눌 수 있습니다. **상업적 이용은 별도 협의**입니다(저장소 이슈로 문의). 공개 표준(OWASP 등)에서는 항목 이름 · 번호 · 링크만 가져오고 설명은 자체 작성했으므로 다른 라이선스가 따라오지 않습니다. 왜 이 라이선스인지는 [license-guide/choose-a-license.md](license-guide/choose-a-license.md) 8절, 전문은 [LICENSE](LICENSE). / **EN** Free for non-commercial use with attribution; **commercial use requires a separate agreement** (open an issue). Public standards are referenced by item name, number, and link only, so no other license attaches. Full text in [LICENSE](LICENSE).

인용 · To cite: [CITATION.cff](CITATION.cff) — GitHub의 "Cite this repository"에서 그대로 복사할 수 있습니다 / shown under "Cite this repository".

## 13. 근거로 삼은 공개 자료 · Sources

**KO** 이 저장소의 분류 · 용어 · 체크리스트는 아래 공개 자료의 **개념과 항목 이름**에 기대고, 설명은 모두 이 저장소의 말로 다시 썼습니다. 재사용 조건 · 확인 방법은 [research/01-source-map.md](research/01-source-map.md), 링크와 확인 로그는 [research/07-references.md](research/07-references.md). / **EN** The taxonomy, glossary, and checklists lean on the concepts and item names of the public sources below; all explanations are written in this repository's own words. Reuse terms and the link-check log are in [research/](research/).

- **AI 위험 · 신뢰성 / AI risk & trustworthiness** — NIST AI RMF 1.0 (2023) · NIST AI 600-1 Generative AI Profile (2024, confabulation) · OWASP Top 10 for LLM Applications 2025 · MIT AI Risk Repository · AI Incident Database · Stanford HAI AI Index · Stanford legal-AI study *Hallucination-Free?*
- **원리 · 운용 / Principles & operation** — Kalai et al. (2025) *Why Language Models Hallucinate* · Anthropic (2024) *Building Effective Agents* · Anthropic (2025) *Effective Context Engineering for AI Agents* · Anthropic (2025) *Effective Harnesses for Long-Running Agents* · Claude Code docs (best practices · memory · permissions · checkpointing)
- **윤리 · 정책 · 공개 / Ethics, policy & disclosure** — OECD AI Principles (2019 · 2024) · UNESCO Recommendation on the Ethics of AI (2021) · EU AI Act Article 50 · C2PA Content Credentials · ICMJE · COPE · Nature Portfolio · ACM authorship policies
- **GitHub** — licensing · .gitignore · secret scanning · push protection · removing sensitive data · CITATION files · commit email privacy · two-factor authentication

확인일 · Verified on 2026-10-10 — 링크 32건 중 30건 정상 응답, 2건(COPE · ACM)은 자동 접근 차단(403)으로 직접 확인 필요 / 32 links opened, 30 responded, 2 blocked automated access. 세부 수치는 원문에서 확인한 것만 옮겼습니다 — 원문을 직접 여는 것이 이 저장소의 원칙입니다 / Only figures confirmed in the originals are quoted — opening the source yourself is this repository's rule.
