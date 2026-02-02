# Rate Limiting

## Introduction

**Rate limiting** restricts request frequency per client to protect APIs, ensure fairness, and control costs.

## Definition

| Concept | Definition |
|---------|------------|
| **Rate Limiting** | Restricting request frequency per client/key |

## Q&A

### Basic

**Q: Design a rate limiter. What algorithms can you use?**

**A:** Algorithms:

- (1) Fixed window: count per window; simple, boundary issue.
- (2) Sliding window: smooth, more accurate.
- (3) Token bucket: allow bursts.
- (4) Leaky bucket: smooth output.

Storage: in-memory for single node; Redis for distributed. Key: user_id or IP. Implementation: Redis INCR with TTL, or sliding window log. Return 429 with Retry-After.

### Medium

**Q: Design a rate limiter for an API. Consider: sliding window vs fixed window, distributed vs single-node, and handling burst traffic.**

**A:** Algorithms:

- (1) Fixed window—simple but allows 2× limit at boundaries.
- (2) Sliding window—smoother, more accurate.
- (3) Token bucket—allows bursts within average rate.
- (4) Leaky bucket—smooths bursts.

Distributed: use Redis with Lua for atomic ops; key = user/IP + window. Sliding window: `ZADD` with timestamp, `ZREMRANGEBYSCORE` for expired, `ZCARD` for count. For burst: token bucket with configurable bucket size. Return `Retry-After` header on 429.

---

## See Also

- [REST vs gRPC vs GraphQL](./rest-vs-grpc-vs-graphql.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
