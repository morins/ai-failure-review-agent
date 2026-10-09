# AI Failure Patterns

> Fluent is not the same as correct. This repository collects **how AI answers fail**, **what a human must check**, and **how to leave a record of that check** — as cases, checklists, a glossary, and guides for publishing your own work on GitHub. No coding required.

[한국어 README](README.ko.md) · License: MIT · Contains no real data (synthetic examples only)

## Why

Ask an AI for a summary or a draft and the result arrives fast. The problem starts afterwards: with no rule for *which sentences to check*, you re-read everything and still miss wrong numbers and citations that do not exist. Asking "are you sure?" does not help — the model picks another plausible answer; it does not open the source.

This repository started from that single pain point. The fix is not a better prompt. It is a **sheet that extracts what to verify**, a **column where a human writes the verdict**, and a **check that stops when the sheet breaks its own rules**. Failure cases are shared assets, not secrets.

## Who it is for

- People who draft reports, assignments, or papers with AI and **own the review**
- People who must **explain to a team or class** how to check AI output
- Non-developers who delegate work to AI agents and have to **judge the result**
- Anyone publishing their **first GitHub repository** without writing code

## What is inside

| Folder | Content | Open it when |
|---|---|---|
| [cases/](cases/) | 10 failure patterns — symptoms, mechanism, how to catch, how to prevent — plus 100 short synthetic cases (C-001 to C-100) | "Why did it get this wrong?" |
| [checklists/](checklists/) | Before trusting an answer · verification vs validation (A–E) · citations · numbers · before delegating · reading the diff | You received output, or are about to delegate |
| [research/](research/) | What may be published · map of authoritative sources with reuse terms · the 10-type taxonomy and its evidence · references with a link-check log | "What is this based on?" · before publishing |
| [ethics/](ethics/) | How much AI use to disclose, and who is responsible | Before submitting anything |
| [glossary/](glossary/) | ~30 terms, each with "the mistake you make if you don't know it" | A manual uses a word you don't know |
| [github-guide/](github-guide/) | What non-developers can publish on GitHub · pre-publish security review | Your first repository |
| [license-guide/](license-guide/) | Why and how to choose a license | Right before you publish |
| [templates/](templates/) | Failure-case form · review-sheet form · AI-use log | Keeping records |
| [tools/](tools/) | Review-sheet generator and shape checker (Python standard library only) | Turning an answer file into a sheet |
| [raw/](raw/) | Two synthetic AI answers with planted errors | Practice |
| [out/](out/) | Their review sheets, verdicts filled in by a human | Seeing the finished shape |

The process files — `01_페인포인트.md` (pain point), `02_기획안.md` (spec), `plan.md`, `기록.md` (log), `CLAUDE.md` (rules for the agent) — record where this repository came from and what counted as "done". The process is published with the result. They are in Korean.

## Quick start (3 minutes)

1. Open [checklists/before-trusting-ai-answer.md](checklists/before-trusting-ai-answer.md).
2. Turn an answer file into a review sheet (Python 3, nothing to install):

```bash
python tools/make_review_sheet.py raw/예시_AI답변_02_통계요약.md
```

3. Open the generated sheet in `out/` and write the **verdict** (통과 pass · 미통과 fail · 〔확인 못 함〕 could not verify) and the **evidence**. The tool never judges.
4. Check that the sheet follows its own rules — a pass or fail without evidence stops the check:

```bash
python tools/check_review_sheet.py raw/예시_AI답변_02_통계요약.md out/검토표_예시02_통계요약.md
```

Sheets, examples, and most prose are in Korean; the structure and the tools work for any language that uses digits and parentheses.

## The eight patterns

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

Each pattern has one essay-style case plus an appendix of short synthetic cases (C-001 to C-100). The mapping between types and evidence is in [research/02-failure-taxonomy.md](research/02-failure-taxonomy.md) (Korean).

## Five principles

1. **Fluent but wrong.** A model does not retrieve knowledge; it picks the most plausible next piece. Smoothness is not evidence.
2. **"Are you sure?" is useless.** Give it the source to compare against, the allowed range of evidence, and a file to write to.
3. **Verification ≠ validation.** Verification: built as specified (can be delegated to a machine). Validation: meets the reader's need (a human's job). Passing one leaves the other.
4. **Commit before delegating, diff after.** Agents edit your files; you need a record of what changed, when, and why — and you decide whether to accept or revert.
5. **Never write "verified" for what you could not verify.** 〔확인 못 함〕 (could not verify) is an honest record, not a failure. Responsibility belongs to the person who reviewed and shipped.

## Contributing

Add new cases to `cases/` using [templates/failure-case-template.md](templates/failure-case-template.md); short cases go at the end of the matching appendix, numbered from C-101. All four sections — symptoms, mechanism, how to catch, how to prevent — are required, and examples must be synthetic or public. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Sources

The taxonomy, glossary, and checklists lean on the concepts and item names of public standards and reports — NIST AI RMF 1.0 and NIST AI 600-1 (confabulation), OWASP Top 10 for LLM Applications 2025, MIT AI Risk Repository, AI Incident Database, Stanford HAI AI Index and the Stanford legal-AI study *Hallucination-Free?*, Kalai et al. (2025) *Why Language Models Hallucinate*, Anthropic's *Building Effective Agents* / *Effective Context Engineering* / *Effective Harnesses for Long-Running Agents*, Claude Code docs, OECD AI Principles, the UNESCO Recommendation on the Ethics of AI, EU AI Act Article 50, C2PA Content Credentials, ICMJE / COPE / Nature Portfolio / ACM authorship policies, and GitHub Docs. All explanations are written in this repository's own words; only names, numbers, and links are taken. Reuse terms and the link-check log (32 links opened on 2026-10-10; 30 responded, 2 blocked automated access) are in [research/](research/).

## License

MIT. If you reuse the documents, a link back to this repository is appreciated. Why MIT: [license-guide/choose-a-license.md](license-guide/choose-a-license.md). To cite, use [CITATION.cff](CITATION.cff) (GitHub shows it under "Cite this repository").
