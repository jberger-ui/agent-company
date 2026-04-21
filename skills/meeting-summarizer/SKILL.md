---
name: meeting-summarizer
description: Use when a meeting transcript, call transcript, or notes need to be converted into a production-style structured summary before routing or drafting.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/meeting-summarizer/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/meeting-summarizer/SKILL.md
      usageMode: mirrored
---

# Meeting Summarizer

Turn noisy transcripts into structured meeting intelligence.

Use a segmented workflow:

1. summarize each transcript segment
2. reconcile the segment summaries into one final summary

## Focus

- extract durable topics, decisions, questions, action items, blockers, and examples
- remove filler, tangents, and operational chatter
- preserve evidence for important items
- separate explicit facts from inferred insights
- flag statements that sound speculative or require validation
- capture customer language and content signals useful for downstream content systems

## Required output

Return:

- `executive_summary`
- `discussion_topics`
- `decisions`
- `open_questions`
- `action_items`
- `risks_and_blockers`
- `customer_language`
- `explicit_facts`
- `inferred_insights`
- `content_signals`
- `evidence_snippets`
- `claims_to_verify`

## Do not

- route ideas into content buckets unless explicitly requested
- tailor for persona
- draft full articles
