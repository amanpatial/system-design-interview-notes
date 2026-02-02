# Design: Rate Limiter

## Introduction

A rate limiter restricts request frequency per client. Considerations: algorithms (fixed/sliding window, token bucket), distributed vs single-node, and consistency.

## Q&A

### Basic

**Q: Design a rate limiter. What algorithms can you use?**

**A:** Algorithms: (1) Fixed window: count per window; simple, boundary issue. (2) Sliding window: smooth, more accurate. (3) Token bucket: allow bursts. (4) Leaky bucket: smooth output. Storage: in-memory for single node; Redis for distributed. Key: user_id or IP. Implementation: Redis INCR with TTL, or sliding window log. Return 429 with Retry-After.

### Complex

**Q: Design a distributed rate limiter that works across multiple API gateway instances. Consider consistency and performance.**

**A:** Challenge: each instance must enforce global limit. Solution: Redis as shared store. Sliding window: Lua script for atomic INCR + ZREMRANGEBYSCORE + ZADD. Token bucket: store (tokens, last_update) in Redis; Lua for atomic check-and-update. Consistency: Redis is single source of truth; eventual consistency if Redis is clustered. Performance: local cache for "under limit" with short TTL to reduce Redis calls. Consider sliding window log for accuracy.

---

## See Also

- [01-API Design / Rate Limiting](../01-api-design/rate-limiting.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
