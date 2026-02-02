# System Design Interview Base — Senior Solution Architect

> A comprehensive interview preparation guide with topic introductions, explanations, and practical Q&A at Basic, Medium, and Complex levels.

**Content has been restructured:** All topic content and Q&A now live in their respective topic files. This document serves as the index and navigation hub.

---

## Table of Contents
1. [00-Foundations](#00-foundations)
2. [01-API Design](#01-api-design)
3. [02-Data Storage](#02-data-storage)
4. [03-Caching](#03-caching)
5. [04-Messaging & Streaming](#04-messaging--streaming)
6. [05-Scalability Patterns](#05-scalability-patterns)
7. [06-Resilience](#06-resilience)
8. [07-Security](#07-security)
9. [08-Observability](#08-observability)
10. [09-Cloud Design](#09-cloud-design)
11. [10-System Design Cases](#10-system-design-cases)
12. [11-Interview Playbook](#11-interview-playbook)
13. [12-Enterprise Architecture TOGAF](12-enterprise-architecture-togaf/README.md)

---

## 00-Foundations

Core concepts: networking, latency, scalability, availability, fault tolerance.

### Topic Pages

| Topic | Link |
|-------|------|
| Availability vs Reliability | [00-foundations/availability-vs-reliability.md](00-foundations/availability-vs-reliability.md) |
| Fault Tolerance vs High Availability | [00-foundations/fault-tolerance-vs-high-availability.md](00-foundations/fault-tolerance-vs-high-availability.md) |
| Latency, Throughput & QPS | [00-foundations/latency-throughput-qps.md](00-foundations/latency-throughput-qps.md) |
| Scalability vs Performance | [00-foundations/scalability-vs-performance.md](00-foundations/scalability-vs-performance.md) |
| Networking Basics | [00-foundations/networking-basics.md](00-foundations/networking-basics.md) |

---

## 01-API Design

REST vs gRPC vs GraphQL, versioning, idempotency, rate limiting.

### Topic Pages

| Topic | Link |
|-------|------|
| REST vs gRPC vs GraphQL | [01-api-design/rest-vs-grpc-vs-graphql.md](01-api-design/rest-vs-grpc-vs-graphql.md) |
| Idempotency | [01-api-design/idempotency.md](01-api-design/idempotency.md) |
| API Versioning | [01-api-design/api-versioning.md](01-api-design/api-versioning.md) |
| Rate Limiting | [01-api-design/rate-limiting.md](01-api-design/rate-limiting.md) |

---

## 02-Data Storage

SQL vs NoSQL, consistency, indexing, partitioning, replication.

### Topic Pages

| Topic | Link |
|-------|------|
| SQL vs NoSQL | [02-data-storage/sql-vs-nosql.md](02-data-storage/sql-vs-nosql.md) |
| Consistency Models | [02-data-storage/consistency-models.md](02-data-storage/consistency-models.md) |
| Partitioning vs Sharding | [02-data-storage/partitioning-vs-sharding.md](02-data-storage/partitioning-vs-sharding.md) |
| Replication Strategies | [02-data-storage/replication-strategies.md](02-data-storage/replication-strategies.md) |
| Indexing Basics | [02-data-storage/indexing-basics.md](02-data-storage/indexing-basics.md) |

---

## 03-Caching

Cache patterns, eviction policies, hit/miss.

### Topic Pages

| Topic | Link |
|-------|------|
| Cache-Aside | [03-caching/cache-aside.md](03-caching/cache-aside.md) |
| Read-Through Cache | [03-caching/read-through-cache.md](03-caching/read-through-cache.md) |
| Write-Through Cache | [03-caching/write-through-cache.md](03-caching/write-through-cache.md) |
| Write-Back Cache | [03-caching/write-back-cache.md](03-caching/write-back-cache.md) |
| Eviction Policies | [03-caching/eviction-policies.md](03-caching/eviction-policies.md) |
| Cache Hit/Miss | [03-caching/cache-hit-miss.md](03-caching/cache-hit-miss.md) |

---

## 04-Messaging & Streaming

Sync vs async, queues, pub/sub, Kafka.

### Topic Pages

| Topic | Link |
|-------|------|
| Sync vs Async | [04-messaging-streaming/sync-vs-async.md](04-messaging-streaming/sync-vs-async.md) |
| Message Queues | [04-messaging-streaming/message-queues.md](04-messaging-streaming/message-queues.md) |
| Pub/Sub Pattern | [04-messaging-streaming/pub-sub-pattern.md](04-messaging-streaming/pub-sub-pattern.md) |
| Kafka Basics | [04-messaging-streaming/kafka-basics.md](04-messaging-streaming/kafka-basics.md) |

---

## 05-Scalability Patterns

Horizontal vs vertical, load balancing, autoscaling, stateless vs stateful.

### Topic Pages

| Topic | Link |
|-------|------|
| Horizontal vs Vertical Scaling | [05-scalability-patterns/horizontal-vs-vertical-scaling.md](05-scalability-patterns/horizontal-vs-vertical-scaling.md) |
| Load Balancing | [05-scalability-patterns/load-balancing.md](05-scalability-patterns/load-balancing.md) |
| Autoscaling | [05-scalability-patterns/autoscaling.md](05-scalability-patterns/autoscaling.md) |
| Stateless vs Stateful | [05-scalability-patterns/stateless-vs-stateful.md](05-scalability-patterns/stateless-vs-stateful.md) |

---

## 06-Resilience

Retries, circuit breaker, bulkhead, graceful degradation.

### Topic Pages

| Topic | Link |
|-------|------|
| Circuit Breaker | [06-resilience/circuit-breaker.md](06-resilience/circuit-breaker.md) |
| Retries & Timeouts | [06-resilience/retries-timeouts.md](06-resilience/retries-timeouts.md) |
| Bulkhead Pattern | [06-resilience/bulkhead-pattern.md](06-resilience/bulkhead-pattern.md) |
| Graceful Degradation | [06-resilience/graceful-degradation.md](06-resilience/graceful-degradation.md) |

---

## 07-Security

Auth, OAuth/JWT, encryption, secrets.

### Topic Pages

| Topic | Link |
|-------|------|
| Authentication vs Authorization | [07-security/authentication-vs-authorization.md](07-security/authentication-vs-authorization.md) |
| OAuth & JWT | [07-security/oauth-jwt.md](07-security/oauth-jwt.md) |
| Encryption at Rest & in Transit | [07-security/encryption-at-rest-in-transit.md](07-security/encryption-at-rest-in-transit.md) |
| Secrets Management | [07-security/secrets-management.md](07-security/secrets-management.md) |

---

## 08-Observability

Logging, metrics, tracing, SLIs/SLOs/SLAs.

### Topic Pages

| Topic | Link |
|-------|------|
| Logging | [08-observability/logging.md](08-observability/logging.md) |
| Metrics | [08-observability/metrics.md](08-observability/metrics.md) |
| Tracing | [08-observability/tracing.md](08-observability/tracing.md) |
| SLIs, SLOs & SLAs | [08-observability/slis-slos-slas.md](08-observability/slis-slos-slas.md) |

---

## 09-Cloud Design

Cloud models, multi-region, disaster recovery, cost.

### Topic Pages

| Topic | Link |
|-------|------|
| Cloud Service Models | [09-cloud-design/cloud-service-models.md](09-cloud-design/cloud-service-models.md) |
| Multi-Region Design | [09-cloud-design/multi-region-design.md](09-cloud-design/multi-region-design.md) |
| Disaster Recovery | [09-cloud-design/disaster-recovery.md](09-cloud-design/disaster-recovery.md) |
| Cost Optimization | [09-cloud-design/cost-optimization.md](09-cloud-design/cost-optimization.md) |

---

## 10-System Design Cases

End-to-end design exercises.

### Topic Pages

| Case | Link |
|------|------|
| URL Shortener | [10-system-design-cases/design-url-shortener.md](10-system-design-cases/design-url-shortener.md) |
| Rate Limiter | [10-system-design-cases/design-rate-limiter.md](10-system-design-cases/design-rate-limiter.md) |
| Chat System | [10-system-design-cases/design-chat-system.md](10-system-design-cases/design-chat-system.md) |
| Notification System | [10-system-design-cases/design-notification-system.md](10-system-design-cases/design-notification-system.md) |
| Feed System | [10-system-design-cases/design-feed-system.md](10-system-design-cases/design-feed-system.md) |
| Advanced Cases | [10-system-design-cases/design-advanced-cases.md](10-system-design-cases/design-advanced-cases.md) |

---

## 11-Interview Playbook

Framework, tradeoffs, common questions, red flags.

### Topic Pages

| Topic | Link |
|-------|------|
| System Design Framework | [11-interview-playbook/system-design-framework.md](11-interview-playbook/system-design-framework.md) |
| Tradeoff Cheat Sheet | [11-interview-playbook/tradeoff-cheat-sheet.md](11-interview-playbook/tradeoff-cheat-sheet.md) |
| Common Interviewer Questions | [11-interview-playbook/common-interviewer-questions.md](11-interview-playbook/common-interviewer-questions.md) |
| Red Flags to Avoid | [11-interview-playbook/red-flags-to-avoid.md](11-interview-playbook/red-flags-to-avoid.md) |

---

## Quick Reference: Difficulty Matrix

| Section | Basic | Medium | Complex |
|---------|-------|--------|---------|
| Foundations | 3 | 3 | 2 |
| API Design | 3 | 3 | 2 |
| Data Storage | 3 | 3 | 2 |
| Caching | 3 | 3 | 2 |
| Messaging | 3 | 3 | 2 |
| Scalability | 3 | 3 | 2 |
| Resilience | 3 | 3 | 2 |
| Security | 3 | 3 | 2 |
| Observability | 3 | 3 | 2 |
| Cloud Design | 3 | 3 | 2 |
| Design Cases | 3 | 2 | 3 |
| Playbook | 3 | 3 | 2 |

---

## How to Use This Guide

1. **Start with Foundations** — Ensure concepts are clear.
2. **Practice by section** — Answer out loud; time yourself (2–3 min basic, 5 min medium, 8 min complex).
3. **Design cases** — Use the framework; practice end-to-end (30–45 min).
4. **Cross-reference** — Link answers to topics (e.g., "rate limiter" uses caching, API design, scalability).
5. **Iterate** — Revisit complex questions; refine answers with tradeoffs and examples.

---

*Last updated: February 2025 | Repository: [system-design-interview-notes](./README.md)*
