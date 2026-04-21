---
name: blog-orchestrator
description: Use when a transcript-to-blog workflow needs end-to-end coordination across summarization, routing, persona shaping, duplication checks, drafting, approval, and publishing.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/blog-orchestrator/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/blog-orchestrator/SKILL.md
      usageMode: mirrored
---

# Blog Orchestrator

This skill coordinates the whole content engine.

## Default workflow

1. call the summarizer on raw transcript material
2. call the router to perform multi-idea extraction
3. decide which ideas are worth pursuing
4. call persona shaping on each viable idea
5. call duplication checks before drafting
6. call the drafter for ideas that still justify a new post
7. publish only after approval exists

## Orchestration rules

- do a short design pass before execution so each stage has a clear input and output
- parallelize independent idea-level work
- keep structured outputs attached to each idea
- write deterministic artifacts into `work/<run_id>/` and mirrored review or publish surfaces
- keep `state/runs.json`, `state/slug-index.json`, `state/topic-index.json`, and `state/published-posts.json` accurate
- block publishing without approval
- return a concise status board with completed steps, open risks, and next actions

## Do not

- skip the duplication step for convenience
- let one large transcript collapse into one generic post by default
