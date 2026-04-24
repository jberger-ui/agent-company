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

# Skills for Blog Draft Writer

This file defines the most useful skills for the `Blog Draft Writer` agent and recommends a small set of additional skills that would improve draft quality, consistency, and editorial usefulness.

## Core Principle

This agent should stay focused on turning an approved opportunity plus persona input into a strong first draft. Skills should help with:

- grounding the draft in source material
- matching the draft to the intended persona
- keeping structure clear and revision-friendly
- packaging substantial outputs cleanly when a file is needed

Skills should not pull the agent toward broad research, generic SEO filler, or heavy publishing workflow overhead unless the user explicitly asks for that.

## Use These Existing Skills

### `docx`
Use when the user wants the draft delivered as a polished editable document, with headings and formatting ready for editorial review.

Why it helps:
- blog drafts are often reviewed in document form
- supports clean handoff to editors or clients
- useful for longer posts, revision rounds, and redlines

### `pdfs`
Use when the user wants a shareable review artifact or needs a PDF export of a draft or content packet.

Why it helps:
- good for stakeholder review
- useful when a static version is preferred

### `openai-docs`
Use only when the blog post is specifically about OpenAI products, APIs, models, or platform behavior and the draft needs current official documentation.

Why it helps:
- keeps claims current and source-grounded
- avoids relying on stale product knowledge

Do not use it for general blog drafting unless the topic is genuinely OpenAI-specific.

## Recommended New Skills

These are the highest-value additions for this agent.

### `source-grounded-blogging`
Use when the user provides transcripts, interview notes, reports, article excerpts, or opportunity packets with embedded source evidence.

What it should do:
- extract the central claim and supporting points from provided materials
- distinguish direct evidence from inference
- preserve the original scope of the opportunity
- flag thinly supported sections before drafting
- help the agent avoid inventing facts or overclaiming

Why this matters:
- this agent’s biggest quality risk is drifting beyond the supplied signal
- a source-grounding skill would directly improve accuracy and trustworthiness

### `persona-adaptation`
Use when the persona package is detailed or when the user asks for multiple versions for different audiences.

What it should do:
- convert persona details into writing decisions
- tune terminology, pacing, examples, and objection-handling
- preserve the article’s thesis while changing framing for the reader
- provide lightweight checks for “too advanced,” “too basic,” or “too generic”

Why this matters:
- persona shaping is central to this agent’s job
- this would make voice and relevance more consistent across drafts

### `blog-structure-and-flow`
Use when the input is solid but the draft needs strong organization, better transitions, or a more publishable shape.

What it should do:
- choose the right article structure based on category
- sharpen titles, intros, section sequencing, and conclusions
- avoid repetitive section patterns
- improve readability without turning the post into formulaic SEO copy

Why this matters:
- many blog drafts fail on structure before they fail on ideas
- this skill would raise baseline editorial quality quickly

### `editorial-qa`
Use after drafting when the user wants a tighter final draft, a self-review, or a revision pass.

What it should do:
- check for unsupported claims
- catch scope drift from the approved angle
- detect repetition, filler, weak transitions, and vague conclusions
- verify that the post answers the implied reader question
- produce a short revision checklist or apply the fixes directly

Why this matters:
- gives the agent a reliable cleanup pass
- especially useful before exporting to a document

### `seo-without-slop`
Use when the user wants search-aware blog writing but still wants the post to feel expert, specific, and human.

What it should do:
- map the primary search intent from the opportunity
- identify natural subtopics and likely reader questions
- improve headline clarity and section labeling
- avoid keyword stuffing and generic “ultimate guide” language
- preserve the article angle instead of flattening it into a generic SEO post

Why this matters:
- some blog opportunities will have search intent baked in
- this skill helps the agent serve that intent without lowering quality

## Nice-to-Have Skills

These are useful, but not as essential as the recommended set above.

### `content-repurposing`
For turning a draft into variants such as LinkedIn posts, newsletter blurbs, executive summaries, or short social copy.

### `internal-linking-and-cta`
For teams that want blog drafts to include suggested internal links, soft calls to action, or conversion-aware endings.

### `house-style-enforcer`
For organizations with a clear editorial style guide, banned phrases list, or brand voice rules.

## Suggested Trigger Rules

Use the skills with light touch:

- Draft from source-heavy material: `source-grounded-blogging`
- Draft for a specific audience: `persona-adaptation`
- Improve article organization: `blog-structure-and-flow`
- Run a cleanup pass: `editorial-qa`
- Write for search intent without losing quality: `seo-without-slop`
- Deliver as a polished file: `docx` or `pdfs`
- OpenAI-specific topic needing current accuracy: `openai-docs`

## Minimal Skill Stack

If you only add a few new skills, start with these three:

1. `source-grounded-blogging`
2. `persona-adaptation`
3. `editorial-qa`

That set would improve accuracy, audience fit, and final polish without making the agent overly complex.