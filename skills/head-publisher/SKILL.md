---
name: head-publisher
description: Use when an approved blog draft is ready for final validation and publication to the company website or CMS.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/head-publisher/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/head-publisher/SKILL.md
      usageMode: mirrored
---

# Skills For Head Publisher

This agent is the final publishing reviewer for transcript-to-blog workflows. Its skills should favor:

- finding the latest approved materials quickly
- assembling article copy with assets and placement notes
- catching production blockers before handoff
- packaging the final review clearly for admin

## Core Skills To Use

These existing skills are the best fit for the current agent role.

### `google-drive:google-drive`
Use for locating the latest draft, designer notes, source assets, and related files across Drive.

### `google-drive:google-docs`
Use for reading and editing the working article draft in Google Docs with precision.

### `gmail:gmail`
Use for preparing and sending approval handoffs, summaries, and blocker notes to admin.

### `docx`
Use when the final deliverable needs to be a polished Word document rather than a Google Doc.

### `pdfs`
Use when final review materials arrive as PDFs, or when a PDF export is needed for approval or archive purposes.

## Recommended Skill Stack By Task

### Final Editorial Review
Preferred skills:

- `google-drive:google-drive`
- `google-drive:google-docs`
- `pdfs`

### Production Package Assembly
Preferred skills:

- `google-drive:google-drive`
- `google-drive:google-docs`
- `docx`

### Approval Handoff
Preferred skills:

- `gmail:gmail`
- `google-drive:google-drive`

## New Skills That Would Improve This Agent

These are the highest-value additions for this role.

### `editorial-final-review`
Purpose: Run a consistent publication-readiness pass on a near-final article.

Should cover:

- narrative clarity and flow
- grammar, spelling, and readability
- unresolved placeholders and contradictions
- approval recommendation: ready / ready with notes / blocked
- concise blocker reporting

Why it helps:
This would turn the final review step into a repeatable workflow instead of relying on general editing instincts each time.

### `asset-placement-packager`
Purpose: Merge article copy, supporting assets, captions, and designer placement notes into one production-ready package.

Should cover:

- mapping assets to exact insertion points
- distinguishing confirmed placements from suggested placements
- caption and alt-text checks
- missing-asset detection
- simple publish-ready packaging format

Why it helps:
This is one of the core responsibilities of the Head Publisher role and deserves its own dedicated workflow.

### `approval-handoff-writer`
Purpose: Produce a clean admin-ready approval email or memo with the right level of detail.

Should cover:

- article status summary
- approval recommendation
- reasons for approval or hold
- clear references to the production-ready draft
- risks, dependencies, and missing pieces

Why it helps:
It would standardize the last mile and keep admin handoffs short, consistent, and decisive.

### `source-material-reconciler`
Purpose: Compare multiple draft versions, supporting notes, and asset bundles to identify the latest and most complete package.

Should cover:

- latest-version detection
- duplicate and stale file spotting
- mismatch reporting across copy, assets, and notes
- confidence level on which package should be treated as canonical

Why it helps:
This directly addresses one of the biggest failure modes in publishing workflows: using the wrong version.

### `blog-seo-and-metadata-check`
Purpose: Add a final web-publishing layer beyond editorial correctness.

Should cover:

- title and subhead quality
- excerpt or summary drafting
- slug suggestions
- meta description draft
- heading structure review
- image alt text completeness

Why it helps:
It closes the gap between “good draft” and “ready to publish on a blog.”

### `publishing-blocker-triage`
Purpose: Turn incomplete packages into a clean blocker report with exact next actions.

Should cover:

- missing files
- unclear approvals
- unresolved factual placeholders
- asset gaps
- ownership questions
- recommended next action by stakeholder

Why it helps:
When a package is not ready, the agent should still be able to move the team forward cleanly.

## Suggested Priority Order For Adding New Skills

1. `asset-placement-packager`
2. `editorial-final-review`
3. `approval-handoff-writer`
4. `source-material-reconciler`
5. `blog-seo-and-metadata-check`
6. `publishing-blocker-triage`

## Minimal Operating Guidance

When this agent is invoked, it should generally:

1. find the latest final draft and supporting files
2. verify that assets and placement notes match the draft
3. assemble the production-ready package
4. issue a clear approval recommendation
5. send or draft the admin handoff when requested

## Avoid Using This Agent For

- early-stage ideation
- rough transcript cleanup before editorial drafting
- graphic design creation from scratch
- inventing missing source material or approvals

This agent is strongest at final review, packaging, and handoff readiness.