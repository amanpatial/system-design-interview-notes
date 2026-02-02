# Multi-Region Design

## Introduction

Multi-region deployment improves latency and resilience. **Active-active** vs **active-passive** trade off complexity and consistency.

## Q&A

### Basic

**Q: What is the difference between active-active and active-passive multi-region?**

**A:** Active-active: all regions serve reads and writes; lower latency globally; need conflict resolution. Active-passive: primary serves; standby replicates; failover on primary loss; simpler, no conflict resolution; standby may have stale data. Use active-active for global apps; active-passive when simplicity or consistency matters more.

### Medium

**Q: Design a multi-region deployment for a globally distributed app. Address latency, data consistency, and failover.**

**A:**

- Regions: deploy in 3+ regions (e.g., US, EU, Asia).
- Latency: route users to nearest region (GeoDNS, CDN); cache static assets.
- Data: primary region for writes; replicate to others (async or sync); consider CRDTs or last-writer-wins for conflict resolution.
- Failover: health checks; automatic DNS or LB failover; runbooks.

Accept eventual consistency for non-critical data; strong consistency where required (e.g., primary region only).

### Complex

**Q: Design a multi-region database strategy with strong consistency for critical data and eventual consistency for the rest. How do you handle failover and conflict resolution?**

**A:** Critical data (e.g., payments): single primary region; sync replica in DR; automatic failover; RPO near zero, RTO minutes.

Non-critical: multi-region with async replication; conflict resolution (last-writer-wins, vector clocks, or CRDTs).

Failover: automated for primary; promote replica; update DNS.

Conflict: avoid for critical (single writer); for rest, define resolution rules and surface conflicts to users when needed. Use managed DB with multi-region (e.g., Aurora Global DB, Cosmos DB).

---

## See Also

- [Disaster Recovery](./disaster-recovery.md)
- [Cost Optimization](./cost-optimization.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
