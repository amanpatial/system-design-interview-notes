# Write-Through Cache

## Introduction

**Write-through** cache writes to both cache and database together. Cache stays in sync with the source of truth.

## Definition

| Concept | Definition |
|---------|------------|
| **Write-Through** | Write to cache and DB together; cache always in sync |

## Q&A

### Medium

**Q: Explain when cache increases consistency issues. How do you handle cache and DB consistency in a distributed system?**

**A:** Cache can serve stale data; concurrent updates can desync. Approaches:

- (1) Shorter TTL—trade freshness for load.
- (2) Write-through—writes go to both; reads are consistent.
- (3) Invalidation on write—delete/update cache when DB changes.
- (4) Version vectors—store version with cache; reject stale.
- (5) Accept eventual consistency with bounded staleness.
- (6) For strong consistency: don't cache, or use cache that participates in transactions (limited support).

Often: TTL + invalidation on write is a practical compromise.

---

## See Also

- [Write-Back Cache](./write-back-cache.md)
- [Cache-Aside](./cache-aside.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
