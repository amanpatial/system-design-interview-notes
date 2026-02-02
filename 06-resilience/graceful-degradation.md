# Graceful Degradation

## Introduction

**Graceful degradation** reduces functionality instead of failing completely. Partial service is better than total failure when appropriate.

## Definition

| Concept | Definition |
|---------|------------|
| **Graceful Degradation** | Reduce functionality instead of total failure |

## Q&A

### Medium

**Q: When would you choose graceful degradation over failing fast? How do you implement it?**

**A:** Graceful degradation when: partial service is better than none (e.g., show cached data, disable non-critical features). Fail fast when: incorrect partial response is worse than error (e.g., payment). Implement: identify critical vs optional features; on dependency failure, disable optional, serve from cache or simplified path; communicate clearly to user ("some features temporarily unavailable").

---

## See Also

- [Circuit Breaker](./circuit-breaker.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
