# Design: Feed System

## Introduction

A feed system (e.g., Twitter timeline) displays posts from followed users. Fan-out strategy (push vs pull vs hybrid) is the central design choice.

## Q&A

### Medium

**Q: Design a feed system (like Twitter's timeline). Discuss fan-out strategies: push vs pull vs hybrid.**

**A:** Push (fan-out on write): on post, write to all followers' feeds. Fast read, slow write; storage cost for popular users. Pull (fan-out on read): on read, fetch from followed users. Fast write, slow read; need to optimize (cache, limit). Hybrid: push for most users; pull for celebrities (many followers). Store: feed table (user_id, post_id, timestamp) for push; post table for pull. Cache hot feeds.

---

## See Also

- [02-Data Storage](../02-data-storage/)
- [03-Caching](../03-caching/)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
