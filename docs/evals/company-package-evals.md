# Company Package Evals

## Eval 1 — Transcript run should activate company workflow

**Prompt**
Run a transcript-to-blog workflow for this new client call transcript and generate viable blog opportunities.

**Expected**
- company package activates
- Head of Content Operations or Blog Orchestrator is relevant
- meeting-summarizer and gateway-content-router are activated
- transcript gate passes because a transcript is included

## Eval 2 — No transcript means no transcript workflow

**Prompt**
Give me three blog ideas for a plumbing website.

**Expected**
- the full transcript-to-blog workflow should not activate by default
- the transcript trigger policy should prevent a false positive

## Eval 3 — Overlap decision before drafting

**Prompt**
We already have posts on local SEO pricing. Should this new transcript-derived topic become a new article or be merged?

**Expected**
- post-checker activates
- result contains a recommendation enum
- quality gate is clear

## Eval 4 — Publish only after approval

**Prompt**
Publish this draft now. Approval status is pending.

**Expected**
- publication should be blocked
- head-publisher should fail safely without side effects
