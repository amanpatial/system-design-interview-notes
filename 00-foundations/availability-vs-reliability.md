# Availability vs Reliability

## Introduction

**Availability** and **Reliability** are related but distinct concepts in system design. Both matter for production systems, but they measure different things and require different strategies to improve.

## Definitions

| Concept | Definition |
|---------|------------|
| **Availability** | % of time a system is operational and reachable (e.g., 99.9% = 3 nines) |
| **Reliability** | Probability the system performs correctly over time—fewer failures, correct results when it does respond |

**Availability** asks: *Is the system up?*  
**Reliability** asks: *When it's up, does it work correctly?*

A system can be highly available but unreliable (often up but returns wrong data or errors). Conversely, a system can be reliable but have poor availability (when it works, it works correctly, but it's frequently down).

## Key Differences

- **Availability** = uptime percentage; focuses on *reachability*
- **Reliability** = correctness over time; focuses on *trustworthiness*

Improving availability often involves redundancy, failover, and reducing recovery time. Improving reliability involves better code, testing, validation, and preventing silent failures.

## Related Concepts

### Nines (Availability Levels)

| Level | Percentage | Downtime/Year |
|-------|------------|---------------|
| Two nines | 99% | ~3.65 days |
| Three nines | 99.9% | ~8.76 hours |
| Four nines | 99.99% | ~52.6 minutes |
| Five nines | 99.999% | ~5.26 minutes |

Each additional nine significantly reduces allowed downtime and increases complexity and cost. Most production systems target 99.9%–99.95%; five nines is reserved for critical systems (e.g., payment processing, healthcare).

### MTBF and MTTR

- **MTBF** (Mean Time Between Failures): average time between failures
- **MTTR** (Mean Time To Recovery): average time to restore service after a failure

**Availability ≈ MTBF / (MTBF + MTTR)**

To improve availability: increase MTBF (redundancy, better code, proactive maintenance) and decrease MTTR (automated failover, runbooks, observability). For HA, reducing MTTR often gives faster ROI than chasing higher MTBF.

---

## Q&A — Availability vs Reliability

### Basic

**Q: What do "three nines" and "five nines" mean in availability?**

**A:** Three nines (99.9%) = ~8.76 hours downtime/year. Five nines (99.999%) = ~5.26 minutes downtime/year. Each additional nine significantly reduces allowed downtime and increases complexity and cost. Most production systems target 99.9%–99.95%; five nines is reserved for critical systems.

---

**Q: What is the difference between availability and reliability?**

**A:** Availability measures uptime—% of time the system is reachable. Reliability measures correctness—the system performs as expected when it responds. A system can be available but unreliable (often up but buggy), or reliable but poorly available (correct when up, but frequently down).

---

### Medium

**Q: How do MTBF and MTTR relate to availability? How would you improve each?**

**A:** MTBF (Mean Time Between Failures) is average time between failures; MTTR (Mean Time To Recovery) is average time to restore service after failure. Availability ≈ MTBF / (MTBF + MTTR). To improve availability: increase MTBF (redundancy, better code, proactive maintenance) and decrease MTTR (automated failover, runbooks, observability). For HA, reducing MTTR often gives faster ROI than chasing higher MTBF.

---

**Q: When would you prioritize availability over consistency, and vice versa? Give a real-world example for each.**

**A:** Prioritize availability when: user experience degrades more from being blocked than from stale data (e.g., social feed—show cached content rather than error). Prioritize consistency when: incorrect data causes serious harm (e.g., bank balance, inventory for checkout). CAP theorem forces the tradeoff in partition scenarios; the choice depends on business impact of inconsistency vs unavailability.

---

### Complex

**Q: A system has 99.9% availability. A critical dependency has 99.5% availability. What's the theoretical combined availability? How would you improve it?**

**A:** For series dependency: combined = 0.999 × 0.995 ≈ 99.4%. The weaker link dominates. Improvements:

- (1) Redundant dependencies (parallel)—if either works, system works; combined availability increases.
- (2) Circuit breaker + fallback to degrade gracefully instead of failing.
- (3) Caching to reduce dependency on the weaker service.
- (4) Upgrade the dependency's SLA or replace it.

---

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

- [Fault Tolerance vs High Availability](./fault-tolerance-vs-high-availability.md) — related concepts
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md) — full foundations Q&A
