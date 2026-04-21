---
name: gateway-content-router
description: Use when transcripts or transcript summaries need multi-idea extraction and classification into the blog engine's five content buckets.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/gateway-content-router/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/gateway-content-router/SKILL.md
      usageMode: mirrored
---

# Gateway Content Router

This skill converts transcript material into structured content opportunities.

Use a two-pass workflow:

1. extract article-worthy candidates
2. classify, score, and route each candidate

## Categories

- `evergreen_answer_page`: recurring questions, explanations, or educational clarifications
- `real_time_intel_post`: trends, current events, recent news, or fast-changing market observations
- `location_page`: places, regions, named markets, or company-specific local context
- `submarket_page`: narrow verticals, buyer slices, or niche business segments
- `foundational_entity_page`: durable concepts, entities, frameworks, and core definitions

## Routing rules

- extract every viable idea, not just the dominant one
- allow one idea to belong to multiple categories when justified
- keep each record narrow enough that one article could credibly target it
- include a source excerpt so downstream agents can trace the reasoning
- include classification rationale, route decision, and scoring data
- reject low-signal candidates explicitly
- classify by editorial intent, not keyword matching alone

## Output format

Prefer JSON containing processing summary, accepted ideas, and rejected candidates.

## Do not

- reduce a transcript to one idea when several distinct ideas exist
- drop weak ideas silently
- draft final blog prose
