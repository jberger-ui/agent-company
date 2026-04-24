---
schema: agentcompanies/v1
kind: company
name: Authority Engine
slug: authority-engine
version: 1.0.0
license: MIT
authors:
  - name: Jacob Berger
  - name: OpenAI ChatGPT

description: Use this company package when work involves running an AEO and SEO optimization company that converts transcripts, market inputs, and subject-matter expertise into differentiated blog content for websites at scale.
tags:
  - aeo
  - seo
  - content-operations
  - blogging
  - transcript-to-blog
  - website-optimization
metadata:
  sources:
    - kind: github-dir
      repo: jberger-ui/Project-1
      path: .agents
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1
      usageMode: mirrored
goals:
  - Turn transcripts, calls, strategy notes, and raw subject matter expertise into high-quality blog content for websites.
  - Increase client visibility across organic search, answer engines, and authority-building topical clusters.
  - Maintain editorial differentiation, deterministic workflow state, and safe publication controls.
  - Preserve a scalable operating model where strategy, operations, drafting, QA, and publishing stay clearly separated.
requirements:
  - Do not trigger the transcript-to-blog workflow unless a new task explicitly includes a transcript or transcript-derived source material.
  - Do not publish drafts without an explicit approval state.
  - Do not bypass overlap and differentiation checks before drafting or publishing.
  - Preserve run-level state, artifact lineage, and publication records.
includes:
  - ./teams/leadership/TEAM.md
  - ./teams/content-intelligence/TEAM.md
  - ./teams/writing/TEAM.md
  - ./teams/review-compliance/TEAM.md
  - ./teams/creative-production/TEAM.md
  - ./teams/publishing/TEAM.md
  - ./projects/content-engine-hardening/PROJECT.md
  - ./projects/programmatic-authority-expansion/PROJECT.md
  - ./projects/answer-engine-footprint/PROJECT.md
---

# Authority Engine

Authority Engine is a markdown-first Agent Company package for an AEO and SEO content business.

## Operating model

The company turns transcripts and source material into production-ready blog outputs through a controlled pipeline:

1. intake and summarize source material
2. extract and route article-worthy ideas
3. shape content for a specific audience or business persona
4. draft the article
5. check overlap, differentiation, and editorial readiness
6. design the supporting visual package
7. package and publish only after approval and target validation

## Activation guidance

Activate this company package when the runtime needs to:

- run or supervise transcript-to-blog production
- plan AEO and SEO editorial operations
- coordinate strategy, routing, drafting, QA, and publication
- manage repeatable website content work across multiple topics or sites

Do not activate the entire company for isolated stand-alone writing requests that do not require company workflows, approvals, or publishing logic.

## Core company rules

- Start from real source material, not invented content premises.
- Treat transcript evidence, topic differentiation, and publication approval as first-class constraints.
- Prefer reusable skill procedures over repeating methods inside multiple role files.
- Keep strategy decisions, editorial judgment, and publication side effects separated.
- Preserve deterministic output structures and run lineage wherever possible.
