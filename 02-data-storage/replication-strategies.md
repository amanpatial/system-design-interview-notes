# Replication Strategies

## Introduction

Replication increases availability and read capacity. Single-leader, multi-leader, and leaderless strategies offer different tradeoffs for consistency and availability.

## Q&A

### Medium

**Q: Compare replication strategies: single-leader, multi-leader, and leaderless. When is each appropriate?**

**A:** Single-leader: one primary, replicas sync; simple, strong consistency on primary; failover complexity. Multi-leader: multiple primaries (e.g., multi-region); write availability, conflict resolution needed. Leaderless (Dynamo-style): quorum reads/writes; no single point of failure; higher latency, read repair. Use single-leader for strong consistency and simplicity; multi-leader for geographic distribution and write availability; leaderless for maximum availability and partition tolerance.

---

## See Also

- [Consistency Models](./consistency-models.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
