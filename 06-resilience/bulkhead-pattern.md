# Bulkhead Pattern

## Introduction

**Bulkhead** isolates resources so failure in one area doesn't drain shared resources. Like ship compartments that limit flooding.

## Definition

| Concept | Definition |
|---------|------------|
| **Bulkhead** | Isolate resources (thread pools, connections) per dependency |

## Q&A

### Basic

**Q: What is the bulkhead pattern? Give an example.**

**A:** Bulkhead: isolate resources so failure in one area doesn't drain shared resources. Example: separate thread pools per downstream service. If service A is slow, its pool fills but B and C keep their pools. Without bulkhead, one slow service could exhaust all threads. Like ship compartments that limit flooding.

---

## See Also

- [Circuit Breaker](./circuit-breaker.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
