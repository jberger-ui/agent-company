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

# Post Checker

This skill evaluates whether a planned article deserves to exist as a new post.

## Process

1. Search the repository for similar titles, slugs, drafts, and topic clusters.
2. Use any provided external search results to compare against public coverage and SERP patterns.
3. Compare the proposed angle against both.
4. Recommend whether to proceed, merge, narrow, or reposition the topic.

## What to return

- summary of local overlap
- summary of external overlap
- the clearest differentiated angle
- what content to keep
- what content to remove or de-emphasize
- merge recommendation when a new article is not justified
- concrete keep/remove guidance aligned to the overlap report schema

## Do not

- stop at finding overlap without making a recommendation
- write the full article
- invent web overlap when the external search layer did not provide it
