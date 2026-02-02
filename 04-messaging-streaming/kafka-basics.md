# Kafka Basics

## Introduction

**Kafka** is a distributed event streaming platform. High throughput, durable log, replay, and stream processing. Often compared to traditional message queues.

## Definitions

| Concept | Definition |
|---------|------------|
| **Streaming** | Continuous, ordered, replayable event log |

## Q&A

### Basic

**Q: Why would you choose Kafka over RabbitMQ (or vice versa)?**

**A:** Kafka: high throughput, durable log, replay, stream processing, retention for days. RabbitMQ: traditional queue, complex routing, lower latency for single messages, flexible patterns. Choose Kafka for: event sourcing, stream processing, replay, high throughput. Choose RabbitMQ for: task queues, complex routing, lower latency, simpler operational model.

### Medium

**Q: How does Kafka achieve high throughput? What are the tradeoffs?**

**A:** Mechanisms: (1) Sequential disk I/O—log append is fast. (2) Zero-copy—kernel sends data without copying to user space. (3) Batching—producer and consumer batch messages. (4) Partitioning—parallelism per partition. (5) No per-message ACK—batch commit. Tradeoffs: higher latency for single messages (batching); ordering only per partition; more complex than simple queue; retention uses disk.

**Q: Explain exactly-once semantics in Kafka. What's required to achieve it?**

**A:** Exactly-once needs: (1) Idempotent producer—deduplicate by producer ID + sequence. (2) Transactional writes—atomic write across partitions. (3) Read-process-write in consumer—consumer commits offset only after successful process and output write; use transactional producer to make consumer read and output write atomic. Requirements: Kafka 0.11+, idempotent producer enabled, transactional producer for consumer. Careful design to avoid duplicates from retries and reprocessing.

### Complex

**Q: Design an event-driven system for real-time analytics: clicks, views, purchases from multiple sources. Requirements: low latency ingestion, exactly-once processing, aggregations (counts, sums) in near real-time. What components and topology?**

**A:** Ingestion: API receives events → Kafka (partitioned by user_id or session_id for ordering). Exactly-once: idempotent producer, consumer with transactional commit. Processing: Kafka Streams or Flink for aggregation (windows, state stores). Output: materialized views to Redis/DB for low-latency queries; or push to OLAP (ClickHouse, Druid). Schema: use Avro/Protobuf with schema registry. Consider: backpressure, dead-letter for bad events, monitoring lag and throughput.

**Q: A Kafka consumer falls behind (lag increases). What are the causes and how do you address them?**

**A:** Causes: (1) Consumer too slow—processing is CPU/IO heavy. (2) Not enough consumers—fewer than partitions. (3) Uneven partition distribution—hot partitions. (4) Downstream slow—DB, API. (5) Large messages—serialization/deserialization cost. Solutions: (1) Scale consumers (up to partition count). (2) Optimize processing—async, batching, parallel within consumer. (3) Increase partition count (requires care; can't decrease easily). (4) Add more consumer instances. (5) Consider separate consumer group for batch processing. (6) Optimize downstream—cache, async writes. (7) If backlog is huge, consider rewriting consumer to process in parallel from multiple offsets (e.g., parallel batch jobs).

---

## See Also

- [Message Queues](./message-queues.md)
- [Pub/Sub Pattern](./pub-sub-pattern.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
