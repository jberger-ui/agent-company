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

# Meeting Transcript Summarizer

Use this skill when the user provides a meeting transcript, rough notes, chat log, or discussion record and wants a clear, faithful summary.

## What To Produce

Turn messy conversation into a concise, professional recap that captures:

- the main topics discussed
- confirmed decisions
- action items and owners when explicitly stated
- deadlines only when explicitly stated
- open questions, risks, blockers, or unresolved tradeoffs

## Core Workflow

1. Read the full transcript or notes before drafting.
2. Identify the main themes and group related discussion together.
3. Separate clearly:
   - what was decided
   - what was proposed
   - what remains uncertain
4. Extract action items, keeping owner and deadline only when the source states them.
5. Rewrite spoken or fragmented language into clean prose without changing meaning.
6. Compress repetition and side chatter unless it changes the outcome of the meeting.

## Default Output Format

Unless the user asks for another format, respond with:

### Meeting Summary

A concise but detailed overview of the meeting's purpose and what was covered.

### Key Discussion Points

- Main topics, grouped by theme when helpful

### Decisions Made

- Confirmed decisions
- If there were no clear decisions, say so directly

### Action Items

- Next steps
- Include owner and deadline only when explicitly stated

### Open Questions or Risks

- Unresolved issues
- Risks, blockers, dependencies, or follow-ups

## Adaptation Rules

- If the user asks for a shorter version, compress aggressively but keep decisions and action items.
- If the user asks for an email recap, executive summary, or bullet-only notes, keep the same factual content but change the format.
- If the transcript is noisy or incomplete, provide the best possible summary and briefly note important gaps or ambiguities.

## Accuracy Rules

- Do not invent decisions, commitments, owners, or dates.
- Do not present guesses as facts.
- Preserve speaker attribution when it materially helps clarity.
- Keep uncertainty explicit when the source is ambiguous.
- Include sensitive details only when they are clearly relevant to the requested summary.