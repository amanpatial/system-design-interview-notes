# Consistency Models

## Introduction

Consistency models define what clients observe when reading data. Strong consistency ensures correctness; eventual consistency trades it for availability and performance.

## Definitions

| Model | Definition |
|-------|------------|
| **Strong Consistency** | Reads always see latest write |
| **Eventual Consistency** | Reads may see stale data; converges over time |

## Q&A

### Basic

**Q: Explain strong vs eventual consistency. Give an example where eventual consistency is acceptable.**

**A:** Strong: every read returns the most recent write. Eventual: reads may return older data; system converges to consistent state. Eventual is acceptable when: temporary inconsistency has low impact (e.g., like counts, view counts, social feed)—eventually correct is fine. Not acceptable for: financial transactions, inventory deduct, medical records.

### Medium

**Q: Explain read-your-writes consistency. How would you implement it in a system with read replicas?**

**A:** Read-your-writes: after a write, the same user's subsequent reads see that write. With replicas, read might hit a replica that hasn't received the write yet. Implementation:

- (1) Route reads for same user to primary until replication lag is acceptable.
- (2) Use session affinity: same user → same replica, with replication tracking.
- (3) Wait for replication: after write, wait for replica to catch up before serving reads (increases latency).
- (4) Version/timestamp: reject read if replica is behind; retry or read from primary.

### Complex

**Q: A system uses eventual consistency. Users report seeing duplicate transactions after retries. How do you fix this while preserving availability?**

**A:** Root cause: retries create duplicate operations. Solutions:

- (1) Idempotency keys: client sends unique key per logical operation; server deduplicates.
- (2) Idempotent writes: design operations so replay is safe (e.g., "add $10" vs "set balance to $110").
- (3) Distributed lock or conditional writes: "update if version = X" to prevent overwrites.
- (4) Transaction log: append-only log with dedup; async apply.
- (5) Compensation: detect duplicates (e.g., via idempotency key), reverse or merge.

Best: idempotency keys at API layer + idempotent design of business logic.

---

## See Also

- [SQL vs NoSQL](./sql-vs-nosql.md)
- [Replication Strategies](./replication-strategies.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
