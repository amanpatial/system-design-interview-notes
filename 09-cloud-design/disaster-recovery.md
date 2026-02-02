# Disaster Recovery

## Introduction

**Disaster recovery (DR)** ensures systems can recover from major failures. RTO and RPO drive backup, replication, and failover design.

## Q&A

### Basic

**Q: Define RTO and RPO. How do they influence disaster recovery design?**

**A:** RPO (Recovery Point Objective): max acceptable data loss (e.g., 1 hour). Drives backup/replication frequency. RTO (Recovery Time Objective): max acceptable downtime (e.g., 4 hours). Drives failover automation and readiness. Lower RPO/RTO = more replication, automation, cost.

### Medium

**Q: Design a disaster recovery plan. What are the key steps and how do you test it?**

**A:** Steps:

- (1) Define RTO/RPO.
- (2) Backup strategy: frequency, retention, encryption.
- (3) Replication: sync/async to DR region.
- (4) Runbooks: failover steps, contacts.
- (5) Test regularly: DR drill (quarterly).

Test:

- (1) Failover to DR; verify app and data.
- (2) Failback.
- (3) Document lessons.
- (4) Chaos engineering for practice.

Automation reduces human error during real DR.

---

## See Also

- [Multi-Region Design](./multi-region-design.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
