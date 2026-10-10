# ai-failure-review-agent — a failure-type-based review agent for AI output

> Before you trust what an AI wrote, drew, or tabulated: this project names **the ten ways AI output goes wrong**, pulls out **exactly which sentences you must check**, and shows the checking process as a **five-gate review loop**. No coding needed. Nothing you upload leaves your computer.

[한국어 README](README.ko.md) · License: CC BY-NC 4.0 (commercial use by separate agreement) · © METACURATION · No real data (all examples are synthetic) · No external servers in the default mode

## What this project does

1. **A casebook of failure types** — ten ways AI answers fail, each with symptoms, mechanism, a checking order, and prevention rules, plus 100 short synthetic cases (C-001 to C-100) as appendices. → [cases/](cases/)
2. **Checklists and tools** — six checklists for the moment you receive output, before you delegate, and after the agent is done; and two small Python tools (standard library only) that turn an AI answer into a **review sheet** and check that the sheet follows its own rules. → [checklists/](checklists/) · [tools/](tools/)
3. **A review-agent page** — open [failure-peer-review-agent.html](failure-peer-review-agent.html) in a browser, drop a file, and watch the five gates (upload → review → detect → repair → pass) and the ten types light up; export the result as a review sheet (.md) or JSON. Demo by default; **enter your own API key (optional) and a real model reviews your text files**.

In one line: **"Even when the AI says it's done, the pass verdict belongs to a human"** — made into something you can actually practice.

## Who it is for

| You | Start here |
|---|---|
| Draft reports, assignments, or papers with AI and own the review | [Before trusting an answer](checklists/before-trusting-ai-answer.md) → generate a review sheet with the tools |
| Must explain to a team or class how to check AI output | Show the demo page, hand out the type table in [cases/](cases/) |
| Delegate work to AI agents and judge the result | [Before delegating](checklists/delegation-check.md) → [Reading the diff afterwards](checklists/diff-review-check.md) |
| Publish your first repository without writing code | [GitHub guide](github-guide/github-for-non-developers.md) → [Choosing a license](license-guide/choose-a-license.md) → [What may be published](research/00-publication-criteria.md) |

## 30-second tour — the demo page

1. Download or clone the repository (green **Code** button → Download ZIP).
2. Double-click `failure-peer-review-agent.html`. No server, install, or login.
3. Drop any file and press **검토 시작** (Start review). The five stages light up in turn; detected issues show in red, repair candidates in blue.
4. Press **검토표 내보내기 (.md)** to download a review sheet whose verdict column is empty — you fill it in.

To be clear: the default mode is a **simulation**. It does not call an AI model and does not read file contents (only names and sizes). The page makes zero external requests.

**Optional real-model mode** — open the "실제 모델 연결(선택)" panel, pick a provider (OpenAI-compatible or Anthropic), and enter an endpoint, a model name, and your own API key. Text files (.txt · .md · .csv · .json, first 60,000 characters) are then sent from your browser **directly to the provider you chose** and come back as a list of "points to verify" by the ten types. There is no server behind this page, so nothing reaches the repository owner. Do not upload personal or internal data. What the model returns is still a list to verify, not a verdict — the pass/fail column stays yours.

## 3-minute practice — build a review sheet

Python 3 only, nothing to install.

```bash
python tools/make_review_sheet.py raw/예시_AI답변_02_통계요약.md
```

Open the generated sheet in `out/`, write the **verdict** (통과 pass · 미통과 fail · 〔확인 못 함〕 could not verify) and the **evidence**. Then check that the sheet follows its own rules — a pass or fail without evidence stops the check:

```bash
python tools/check_review_sheet.py raw/예시_AI답변_02_통계요약.md out/검토표_예시02_통계요약.md
```

Sheets, examples, and most prose are in Korean; the structure and tools work for any language that uses digits and parentheses.

## What is inside

| File / folder | Content | Open it when |
|---|---|---|
| [failure-peer-review-agent.html](failure-peer-review-agent.html) | Review-agent page — five gates, ten types, export, optional real-model review with your own key | First look · explaining to others · a quick pass over a text draft |
| [cases/](cases/) | Ten failure patterns + 100 short synthetic cases | "Why did it get this wrong?" |
| [checklists/](checklists/) | Before trusting · verification vs validation (A–E) · citations · numbers · before delegating · reading the diff | You received output, or are about to delegate |
| [tools/](tools/) | Review-sheet generator and shape checker | Turning an answer file into a sheet |
| [raw/](raw/) · [out/](out/) | Two synthetic answers with planted errors and their sheets | Practice · the finished shape |
| [ethics/](ethics/) | How much AI use to disclose, who is responsible, how publishers differ | Before submitting anything |
| [glossary/](glossary/) | ~40 terms, each with "the mistake you make if you don't know it" | A manual uses a word you don't know |
| [github-guide/](github-guide/) · [license-guide/](license-guide/) | Publishing on GitHub without code · pre-publish security review · choosing a license | Your first repository |
| [research/](research/) | What may be published · source map with reuse terms and verification results · taxonomy · references with a link-check log | "What is this based on?" |
| [templates/](templates/) | Failure-case form · review-sheet form · AI-use log | Keeping records |
| `01_페인포인트.md` · `02_기획안.md` · `plan.md` · `기록.md` · `CLAUDE.md` | Process records (pain point, spec, plan, log) and the rules file for agents — in Korean | Building something the same way |

## The ten patterns

| # | Pattern | What you see | Fastest check |
|---|---|---|---|
| [01](cases/01_hallucination.md) | Hallucination | Papers, statutes, figures that do not exist, in polished sentences | Search the title / article number first |
| [02](cases/02_citation-failure.md) | Citation failure | The link opens, but the claim is not on that page | Open and find (Ctrl+F), check the page number |
| [03](cases/03_context-failure.md) | Context failure | Wrong country, outdated date, wrong population, wrong unit | Country · as-of date · population · unit |
| [04](cases/04_number-failure.md) | Number failure | Totals, shares, units, periods do not add up | Recompute · shares sum to 100 · % vs %p |
| [05](cases/05_prompt-failure.md) | Instruction failure | Blanks filled with plausible defaults | Find choices you never made |
| [06](cases/06_completion-claim.md) | False completion | "Done" when it is not · "verified" when it could not be | Compare with the definition of done · diff · open it |
| [07](cases/07_context-loss.md) | Long conversation | Morning rules vanish by afternoon · same correction three times | Is the rule in a file? · start a new conversation |
| [08](cases/08_visual-ai-failure.md) | Image & video | Hands, text, logos, chart values break | Zoom in on text, hands, numbers |
| [09](cases/09_security-failure.md) | Security failure | Pasted text becomes an instruction · what you put in comes back out · keys get committed | Did the output do what you asked? · search the output for secrets |
| [10](cases/10_excessive-agency.md) | Excessive agency | Deletes, edits out of scope, pushes, resets, sends — without approval | File list · remote history · history graph |

Each pattern has one essay-style case plus an appendix of short synthetic cases. The mapping between types and evidence is in [research/02-failure-taxonomy.md](research/02-failure-taxonomy.md) (Korean).

## Five principles

1. **Fluent is not evidence.** A model does not look up stored facts; it picks what is statistically likely to come next. So it is fluent even when wrong.
2. **"Are you sure?" is useless.** It only asks for the same guess again. Give it the source to compare against, the allowed range of evidence, and a file to write to.
3. **Verification ≠ validation.** Verification: built as specified (can be delegated to a machine). Validation: meets the reader's need (a human's job). Passing one leaves the other.
4. **Make a save point before delegating, read the changed lines afterwards.** Agents edit your files; you need a record of what changed, when, and why — and you decide whether to accept or revert.
5. **Never write "verified" for what you could not verify.** 〔확인 못 함〕 (could not verify) is an honest record, not a failure. Responsibility belongs to the person who reviewed and shipped.

## FAQ

- **Is there a real AI inside?** Not in the default mode. The page simulates the procedure; the tools use regular expressions to extract what to check. With your own API key (optional) a real model reviews text files — but its output is still a list of points to verify, not a verdict. A human judges.
- **Where do uploaded files go?** In the default mode, nowhere: no external requests (no scripts, fonts, or analytics) and file contents are never read. In real-model mode, only to the API provider you configured. The tools run locally and write to `out/`.
- **Are the cases real incidents?** No. All 100 are synthetic and unrelated to any real person, organization, or customer. No product is targeted.
- **Why no automatic pass/fail?** Because self-grading drifting toward "done" is itself one of the failure types here (06). The tools only extract what to check and verify the sheet's shape.
- **Can I use it in class, research, or at work?** Non-commercial use is free with attribution (© METACURATION, link to this repository) under CC BY-NC 4.0. **Commercial use (corporate training, paid courses, paid services, products) requires a separate agreement** — open an issue.

## Contributing

Add new cases to `cases/` using [templates/failure-case-template.md](templates/failure-case-template.md); short cases go at the end of the matching appendix, numbered from C-101. All four sections — symptoms, mechanism, how to catch, how to prevent — are required, and examples must be synthetic or public. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Sources

The taxonomy, glossary, and checklists lean on the concepts and item names of public standards and reports — NIST AI RMF 1.0 and NIST AI 600-1 (confabulation), OWASP Top 10 for LLM Applications 2025, MIT AI Risk Repository, AI Incident Database, Stanford HAI AI Index and the Stanford legal-AI study *Hallucination-Free?*, Kalai et al. (2025) *Why Language Models Hallucinate*, Anthropic's *Building Effective Agents* / *Effective Context Engineering* / *Effective Harnesses for Long-Running Agents*, Claude Code docs, OECD AI Principles, the UNESCO Recommendation on the Ethics of AI, EU AI Act Article 50, C2PA Content Credentials, ICMJE / COPE / Nature Portfolio / ACM authorship policies, and GitHub Docs. All explanations are written in this repository's own words; only names, numbers, and links are taken. Reuse terms and the link-check log (32 links opened on 2026-10-10; 30 responded, 2 blocked automated access) are in [research/](research/).

## License · Citation

**© METACURATION · CC BY-NC 4.0.** Free for non-commercial use with attribution; **commercial use requires a separate agreement** (open an issue). Public standards (OWASP etc.) are referenced by item name, number, and link only, so no other license attaches. Why this license: [license-guide/choose-a-license.md](license-guide/choose-a-license.md) §8; full text in [LICENSE](LICENSE). To cite, use [CITATION.cff](CITATION.cff) (GitHub shows it under "Cite this repository").
