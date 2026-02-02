# Partitioning vs Sharding

## Introduction

Partitioning and sharding both split data, but at different scopes. Partitioning is within a single node; sharding distributes across nodes for horizontal scale.

## Definitions

| Concept | Definition |
|---------|------------|
| **Partitioning** | Splitting data within a single DB (e.g., by range) |
| **Sharding** | Distributing data across multiple DB instances |

## Q&A

### Basic

**Q: What is the difference between partitioning and sharding?**

**A:** Partitioning: logical or physical division of data within one database (e.g., table partitioning by date). Sharding: distributing data across multiple database instances/servers. Partitioning can be for organization/performance within one node; sharding is for horizontal scalability across nodes. Sharding implies data is split across machines; partitioning may be local.

### Medium

**Q: Design a sharding strategy for a user table with 1B rows. How do you choose a shard key? What are the tradeoffs?**

**A:** Shard key options:

- (1) User ID hash—even distribution, but range queries across users are hard.
- (2) User ID range—enables range queries; can cause hotspots (e.g., recent users).
- (3) Tenant/org ID—multi-tenant isolation; uneven if tenant sizes vary.
- (4) Composite (tenant_id, user_id)—balance distribution and locality.

For 1B users: hash(user_id) mod N shards gives even spread. Avoid shard keys that cause hotspots (e.g., timestamp alone). Consider consistent hashing for adding/removing shards without full rehash.

### Complex

**Q: Design a time-series data store for 10TB of metrics (timestamp, metric_id, value) with queries: point lookup, range by time, and aggregation by metric. Address indexing, retention, and compression.**

**A:** Schema: (metric_id, timestamp) as composite key for locality.

- Index: B-tree or LSM on (metric_id, timestamp).
- Partitioning: by time (e.g., daily) for retention and pruning.
- Sharding: by metric_id hash for even distribution.
- Storage: columnar format for aggregation (e.g., Parquet); compression (delta encoding, run-length).
- Retention: TTL or background jobs to drop old partitions.

Use TimescaleDB, InfluxDB, or Cassandra with time-based compaction. For aggregation: pre-aggregate (e.g., 1min, 1hr) for common queries.

---

## See Also

- [Indexing Basics](./indexing-basics.md)
- [Replication Strategies](./replication-strategies.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
