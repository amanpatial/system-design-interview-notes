# Horizontal vs Vertical Scaling

## Introduction

**Horizontal scaling** (scale out) adds more machines. **Vertical scaling** (scale up) adds more resources to a single machine. Choice affects cost, limits, and complexity.

## Definitions

| Type | Definition |
|------|------------|
| **Horizontal Scaling** | Add more machines (scale out) |
| **Vertical Scaling** | Add more resources to a machine (scale up) |

## Q&A

### Basic

**Q: What is the difference between horizontal and vertical scaling? What are the limits of each?**

**A:** Vertical: bigger machine (CPU, RAM). Simpler, no distributed complexity; hits hardware limits, single point of failure, costly at high end. Horizontal: more machines. Scales further, fault tolerant; adds complexity (distribution, consistency, coordination). Vertical for quick wins; horizontal for long-term scale. Cloud favors horizontal (elasticity).

### Complex

**Q: Design a system that scales from 100 to 100,000 users. What are the key bottlenecks at each stage and how do you address them?**

**A:**

- 100–1K: single server fine; DB on same or separate.
- 1K–10K: add caching, DB read replicas, CDN for static.
- 10K–100K: horizontal scaling of app tier, connection pooling, async processing, message queue.
- 100K+: sharding, multi-region, event-driven, specialized stores (search, analytics).

Bottlenecks: DB connections → pool, read replicas; CPU → scale app; DB write → shard, async; network → CDN, compression. Plan for each order of magnitude.

---

## See Also

- [Load Balancing](./load-balancing.md)
- [Autoscaling](./autoscaling.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
