# Authority Engine Agent Company

A production-ready **Agent Companies** package for an AEO and SEO optimization business that turns transcripts, calls, briefs, and market signals into publishable blog content for client websites.

This repository is designed to be:

- portable across Agent Companies-compatible runtimes
- grounded in a real transcript-to-blog operating model
- ready to extend with projects, tasks, references, schemas, and automations
- compatible with existing specialist role and skill packages already authored in `jberger-ui/Project-1`

## What this package models

This package models two layers of the business:

1. **The company operating layer**
   - leadership and approvals
   - strategy and growth planning
   - content operations
   - editorial quality and publication governance
   - platform and automation enablement

2. **The specialist workflow layer**
   - summarize transcript material
   - route content ideas
   - shape content by persona
   - check overlap and differentiation
   - draft posts
   - manage approvals and publishing
   - orchestrate the end-to-end run

## Provisional team structure

Because the exact org chart has not been finalized yet, this repo uses a practical default structure that you can edit later:

- CEO
- Head of Strategy & Growth
- Head of Content Operations
- Editorial QA Lead
- Platform Automation Lead

In addition, the repo vendors the existing specialist workflow roles from `Project-1` as operational agents.

## Canonical package layout

```text
COMPANY.md
teams/
agents/
projects/
tasks/
skills/
references/
docs/evals/
.github/workflows/
scripts/
```

## Included example work

### Example projects

- `content-engine-hardening` — operational hardening of the transcript-to-blog engine
- `programmatic-authority-expansion` — scaling topic coverage across client sites and entities
- `answer-engine-footprint` — increasing answer-engine visibility and citation readiness

### Example tasks

- `transcript-to-blog-run`
- `weekly-editorial-council`
- `monthly-serp-intelligence-review`
- `qa-release-gate`
- `site-publishing-readiness`

## Source provenance

The workflow-specialist roles and skills in this repo are adapted from the public source repository below and carry provenance metadata inside each vendored file:

- `https://github.com/jberger-ui/Project-1/tree/main/.agents/roles`
- `https://github.com/jberger-ui/Project-1/tree/main/.agents/skills`

## Recommended next edits

1. Replace the provisional company name if needed.
2. Adjust the team and reporting structure.
3. Add your real CMS, publishing, and approval adapters.
4. Add client-specific schemas and references.
5. Add real evaluation prompts under `docs/evals/`.

## Suggested GitHub setup

- create a new GitHub repository
- copy this directory into the repo root
- commit and push
- wire any CI or linting you want
- add internal references and schemas as they become stable

## License

MIT
