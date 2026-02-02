# Write-Back Cache

## Introduction

**Write-back** (write-behind) cache writes to cache first and asynchronously to the database. Higher throughput but risk of data loss.

## Definition

| Concept | Definition |
|---------|------------|
| **Write-Back** | Write to cache; async write to DB; risk of data loss |

## Q&A

### Basic

**Q: What are the risks of write-back cache? When is it acceptable?**

**A:** Risks: data loss if cache fails before flushing to DB; inconsistency between cache and DB. Acceptable when:

- (1) Data is disposable or reproducible (e.g., analytics, session data).
- (2) Write volume is very high and DB can't keep up.
- (3) You have replication and can tolerate some loss.

Mitigate with: persistence (Redis AOF), replicate cache, batch writes, circuit breaker to fail over to sync writes on issues.

---

## See Also

- [Write-Through Cache](./write-through-cache.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
