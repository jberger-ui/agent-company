---
name: post-checker
description: Use when a proposed article needs duplication checks against existing local content and comparable content on the public web.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/post-checker/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/post-checker/SKILL.md
      usageMode: mirrored
---

# Skills for Post Checker


This file defines the skill set that best fits the `Post Checker` agent.

The goal is to keep the agent strong at three things:
- finding internal overlap
- judging how saturated a topic already is on the public web
- turning that research into concrete editorial guidance

## Recommended Core Skills

These are the skills the agent should have by default because they directly support normal review work.

### Internal Content Similarity Reviewer
**Purpose:** Search local files, uploaded drafts, archives, and agent-accessible materials for posts that overlap in topic, thesis, framing, structure, or examples.

**Use when:**
- the draft may overlap with existing company content
- there are local blog archives, content calendars, PDFs, DOCX files, exports, or notes in the run
- the reviewer needs evidence-based internal duplication findings

**What it should do:**
1. Search local/internal materials first.
2. Identify likely matches by title, angle, structure, repeated claims, or repeated examples.
3. Separate exact duplication from partial overlap and topic adjacency.
4. Report confidence level and quote or summarize only what is supported by available material.
5. Explicitly say when internal coverage is unavailable or incomplete.

**Why this improves the agent:** The current agent brief requires internal similarity review, but a dedicated skill makes that work more systematic and less likely to miss near-duplicate angles.

### Public Coverage Saturation Analyst
**Purpose:** Assess how heavily the topic is already covered on the public web and identify the most common angles, examples, and framing patterns.

**Use when:**
- the draft topic is likely to be widely covered
- the reviewer needs to know whether the draft is adding anything new
- public-web comparison is part of the originality check

**What it should do:**
1. Search the public web after the internal review.
2. Cluster results by common angle, argument, and audience.
3. Identify phrases, examples, and structures that appear repeatedly across coverage.
4. Distinguish “popular topic” from “undifferentiated treatment.”
5. Note whether the draft is stronger, weaker, or merely similar to typical coverage.

**Why this improves the agent:** It turns generic web research into a consistent editorial comparison rather than a loose collection of links.

### Editorial Differentiation Coach
**Purpose:** Convert overlap findings into practical keep/cut/rewrite guidance that sharpens originality and editorial value.

**Use when:**
- the user wants publication guidance, not just overlap detection
- a draft has promising ideas but weak differentiation
- the reviewer should suggest a better angle or structure

**What it should do:**
1. Preserve differentiated sections.
2. Flag generic or saturated sections for removal.
3. Recommend rewrites where the idea is sound but the framing is common.
4. Suggest sharper thesis options, audience shifts, or evidence upgrades.
5. Prefer editorially specific recommendations over vague advice.

**Why this improves the agent:** The current brief already asks for keep/cut/rewrite recommendations; this skill makes that part sharper and more actionable.

## Useful Supporting Skills

These are not needed for every review, but they make the agent more capable in common real-world cases.

### SEO Cannibalization Checker
**Purpose:** Detect when a new post risks competing with an existing company post for the same search intent instead of adding a distinct editorial angle.

**Use when:**
- the company publishes search-driven content
- two drafts target very similar keywords or reader questions
- the user cares about topic cannibalization

**What it should do:**
- compare likely primary search intent across internal posts
- flag drafts that should be merged, repositioned, or retitled
- recommend a cleaner differentiation strategy

### Evidence and Specificity Upgrader
**Purpose:** Identify where a draft relies on generic statements and suggest where stronger examples, internal data, contrarian framing, or concrete audience detail would make it meaningfully better.

**Use when:**
- the draft feels correct but ordinary
- the user wants a stronger point of view
- the review should go beyond overlap and improve publishability

**What it should do:**
- mark generic claims that need proof or specificity
- suggest examples, case studies, metrics, or sharper framing
- distinguish “fine but bland” from “actually differentiated”

### Document Intake for Draft Review
**Purpose:** Reliably read and normalize draft inputs from DOCX, PDF, spreadsheets, and pasted text before review.

**Use when:**
- the draft or archive is provided in file form
- the review depends on attachments rather than pasted text

**What it should do:**
- extract text cleanly from common file types
- preserve headings and section structure where possible
- surface extraction limits clearly when formatting or OCR quality is poor

**Implementation note:** This skill can lean on existing `docx` and `pdfs` capabilities rather than replacing them.

## Existing Built-In Skills Worth Keeping

These already exist and are useful for this agent:

### docx
Keep this for reviewing uploaded Word drafts or internal editorial docs.

### pdfs
Keep this for reviewing PDFs, exported blog archives, content briefs, or scanned internal materials.

## Skills That Are Not Core for This Agent

These do not need to be part of the default skill stack unless the agent’s role expands:
- `PowerPoint`
- `Excel` except when content inventories are stored in spreadsheets
- `frontend-skill`
- `openai-docs`
- `skill-installer`
- `skill-creator`

## Suggested Final Skill Stack

If you want a compact, high-value setup, use this set:
1. `Internal Content Similarity Reviewer`
2. `Public Coverage Saturation Analyst`
3. `Editorial Differentiation Coach`
4. `SEO Cannibalization Checker`
5. `Evidence and Specificity Upgrader`
6. `Document Intake for Draft Review`
7. `docx`
8. `pdfs`

## Notes for Future Expansion

If this agent later starts reviewing full content programs instead of single drafts, the next skills to add would be:
- a `Content Portfolio Gap Finder`
- a `Series and Cluster Planner`
- a `Voice and Style Consistency Reviewer`