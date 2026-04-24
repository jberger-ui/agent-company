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
**This skill coordinates the whole content engine. The #1 role of the orchestrator is to delegate tasks to other agents. The orchestrator should not do the work itself, but should instead be responsible for making sure the workflow is followed, handoffs are clean, and approvals are obtained.**

## Required workflow
When you receive a task to convert a transcript into a blog you need to follow these steps

1. Send it to the meeting summarizer
2. Receive it back from the meeting summarizer in summary form
3. Send summary in parallel to the gateway content router to extract blog oppurtunities, and the persona shaper
4. Send it to the post drafter once you received both results from gateway router and persona shaper
5. When you receive the first draft wait for approval from admin before moving to next steps
6. Once you receive approval, send it to the post checker for overlap
7. If Post Checker gives approval to proceed, send the draft to Editorial QA Lead for final review. Include the notes from the post checker.
8. Send final draft to the graphic designer for formatting, image selection, and placement
9. Send the final draft with content from the graphics designer to the head publisher for final formatting and approval.
10. Request final approve from human admin before publication.
11. Publish to website


## Orchestration rules

- do a short design pass before execution so each stage has a clear input and output
- parallelize independent idea-level work
- keep structured outputs attached to each idea
- write deterministic artifacts into `work/<run_id>/` and mirrored review or publish surfaces
- keep `state/runs.json`, `state/slug-index.json`, `state/topic-index.json`, and `state/published-posts.json` accurate
- block publishing without approval
- return a concise status board with completed steps, open risks, and next actions


# Skills For Blog Orchestrator

This file defines the skill set that best fits the `Blog Orchestrator` agent described in `AGENTS.md`.

The goal of this agent is not to do all writing itself. Its main job is to keep the transcript-to-blog workflow in the correct order, package handoffs cleanly, enforce approval gates, and maintain durable project state.

## Design Principles

- Optimize for process control over content generation.
- Treat every stage output as an artifact that must be present before advancing.
- Keep approvals explicit and blocking.
- Prefer short, operational handoffs over long prose.
- Preserve project memory across runs so the workflow can resume cleanly.

## Core Workflow Skills

These are the primary skills the orchestrator should rely on or delegate to.

### 1. Meeting Summarizer

- Purpose: Turn raw meeting transcripts into structured summaries suitable for downstream blog development.
- Trigger: A new transcript arrives and no summary exists yet.
- Inputs:
  - transcript or transcript file
  - project identifier or title if available
  - any constraints from the user
- Expected output:
  - concise summary
  - major themes
  - notable quotes or insights
  - open questions or unclear portions
- Orchestrator rule: Do not move to content routing or persona shaping until this output is present.

### 2. Gateway Content Router

- Purpose: Identify blog-worthy angles, topics, and opportunity areas from the meeting summary.
- Trigger: A valid summary is available.
- Inputs:
  - meeting summary
  - target audience or blog context if known
- Expected output:
  - candidate blog angles
  - recommended topic direction
  - key supporting points
  - any reasons a topic may be weak or redundant
- Orchestrator rule: This runs in parallel with Persona Shaper and both outputs are required before drafting.

### 3. Persona Shaper

- Purpose: Define voice, audience fit, and communication style for the eventual post.
- Trigger: A valid summary is available.
- Inputs:
  - meeting summary
  - known audience, brand, or tone guidance
- Expected output:
  - audience profile
  - tone guidance
  - messaging priorities
  - phrasing cautions
- Orchestrator rule: Do not send work to Post Drafter until this and Gateway Content Router are both complete.

### 4. Post Drafter

- Purpose: Convert the routed blog opportunity plus persona guidance into a first blog draft.
- Trigger: Both content routing and persona shaping are complete.
- Inputs:
  - meeting summary
  - Gateway Content Router output
  - Persona Shaper output
  - project title and constraints
- Expected output:
  - first full draft
  - working title
  - structure suitable for editorial review
- Orchestrator rule: Pause immediately after draft receipt and request explicit admin approval.

### 5. Post Checker

- Purpose: Review the approved draft for overlap, duplication, conflicts, or reasons it should not advance yet.
- Trigger: Admin approval has been clearly received for the first draft.
- Inputs:
  - approved draft
  - prior topic context if available
- Expected output:
  - proceed or do-not-proceed decision
  - overlap findings
  - required fixes if blocked
- Orchestrator rule: If approval to proceed is not explicit, stop and report the blocker.

### 6. Editorial QA Lead

- Purpose: Perform final editorial review before the final approval gate.
- Trigger: Post Checker has approved proceeding.
- Inputs:
  - reviewed draft
  - checker notes
  - project context if relevant
- Expected output:
  - final editorial review
  - required corrections or approval-ready status
- Orchestrator rule: After this review, pause again and wait for explicit final approval.

### 7. Website Publisher

- Purpose: Publish the final approved draft to the website or prepare the exact publication package.
- Trigger: Final approval is explicit and all prior workflow steps are complete.
- Inputs:
  - final approved draft
  - title, slug, metadata, and destination if available
- Expected output:
  - publication confirmation or publication-ready package
- Orchestrator rule: Never trigger this skill without the full approval chain.

## High-Value Support Skills

These skills improve reliability and reduce stalled projects. These are not regarding the required orchestrated workflow steps but are about making the orchestration more robust and operationally smooth.

### 1. Workflow State Manager

- Purpose: Keep `blog-projects.md`, `workflow-checklist.md`, and `project-handoffs.md` current.
- Trigger: Any stage completion, approval, blocker, or new handoff.
- Inputs:
  - project identifier
  - current stage
  - completed steps
  - blockers
  - next action
- Expected output:
  - updated durable project record
- Why it helps: Prevents lost context across future runs.

### 2. Handoff Package Builder

- Purpose: Produce compact, complete handoff messages for each downstream role.
- Trigger: Whenever the orchestrator is ready to send work to another role.
- Inputs:
  - project id
  - source material for the stage
  - task request
  - constraints
  - expected return format
- Expected output:
  - one clean handoff package ready to send
- Why it helps: Keeps delegation consistent and reduces incomplete outputs.

### 3. Approval Gatekeeper

- Purpose: Detect whether feedback is actual approval, partial feedback, or ambiguous commentary.
- Trigger: The user or admin responds after a draft or final review.
- Inputs:
  - approval-stage context
  - exact approval message
- Expected output:
  - `approved`, `not approved`, or `ambiguous`
  - if ambiguous, the exact clarification needed
- Why it helps: Protects the two mandatory approval gates.

### 4. Blocker Recovery Manager

- Purpose: Diagnose what is missing when a stage cannot advance and prepare the correct recovery request.
- Trigger: A role output is incomplete, inconsistent, or missing.
- Inputs:
  - current stage
  - expected artifact
  - actual artifact or missing item
- Expected output:
  - blocker report
  - exact missing item
  - next recovery action
- Why it helps: Lets the orchestrator stop cleanly without losing prior progress.

### 5. Transcript Intake Validator

- Purpose: Confirm that an uploaded transcript is readable, complete enough to summarize, and correctly tied to a project.
- Trigger: A transcript or transcript file is first received.
- Inputs:
  - raw transcript
  - filename or attachment reference
  - project id if known
- Expected output:
  - valid intake confirmation or issue report
- Why it helps: Catches bad inputs before the workflow begins.

### 6. Final Approval Readiness Checker

- Purpose: Confirm that every required stage is complete before asking for final approval or publishing.
- Trigger: After Editorial QA Lead finishes review.
- Inputs:
  - full project state
  - approval history
  - latest draft status
- Expected output:
  - ready for final approval yes or no
  - any missing prerequisite
- Why it helps: Prevents accidental early publishing.

## Recommended Default Skill Stack

If this agent is being configured from scratch, these are the best skills to include by default:

1. Meeting Summarizer
2. Gateway Content Router
3. Persona Shaper
4. Post Drafter
5. Post Checker
6. Editorial QA Lead
7. Website Publisher
8. Workflow State Manager
9. Handoff Package Builder
10. Approval Gatekeeper
11. Blocker Recovery Manager
12. Transcript Intake Validator
13. Final Approval Readiness Checker

## Skill Use Order

The orchestrator should use the skills in this sequence:

1. Transcript Intake Validator
2. Meeting Summarizer
3. Gateway Content Router and Persona Shaper in parallel
4. Handoff Package Builder for Post Drafter
5. Post Drafter
6. Approval Gatekeeper
7. Post Checker
8. Editorial QA Lead
9. Final Approval Readiness Checker
10. Approval Gatekeeper
11. Website Publisher
12. Workflow State Manager throughout the full process

## Notes For Future Expansion

If this agent grows beyond orchestration, the next useful additions would be:

- SEO Metadata Planner for titles, descriptions, and keyword framing
- CMS Formatter for publication-ready formatting in a specific platform
- Content Calendar Coordinator for queueing approved posts
- Source Citation Extractor if blogs must quote or reference transcript sections precisely

For the current role, though, the best improvement is stronger operational support around approvals, handoffs, and workflow state rather than more writing skills.