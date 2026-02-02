# Circuit Breaker

## Introduction

**Circuit breaker** stops calling a failing service, fails fast, and periodically probes recovery. Prevents cascading failures and wasted load on a down dependency.

## Definition

| Concept | Definition |
|---------|------------|
| **Circuit Breaker** | Stop calling failing service; fail fast; periodically probe |

## Q&A

### Basic

**Q: Explain the states of a circuit breaker. When does it transition between them?**

**A:** Closed: normal; requests pass through. Open: after failure threshold; requests fail immediately (no call to dependency). Half-open: after timeout; allow limited test requests. If test succeeds → closed. If test fails → open. Prevents cascading failures and wasted calls to a down service.

### Medium

**Q: A circuit breaker is open. What are the implications for the failing service when it recovers? How do you avoid a stampede when it closes?**

**A:** When open, no traffic goes to the service; it may recover. When closed, traffic returns. Stampede: many requests at once can overload a recovering service. Mitigations: (1) Half-open with limited concurrency (e.g., 1–2 test requests). (2) Gradual traffic increase. (3) Rate limit requests when transitioning to closed. (4) Ensure dependency has recovered (health checks) before closing.

### Complex

**Q: Design a resilient service that calls 5 downstream dependencies. One is critical; four are optional. Handle timeouts, retries, and cascading failures.**

**A:** Critical: circuit breaker, retry with backoff, timeout. Fail the request if critical fails after retries. Optional: circuit breaker per dependency, no retry (or 1 retry), short timeout. Use bulkheads: separate connection pools/thread pools per dependency. Call optional in parallel where possible; don't let one block others. Aggregate: return partial success with flags for which optional data is missing. Use fallbacks: cache, default values for optional.

**Q: Implement a distributed circuit breaker. Single-node is easy; how do you coordinate state across multiple service instances?**

**A:** Options: (1) Local circuit breaker per instance—simplest; each instance may open/close independently; eventual consistency. (2) Shared state: Redis stores circuit state (open/closed/half-open, failure count); all instances read/write. Need atomic updates. (3) Central coordinator: one instance decides; others query (adds dependency). (4) Event broadcast: instance that opens broadcasts; others open locally. Tradeoff: local is simpler but can send traffic during recovery; shared is coordinated but adds latency and dependency on Redis.

---

## See Also

- [Retries & Timeouts](./retries-timeouts.md)
- [Bulkhead Pattern](./bulkhead-pattern.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
