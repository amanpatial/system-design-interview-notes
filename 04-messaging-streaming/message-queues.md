# Message Queues

## Introduction

Message queues provide point-to-point delivery: one consumer processes each message. Used for task distribution, decoupling, and buffering.

## Q&A

### Basic

**Q: What is the difference between message queue and pub/sub?**

**A:** Message queue: point-to-point; message consumed by one consumer; workload distribution. Pub/sub: broadcast; message to multiple subscribers; event distribution. Queue: task distribution (e.g., process order). Pub/sub: event notification (e.g., order created → inventory, email, analytics). Kafka blurs the line: consumer groups act like queues; topics like pub/sub.

### Medium

**Q: Design an order processing system where: order placed → validate inventory → charge payment → ship. What if a step fails mid-flow? How do you ensure consistency?**

**A:** Use saga pattern: each step is a local transaction + compensating action on failure. Flow: Place order → Reserve inventory → Charge payment → Create shipment. If charge fails: release inventory. If ship fails: refund payment, release inventory. Implement via: (1) Choreography: each service publishes events; others react and compensate. (2) Orchestration: central coordinator calls services and triggers compensation. Ensure idempotency at each step. Use dead-letter queue for retries; eventual resolution (manual or automated).

---

## See Also

- [Pub/Sub Pattern](./pub-sub-pattern.md)
- [Kafka Basics](./kafka-basics.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
