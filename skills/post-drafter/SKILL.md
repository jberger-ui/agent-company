---
name: post-drafter
description: Use when routed ideas, persona guidance, and overlap checks are ready to be turned into a first blog draft for approval.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/post-drafter/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/post-drafter/SKILL.md
      usageMode: mirrored
---

# Post Drafter

This skill creates a strong preliminary article.

## Inputs

- routed content category and title seed
- summary or source transcript evidence
- persona guidance
- duplication and differentiation guidance

## Drafting guidance

- open with the reader's real problem or question
- keep the structure aligned with the content category
- preserve factual discipline from source material
- use the persona guidance to choose tone, depth, and emphasis
- use overlap guidance to narrow the angle and avoid redundancy
- include unresolved questions or approval notes separately from the body
- return deterministic draft metadata and approval artifacts when the workflow requests them

## Approval step

When the workflow supports it, prepare the draft so it can enter a Paperclip or GitHub approval path.

## Do not

- publish the post
- hide major assumptions
