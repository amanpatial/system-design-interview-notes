# Fault Tolerance vs High Availability

## Introduction

**Fault tolerance** and **high availability (HA)** are related but distinct. Both aim to keep systems running, but they address different aspects of reliability.

## Definitions

| Concept | Definition |
|---------|------------|
| **Fault Tolerance** | System continues functioning correctly when components fail—graceful degradation, no data loss |
| **High Availability (HA)** | System designed to minimize downtime; stays up with minimal interruptions |

**Fault tolerance** asks: *When something fails, does the system keep working correctly?*  
**HA** asks: *Is the system reachable as much as possible?*

You can have HA without full fault tolerance (system stays up but returns errors or degraded functionality). True fault tolerance often implies HA.

## Q&A

### Basic

**Q: Explain fault tolerance vs high availability. Can you have one without the other?**

**A:** Fault tolerance means the system continues functioning correctly when components fail (graceful degradation, no data loss). HA means the system stays up with minimal downtime. You can have HA without full fault tolerance (system stays up but with degraded functionality). True fault tolerance often implies HA, but HA doesn't guarantee fault tolerance—a system could stay "up" while returning errors.

### Complex

**Q: Design a fault-tolerant system that maintains 99.99% availability for a read-heavy API. Walk through your failure scenarios and mitigations.**

**A:** Key design elements:

- (1) Multi-AZ deployment with redundant instances in each AZ.
- (2) Database: primary-replica with automatic failover, read replicas for scaling reads.
- (3) Caching: Redis cluster with replication; cache-aside with fallback to DB on cache miss.
- (4) Load balancer with health checks; remove unhealthy instances.
- (5) Circuit breaker for downstream dependencies.
- (6) Idempotent APIs for safe retries.

Failure scenarios: AZ failure → traffic shifts to other AZs; DB failover → replicas promote; cache failure → degrade to DB; dependency failure → circuit breaker prevents cascade.

---

## See Also

- [Availability vs Reliability](./availability-vs-reliability.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
