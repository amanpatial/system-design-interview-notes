# Latency, Throughput & QPS

## Introduction

**Latency**, **throughput**, and **QPS** (queries per second) are core metrics for understanding system performance and capacity.

## Definitions

| Concept | Definition |
|---------|------------|
| **Latency** | Time for a single request/operation to complete (e.g., 50ms p99) |
| **Throughput** | Number of operations processed per unit time (e.g., 10K req/s) |
| **QPS** | Queries per second—throughput measured in requests/second |

## Q&A

### Basic

**Q: What is the difference between latency and throughput?**

**A:** Latency is the time it takes for a single operation to complete (e.g., 100ms response time). Throughput is how many operations the system can process per second (e.g., 5,000 requests/second). They're related but distinct: a system can have low latency with low throughput (fast but few concurrent users), or high latency with high throughput (slow per request but handling many at once).

---

## See Also

- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
