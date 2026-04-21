---
name: head-publisher
description: Use when an approved blog draft is ready for final validation and publication to the company website or CMS.
metadata:
  sources:
    - kind: github-file
      repo: jberger-ui/Project-1
      path: .agents/skills/head-publisher/SKILL.md
      commit: main
      trackingRef: main
      url: https://github.com/jberger-ui/Project-1/blob/main/.agents/skills/head-publisher/SKILL.md
      usageMode: mirrored
---

# Head Publisher

This skill handles safe publication.

## Pre-publication checklist

- approval exists
- approval decision is explicitly `approved`
- final draft source is identified
- title, slug, summary, and metadata are valid
- destination website or CMS target is correct
- duplicate publication risk has been checked
- draft metadata and approval decision refer to the same run and idea

## Publish behavior

- prefer idempotent operations
- return precise errors when a prerequisite is missing
- report the canonical URL or publication identifier after success
- include retryable and rollback guidance when publication fails or succeeds

## Do not

- publish an unapproved draft
- silently alter the article's strategic intent
