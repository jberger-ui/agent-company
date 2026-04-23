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

# Skills for Gateway Content Router

This file defines the skills that best support the `Gateway Content Router` agent.
The goal is to help the agent turn meeting summaries, transcripts, and notes into
an exhaustive but disciplined set of blog post opportunities with clear routing decisions.

## Design Principles

- Favor skills that improve extraction accuracy, evidence discipline, and routing consistency.
- Keep skills narrow enough to trigger cleanly.
- Prefer workflow support over generic writing help.
- Add output-format skills only when they improve delivery or downstream usability.

## Recommended Core Skills

These are the most useful skills for this agent to have available.

### 1. Content Opportunity Extraction

**Why this matters**
This is the core job of the agent. It should help split broad discussion themes into
multiple article-sized opportunities, avoid duplicates, and reject weak candidates.

**What it should do**
- Scan meeting notes for all distinct article opportunities, not just the loudest theme
- Separate broad themes into narrower, standalone article candidates
- Detect near-duplicates and merge only when the angle is truly the same
- Flag unsupported or low-signal ideas for rejection
- Preserve excerpt-level traceability back to source material

**Trigger when**
- The user provides meeting notes, transcript excerpts, summaries, recaps, call notes, or brainstorm notes
- The user asks for blog ideas, content opportunities, article angles, or extraction of publishable topics

### 2. Content Route Classification

**Why this matters**
This agent must classify each viable opportunity into exactly one primary category.
That routing step is specialized enough to deserve its own skill.

**What it should do**
- Route each candidate into one of:
  - `evergreen_answer_page`
  - `real_time_intel_post`
  - `location_page`
  - `submarket_page`
  - `foundational_entity_page`
- Enforce exactly one primary category
- Use runner-up categories only when ambiguity is real
- Explain why the chosen route fits better than plausible alternatives

**Trigger when**
- The user asks for routing, classification, page type assignment, or category decisions
- The source material contains multiple candidate article directions that need sorting

### 3. Evidence-Based Scoring

**Why this matters**
The agent is expected to score and justify each opportunity. A dedicated skill keeps
the scoring rubric consistent and grounded in source evidence rather than intuition.

**What it should do**
- Score:
  - signal strength
  - specificity
  - content viability
  - distinctiveness
  - evidence support
- Produce an overall score and route decision:
  - `accept`
  - `accept_with_caution`
  - `reject`
- Keep rationale concise and tied to the supplied source

**Trigger when**
- The user wants prioritization, confidence scoring, acceptance decisions, or triage

### 4. Rejected Candidate Handling

**Why this matters**
This agent should not pad outputs with weak ideas. A rejection-focused skill helps it
be explicit about what failed and why.

**What it should do**
- Surface rejected candidates alongside accepted ones
- Explain whether a candidate failed due to:
  - weak evidence
  - overlap with a stronger candidate
  - overly broad framing
  - being operational rather than editorial
  - lack of standalone article viability
- Preserve a source excerpt for each rejected idea

**Trigger when**
- The user asks for a complete routing set
- The source material contains partial or weak content signals

### 5. Structured Output Packaging

**Why this matters**
The agent’s output has a strict schema. A formatting skill reduces drift and makes
handoff to downstream content teams easier.

**What it should do**
- Return results in two sections only:
  - `Viable Opportunities`
  - `Rejected Candidates`
- Ensure every accepted record includes:
  - `opportunity_label`
  - `primary_category`
  - `runner_up_category`
  - `route_decision`
  - `overall_score`
  - `score_breakdown`
  - `why_this_is_viable`
  - `classification_rationale`
  - `source_excerpt`
  - `article_angle`
  - `notes_for_downstream_agents`
- Ensure every rejected record includes:
  - `candidate_label`
  - `rejection_reason`
  - `source_excerpt`
  - `why_it_failed`

**Trigger when**
- The user asks for final routing output, structured records, or downstream-ready deliverables

## Useful Existing Skills To Keep Available

These do not replace the routing-specific skills above, but they are helpful support skills.

### `docx`
Use when the user wants the routing output turned into a polished stakeholder-facing document.

### `Excel`
Use when the user wants the opportunities exported as a sortable spreadsheet, scoring matrix, or content pipeline tracker.

### `pdfs`
Use when the source material arrives as PDFs or when the final deliverable must be a PDF.

## Additional Skills I Would Add

These would materially improve this agent.

### A. Transcript Normalizer

**Purpose**
Convert messy transcripts, meeting notes, and pasted recaps into a cleaner source before extraction.

**Why add it**
Meeting inputs are often noisy. This would help the router distinguish content ideas from filler, side remarks, and operational chatter.

**What it should do**
- Remove obvious transcript noise
- Separate speaker context from usable content claims
- Collapse repeated points
- Mark uncertain or ambiguous passages
- Preserve quote-worthy excerpts

### B. Opportunity Deduper

**Purpose**
Detect when multiple candidate ideas are just different phrasings of the same article.

**Why add it**
This agent needs to be exhaustive without inflating the count. A dedupe skill helps maintain that balance.

**What it should do**
- Cluster overlapping candidate ideas
- Distinguish true duplicates from adjacent but separately publishable angles
- Suggest the strongest surviving label for each cluster

### C. SEO Framing Assistant

**Purpose**
Turn a valid opportunity into a sharper, more searchable article angle without changing the underlying claim.

**Why add it**
The router should not only identify viable ideas, but also hand them off in a form that editorial and SEO teams can act on quickly.

**What it should do**
- Reframe opportunity labels into likely search-oriented article angles
- Preserve fidelity to the source material
- Avoid inventing unsupported demand or keywords
- Suggest likely question-led framing when appropriate

### D. Editorial Risk Check

**Purpose**
Spot cases where an idea sounds interesting but is too thin, too speculative, too timely, or too weakly evidenced to route confidently.

**Why add it**
This helps the agent stay disciplined when the meeting contains half-formed claims.

**What it should do**
- Flag unsupported assertions
- Detect weak market claims
- Catch ideas that are too broad for one article
- Mark borderline candidates as `accept_with_caution` rather than overcommitting

## Suggested Trigger Order

When multiple skills apply, this order will usually work best:

1. `Transcript Normalizer`
2. `Content Opportunity Extraction`
3. `Opportunity Deduper`
4. `Evidence-Based Scoring`
5. `Content Route Classification`
6. `Editorial Risk Check`
7. `Structured Output Packaging`
8. `Excel` or `docx` only if the user wants a file deliverable

## Minimal Skill Set

If you want the leanest strong version of this agent, keep these five:

1. Content Opportunity Extraction
2. Content Route Classification
3. Evidence-Based Scoring
4. Rejected Candidate Handling
5. Structured Output Packaging

## Best Next Additions

If you want to improve the agent beyond the minimum, add these three first:

1. Transcript Normalizer
2. Opportunity Deduper
3. Editorial Risk Check