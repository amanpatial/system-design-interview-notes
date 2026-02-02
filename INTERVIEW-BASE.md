# System Design Interview Base — Senior Solution Architect

> A comprehensive interview preparation guide with topic introductions, explanations, and practical Q&A at Basic, Medium, and Complex levels.

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

---

## 00-Foundations

### Topic Introduction

Foundations cover the core concepts every solution architect must understand: networking basics, latency vs throughput, scalability vs performance, availability vs reliability, and fault tolerance vs high availability. These form the vocabulary and mental models for discussing distributed systems.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Latency** | Time for a single request to complete (e.g., 50ms p99) |
| **Throughput** | Number of requests processed per unit time (e.g., 10K QPS) |
| **Availability** | % of time a system is operational (e.g., 99.9% = 3 nines) |
| **Reliability** | Probability system performs correctly over time (fewer failures) |
| **Scalability** | Ability to handle growth by adding resources |
| **Performance** | Speed/efficiency of a system under load |
| **Fault Tolerance** | System continues operating when components fail |
| **High Availability (HA)** | System designed to minimize downtime |

### Topic Pages

- **[Availability vs Reliability](00-foundations/availability-vs-reliability.md)** — Definitions, nines, MTBF/MTTR, and Q&A

### Q&A — Foundations

#### BASIC

**Q1: What is the difference between latency and throughput?**

**A:** Latency is the time it takes for a single operation to complete (e.g., 100ms response time). Throughput is how many operations the system can process per second (e.g., 5,000 requests/second). They're related but distinct: a system can have low latency with low throughput (fast but few concurrent users), or high latency with high throughput (slow per request but handling many at once).

---

**Q3: Explain scalability vs performance.**

**A:** Scalability is the ability to handle more load by adding resources (more servers, more capacity). Performance is how fast or efficiently the system runs at a given scale. A system can be performant (fast single request) but not scalable (hits a ceiling). A scalable system can grow; a performant system runs well at current scale.

---

#### MEDIUM

**Q6: Explain fault tolerance vs high availability. Can you have one without the other?**

**A:** Fault tolerance means the system continues functioning correctly when components fail (graceful degradation, no data loss). HA means the system stays up with minimal downtime. You can have HA without full fault tolerance (system stays up but with degraded functionality). True fault tolerance often implies HA, but HA doesn't guarantee fault tolerance—a system could stay "up" while returning errors.

---

---

## 01-API Design

### Topic Introduction

API design covers how systems expose and consume interfaces. Key areas include REST vs gRPC vs GraphQL, API versioning, idempotency for safe retries, and rate limiting for protection and fairness.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **REST** | Resource-oriented, HTTP verbs, stateless, JSON/XML |
| **gRPC** | RPC over HTTP/2, binary (Protobuf), streaming, low latency |
| **GraphQL** | Query language, client specifies needed fields, single endpoint |
| **Idempotency** | Same request multiple times = same effect as once |
| **Rate Limiting** | Restricting request frequency per client/key |

---

### Q&A — API Design

#### BASIC

**Q1: When would you choose REST over gRPC, and vice versa?**

**A:** Choose REST when: public APIs, browser clients, wide tooling support, human-readable payloads, CRUD-heavy. Choose gRPC when: microservice-to-microservice, performance-critical, need streaming (bidirectional), strong typing with code generation, mobile/low-bandwidth (binary). GraphQL when clients need flexible querying and you want to avoid over/under-fetching.

---

**Q2: What is idempotency and why does it matter for APIs?**

**A:** Idempotency means repeating the same request produces the same result as executing it once. Critical for: retries (network failures, timeouts), duplicate submissions (user double-clicks), exactly-once processing. Implement via idempotency keys: client sends unique key; server stores key with result; duplicate requests return cached result. Essential for payment and order APIs.

---

**Q3: What are common API versioning strategies? What are their tradeoffs?**

**A:** (1) URL path: `/v1/users`—clear, cacheable; requires new routes. (2) Query param: `/users?version=1`—optional; messy for many versions. (3) Header: `Accept: application/vnd.api.v1+json`—clean URLs; less discoverable. (4) No versioning, backward-compatible changes—simplest but limits evolution. For public APIs, path versioning is common; for internal, headers or backward compatibility often suffice.

---

#### MEDIUM

**Q4: Design a rate limiter for an API. Consider: sliding window vs fixed window, distributed vs single-node, and handling burst traffic.**

**A:** Algorithms: (1) Fixed window—simple but allows 2× limit at boundaries. (2) Sliding window—smoother, more accurate. (3) Token bucket—allows bursts within average rate. (4) Leaky bucket—smooths bursts. Distributed: use Redis with Lua for atomic ops; key = user/IP + window. Sliding window: `ZADD` with timestamp, `ZREMRANGEBYSCORE` for expired, `ZCARD` for count. For burst: token bucket with configurable bucket size. Return `Retry-After` header on 429.

---

**Q5: How would you design an API that supports both synchronous and asynchronous processing? When would a client use each?**

**A:** Sync: immediate response (e.g., GET, simple POST). Async: return 202 Accepted with `Location` header to poll for result, or use webhooks/callbacks. Use sync for: fast operations (< few seconds), simple CRUD. Use async for: long-running jobs (report generation, bulk imports), resource-intensive ops. Design: POST creates job → 202 + job ID; GET /jobs/{id} returns status; optionally webhook on completion. Client chooses based on operation type and UX requirements.

---

**Q6: Explain the tradeoffs between REST, gRPC, and GraphQL for a B2B platform with 50+ integrating partners.**

**A:** REST: partners expect it, easy onboarding, wide SDK support; risk of over-fetching and version sprawl. gRPC: great for internal services; many partners lack gRPC tooling; consider gRPC-Web or REST gateway. GraphQL: flexible queries reduce over-fetching; schema evolution is easier; but exposes more surface, requires auth/rate limit at query level, and some partners prefer REST. Recommendation: offer REST for public API (adoption), GraphQL as optional for power users; use gRPC internally.

---

#### COMPLEX

**Q7: Design an API gateway that handles versioning, rate limiting, authentication, and routing for 100+ microservices. What components and data flows would you use?**

**A:** Components: (1) Gateway (Kong, AWS API Gateway, Envoy)—single entry, routing, middleware. (2) Auth: validate JWT/OAuth; optionally call auth service. (3) Rate limiting: Redis-backed, per API key + endpoint. (4) Version routing: path/header → service version; maintain mapping. (5) Service discovery: route to healthy instances. Flow: Request → TLS termination → Auth → Rate limit check → Version resolution → Route to backend → Response (aggregate, transform if needed). Consider: caching at gateway, circuit breaker for backends, request/response logging for audit.

---

**Q8: How would you evolve an existing REST API to GraphQL without breaking existing clients? Describe migration strategy and compatibility concerns.**

**A:** Strategy: (1) Add GraphQL endpoint alongside REST (`/graphql`). (2) Build GraphQL schema that mirrors REST resources; resolvers call existing REST services or shared logic. (3) Run both in parallel; new clients use GraphQL. (4) Deprecate REST endpoints gradually with long notice. Compatibility: shared auth, rate limits, and SLAs. Ensure GraphQL doesn't create N+1 or expensive queries—implement query complexity analysis, depth limits, and pagination. Use schema stitching if services expose their own GraphQL. Consider Apollo Federation for microservice GraphQL.

---

---

## 02-Data Storage

### Topic Introduction

Data storage covers database selection (SQL vs NoSQL), consistency models, indexing, partitioning vs sharding, and replication strategies. These decisions underpin scalability, reliability, and performance of data-intensive systems.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **SQL** | Relational, ACID, structured schema, joins |
| **NoSQL** | Document, key-value, wide-column, graph; flexible schema |
| **Strong Consistency** | Reads always see latest write |
| **Eventual Consistency** | Reads may see stale data; converges over time |
| **Partitioning** | Splitting data within a single DB (e.g., by range) |
| **Sharding** | Distributing data across multiple DB instances |

---

### Q&A — Data Storage

#### BASIC

**Q1: When would you choose SQL over NoSQL, and vice versa?**

**A:** SQL when: complex queries, joins, transactions, strong consistency, relational data (orders, users, inventory). NoSQL when: flexible schema, high write throughput, horizontal scaling, specific access patterns (key-value lookup, document by ID, graph traversals). Choose based on access patterns and consistency requirements, not hype.

---

**Q2: Explain strong vs eventual consistency. Give an example where eventual consistency is acceptable.**

**A:** Strong: every read returns the most recent write. Eventual: reads may return older data; system converges to consistent state. Eventual is acceptable when: temporary inconsistency has low impact (e.g., like counts, view counts, social feed)—eventually correct is fine. Not acceptable for: financial transactions, inventory deduct, medical records.

---

**Q3: What is the difference between partitioning and sharding?**

**A:** Partitioning: logical or physical division of data within one database (e.g., table partitioning by date). Sharding: distributing data across multiple database instances/servers. Partitioning can be for organization/performance within one node; sharding is for horizontal scalability across nodes. Sharding implies data is split across machines; partitioning may be local.

---

#### MEDIUM

**Q4: Design a sharding strategy for a user table with 1B rows. How do you choose a shard key? What are the tradeoffs?**

**A:** Shard key options: (1) User ID hash—even distribution, but range queries across users are hard. (2) User ID range—enables range queries; can cause hotspots (e.g., recent users). (3) Tenant/org ID—multi-tenant isolation; uneven if tenant sizes vary. (4) Composite (tenant_id, user_id)—balance distribution and locality. For 1B users: hash(user_id) mod N shards gives even spread. Avoid shard keys that cause hotspots (e.g., timestamp alone). Consider consistent hashing for adding/removing shards without full rehash.

---

**Q5: Explain read-your-writes consistency. How would you implement it in a system with read replicas?**

**A:** Read-your-writes: after a write, the same user's subsequent reads see that write. With replicas, read might hit a replica that hasn't received the write yet. Implementation: (1) Route reads for same user to primary until replication lag is acceptable. (2) Use session affinity: same user → same replica, with replication tracking. (3) Wait for replication: after write, wait for replica to catch up before serving reads (increases latency). (4) Version/timestamp: reject read if replica is behind; retry or read from primary.

---

**Q6: Compare replication strategies: single-leader, multi-leader, and leaderless. When is each appropriate?**

**A:** Single-leader: one primary, replicas sync; simple, strong consistency on primary; failover complexity. Multi-leader: multiple primaries (e.g., multi-region); write availability, conflict resolution needed. Leaderless (Dynamo-style): quorum reads/writes; no single point of failure; higher latency, read repair. Use single-leader for strong consistency and simplicity; multi-leader for geographic distribution and write availability; leaderless for maximum availability and partition tolerance.

---

#### COMPLEX

**Q7: Design a time-series data store for 10TB of metrics (timestamp, metric_id, value) with queries: point lookup, range by time, and aggregation by metric. Address indexing, retention, and compression.**

**A:** Schema: (metric_id, timestamp) as composite key for locality. Index: B-tree or LSM on (metric_id, timestamp). Partitioning: by time (e.g., daily) for retention and pruning. Sharding: by metric_id hash for even distribution. Storage: columnar format for aggregation (e.g., Parquet); compression (delta encoding, run-length). Retention: TTL or background jobs to drop old partitions. Use TimescaleDB, InfluxDB, or Cassandra with time-based compaction. For aggregation: pre-aggregate (e.g., 1min, 1hr) for common queries.

---

**Q8: A system uses eventual consistency. Users report seeing duplicate transactions after retries. How do you fix this while preserving availability?**

**A:** Root cause: retries create duplicate operations. Solutions: (1) Idempotency keys: client sends unique key per logical operation; server deduplicates. (2) Idempotent writes: design operations so replay is safe (e.g., "add $10" vs "set balance to $110"). (3) Distributed lock or conditional writes: "update if version = X" to prevent overwrites. (4) Transaction log: append-only log with dedup; async apply. (5) Compensation: detect duplicates (e.g., via idempotency key), reverse or merge. Best: idempotency keys at API layer + idempotent design of business logic.

---

---

## 03-Caching

### Topic Introduction

Caching reduces latency and load by storing frequently accessed data closer to consumers. Topics include cache patterns (cache-aside, read-through, write-through, write-back), eviction policies, and cache hit/miss behavior.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Cache-Aside** | App manages cache; on miss, load from DB and populate cache |
| **Read-Through** | Cache proxies reads; transparent to app |
| **Write-Through** | Write to cache and DB together; cache always in sync |
| **Write-Back** | Write to cache; async write to DB; risk of data loss |
| **Eviction** | LRU, LFU, TTL—deciding what to remove when full |

---

### Q&A — Caching

#### BASIC

**Q1: Explain cache-aside vs read-through. When would you use each?**

**A:** Cache-aside: application checks cache; on miss, loads from DB and populates cache. Gives app full control. Read-through: cache layer loads from DB on miss; app only talks to cache. Simpler for app; cache must integrate with DB. Use cache-aside when using generic cache (Redis, Memcached). Use read-through when cache is built into storage (e.g., DAX for DynamoDB) or you want app simplicity.

---

**Q2: What are the risks of write-back cache? When is it acceptable?**

**A:** Risks: data loss if cache fails before flushing to DB; inconsistency between cache and DB. Acceptable when: (1) Data is disposable or reproducible (e.g., analytics, session data). (2) Write volume is very high and DB can't keep up. (3) You have replication and can tolerate some loss. Mitigate with: persistence (Redis AOF), replicate cache, batch writes, circuit breaker to fail over to sync writes on issues.

---

**Q3: Compare LRU vs LFU eviction. Which is better for a news feed cache?**

**A:** LRU: evicts least recently used. Good for temporal locality. LFU: evicts least frequently used. Good for popularity. News feed: mix of trending (high frequency) and new (recent). LRU can evict popular older items; LFU can hold old popular items and evict new hot items. Consider: LRU with TTL for freshness, or hybrid (e.g., TinyLFU, W-TinyLFU) that considers both recency and frequency.

---

#### MEDIUM

**Q4: Design a caching strategy for an e-commerce product catalog. Products change occasionally; some are popular. Handle cache invalidation.**

**A:** Cache product by ID. Invalidation: (1) TTL (e.g., 1 hr) for eventual consistency. (2) Event-driven: on product update, publish event; cache layer invalidates or updates. (3) Version/ETag: cache stores version; on update, version changes; conditional fetch. (4) Categories/listing: invalidate category cache when product in category changes. Use cache-aside with Redis. For popular products: longer TTL or pre-warm. Consider CDN for static product images.

---

**Q5: How do you prevent cache stampede (thundering herd) when a popular key expires?**

**A:** Stampede: many requests miss simultaneously, all hit DB. Solutions: (1) Probabilistic early expiration: before TTL, with low probability refresh in background. (2) Lock/mutex: first request acquires lock, loads, others wait or get stale. (3) Request coalescing: single in-flight load per key; others wait for result. (4) Stale-while-revalidate: serve stale, refresh async. (5) Random jitter on TTL to spread expirations. Implement with Redis SETNX for locking or use libraries (e.g., cache-aside with coalescing).

---

**Q6: Explain when cache increases consistency issues. How do you handle cache and DB consistency in a distributed system?**

**A:** Cache can serve stale data; concurrent updates can desync. Approaches: (1) Shorter TTL—trade freshness for load. (2) Write-through—writes go to both; reads are consistent. (3) Invalidation on write—delete/update cache when DB changes. (4) Version vectors—store version with cache; reject stale. (5) Accept eventual consistency with bounded staleness. (6) For strong consistency: don't cache, or use cache that participates in transactions (limited support). Often: TTL + invalidation on write is a practical compromise.

---

#### COMPLEX

**Q7: Design a multi-layer cache (L1 in-process, L2 Redis) for a high-throughput API. When does data go to each layer? How do you handle invalidation across layers?**

**A:** L1 (in-process): hottest keys, nanosecond access, limited size (e.g., 10K keys). L2 (Redis): broader set, millisecond access, larger. Flow: read from L1 → miss → L2 → miss → DB. Write: invalidate or update both layers. Invalidation: (1) Pub/Sub: on write, publish invalidation; all app nodes subscribed, clear L1. (2) TTL: both layers have TTL; L1 shorter than L2 to avoid long staleness. (3) Version in key: new version = new key; old expires. Challenge: ensuring all nodes get invalidation; Redis Pub/Sub or broadcast. Consider cache stampede at L2; use coalescing.

---

**Q8: A cache has 90% hit rate but still high DB load. Diagnose and propose solutions.**

**A:** Possible causes: (1) 10% miss handling high traffic—even 1% of large traffic is big. (2) Popular keys evicted—hot keys not fitting in cache. (3) Cache key design—too specific, low reuse (e.g., per-user keys for shared data). (4) Thundering herd on miss. (5) Expensive queries on miss—single miss triggers heavy query. Solutions: (1) Increase cache size or optimize eviction for hot keys. (2) Cache at coarser granularity where possible. (3) Request coalescing, lock, or stale-while-revalidate. (4) Pre-warm cache for known hot keys. (5) Optimize DB queries and add indexes. (6) Add read replicas for cache miss traffic.

---

---

## 04-Messaging & Streaming

### Topic Introduction

Messaging enables loose coupling and async processing. Covers sync vs async communication, message queues, pub/sub, and streaming (e.g., Kafka). Critical for event-driven and scalable architectures.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Sync** | Caller waits for response; tight coupling |
| **Async** | Fire-and-forget or callback; loose coupling |
| **Message Queue** | Point-to-point; one consumer per message |
| **Pub/Sub** | Publish to topic; multiple subscribers |
| **Streaming** | Continuous, ordered, replayable event log |

---

### Q&A — Messaging & Streaming

#### BASIC

**Q1: When would you use sync vs async communication between services?**

**A:** Sync when: need immediate response (e.g., auth check, fetch user), simple request-response, client must have result to continue. Async when: fire-and-forget (notifications), long-running work, decoupling (producer doesn't need to know consumers), reliability (queue buffers if consumer is down). Prefer async for scalability and resilience; use sync only when necessary.

---

**Q2: What is the difference between message queue and pub/sub?**

**A:** Message queue: point-to-point; message consumed by one consumer; workload distribution. Pub/sub: broadcast; message to multiple subscribers; event distribution. Queue: task distribution (e.g., process order). Pub/sub: event notification (e.g., order created → inventory, email, analytics). Kafka blurs the line: consumer groups act like queues; topics like pub/sub.

---

**Q3: Why would you choose Kafka over RabbitMQ (or vice versa)?**

**A:** Kafka: high throughput, durable log, replay, stream processing, retention for days. RabbitMQ: traditional queue, complex routing, lower latency for single messages, flexible patterns. Choose Kafka for: event sourcing, stream processing, replay, high throughput. Choose RabbitMQ for: task queues, complex routing, lower latency, simpler operational model.

---

#### MEDIUM

**Q4: Design an order processing system where: order placed → validate inventory → charge payment → ship. What if a step fails mid-flow? How do you ensure consistency?**

**A:** Use saga pattern: each step is a local transaction + compensating action on failure. Flow: Place order → Reserve inventory → Charge payment → Create shipment. If charge fails: release inventory. If ship fails: refund payment, release inventory. Implement via: (1) Choreography: each service publishes events; others react and compensate. (2) Orchestration: central coordinator calls services and triggers compensation. Ensure idempotency at each step. Use dead-letter queue for retries; eventual resolution (manual or automated).

---

**Q5: How does Kafka achieve high throughput? What are the tradeoffs?**

**A:** Mechanisms: (1) Sequential disk I/O—log append is fast. (2) Zero-copy—kernel sends data without copying to user space. (3) Batching—producer and consumer batch messages. (4) Partitioning—parallelism per partition. (5) No per-message ACK—batch commit. Tradeoffs: higher latency for single messages (batching); ordering only per partition; more complex than simple queue; retention uses disk.

---

**Q6: Explain exactly-once semantics in Kafka. What's required to achieve it?**

**A:** Exactly-once needs: (1) Idempotent producer—deduplicate by producer ID + sequence. (2) Transactional writes—atomic write across partitions. (3) Read-process-write in consumer—consumer commits offset only after successful process and output write; use transactional producer to make consumer read and output write atomic. Requirements: Kafka 0.11+, idempotent producer enabled, transactional producer for consumer. Careful design to avoid duplicates from retries and reprocessing.

---

#### COMPLEX

**Q7: Design an event-driven system for real-time analytics: clicks, views, purchases from multiple sources. Requirements: low latency ingestion, exactly-once processing, aggregations (counts, sums) in near real-time. What components and topology?**

**A:** Ingestion: API receives events → Kafka (partitioned by user_id or session_id for ordering). Exactly-once: idempotent producer, consumer with transactional commit. Processing: Kafka Streams or Flink for aggregation (windows, state stores). Output: materialized views to Redis/DB for low-latency queries; or push to OLAP (ClickHouse, Druid). Schema: use Avro/Protobuf with schema registry. Consider: backpressure, dead-letter for bad events, monitoring lag and throughput.

---

**Q8: A Kafka consumer falls behind (lag increases). What are the causes and how do you address them?**

**A:** Causes: (1) Consumer too slow—processing is CPU/IO heavy. (2) Not enough consumers—fewer than partitions. (3) Uneven partition distribution—hot partitions. (4) Downstream slow—DB, API. (5) Large messages—serialization/deserialization cost. Solutions: (1) Scale consumers (up to partition count). (2) Optimize processing—async, batching, parallel within consumer. (3) Increase partition count (requires care; can't decrease easily). (4) Add more consumer instances. (5) Consider separate consumer group for batch processing. (6) Optimize downstream—cache, async writes. (7) If backlog is huge, consider rewriting consumer to process in parallel from multiple offsets (e.g., parallel batch jobs).

---

---

## 05-Scalability Patterns

### Topic Introduction

Scalability patterns include horizontal vs vertical scaling, load balancing, autoscaling, and stateless vs stateful design. These enable systems to grow with demand.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Horizontal Scaling** | Add more machines (scale out) |
| **Vertical Scaling** | Add more resources to a machine (scale up) |
| **Load Balancer** | Distribute traffic across instances |
| **Stateless** | No server-side session; any instance can serve |
| **Stateful** | Server holds session state |

---

### Q&A — Scalability Patterns

#### BASIC

**Q1: What is the difference between horizontal and vertical scaling? What are the limits of each?**

**A:** Vertical: bigger machine (CPU, RAM). Simpler, no distributed complexity; hits hardware limits, single point of failure, costly at high end. Horizontal: more machines. Scales further, fault tolerant; adds complexity (distribution, consistency, coordination). Vertical for quick wins; horizontal for long-term scale. Cloud favors horizontal (elasticity).

---

**Q2: Explain L4 vs L7 load balancing. When would you use each?**

**A:** L4 (transport): IP + port; no awareness of HTTP. Fast, low overhead; can't route by path, header, or content. L7 (application): HTTP-aware; route by URL, header, cookie. Enables canary, A/B, path-based routing. Use L4 for raw throughput (e.g., TCP); L7 when you need content-based routing, SSL termination, or HTTP features.

---

**Q3: Why is stateless design preferred for scalability?**

**A:** Stateless: any instance can serve any request; no server affinity. Enables: easy horizontal scaling, simple load balancing, no session migration on instance failure. Stateful: need sticky sessions or state replication; complicates scaling and failover. Store state in DB, cache, or client; keep servers stateless.

---

#### MEDIUM

**Q4: Design autoscaling for a web API. What metrics would you use? How do you avoid flapping?**

**A:** Metrics: CPU, request rate, latency (p99), queue depth. Scale up: high CPU or latency, or queue building. Scale down: low CPU and latency. Flapping: scale up/down repeatedly. Avoid: (1) Cooldown period after scale action. (2) Different thresholds for scale-up vs scale-down (hysteresis). (3) Scale-down more slowly than scale-up. (4) Use multiple metrics (e.g., scale up if CPU > 70% for 3 min; scale down if CPU < 30% for 10 min).

---

**Q5: How do you handle stateful workloads (e.g., WebSocket servers, gaming servers) in a horizontally scaled environment?**

**A:** Options: (1) Sticky sessions: load balancer routes same client to same instance; instance holds state. Risk: instance failure loses state. (2) Externalize state: Redis/DB for session; any instance can serve. (3) Sharding: assign users to instances by user_id; client reconnects to same shard. (4) State replication: replicate to backup (complex). (5) Accept reconnection: design for reconnect and state rebuild. Often: sticky sessions + externalized critical state + graceful shutdown with drain.

---

**Q6: Compare round-robin, least connections, and consistent hashing for load balancing. When is each appropriate?**

**A:** Round-robin: rotate evenly. Simple; ignores actual load. Least connections: send to instance with fewest active connections. Better for varying request duration. Consistent hashing: same key always to same instance (or small set). Good for caching, session affinity. Use round-robin for similar requests; least connections for mixed durations; consistent hashing when locality matters.

---

#### COMPLEX

**Q7: Design a system that scales from 100 to 100,000 users. What are the key bottlenecks at each stage and how do you address them?**

**A:** 100–1K: single server fine; DB on same or separate. 1K–10K: add caching, DB read replicas, CDN for static. 10K–100K: horizontal scaling of app tier, connection pooling, async processing, message queue. 100K+: sharding, multi-region, event-driven, specialized stores (search, analytics). Bottlenecks: DB connections → pool, read replicas; CPU → scale app; DB write → shard, async; network → CDN, compression. Plan for each order of magnitude.

---

**Q8: A load balancer is a single point of failure. How do you make it highly available?**

**A:** (1) Active-passive: standby LB; failover via health checks (e.g., VRRP, keepalived). (2) Active-active: multiple LBs; DNS round-robin or anycast; each can handle full load. (3) Cloud LB: use managed service (ALB, ELB) with multiple AZs. (4) DNS failover: multiple LB IPs; health-based DNS. (5) Eliminate LB: client-side load balancing (service mesh, client knows all endpoints). Tradeoff: complexity vs availability.

---

---

## 06-Resilience

### Topic Introduction

Resilience patterns help systems handle failures gracefully: retries with backoff, circuit breakers, bulkheads to isolate failures, and graceful degradation. Essential for distributed systems.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Retry** | Retry failed requests; use backoff to avoid overload |
| **Circuit Breaker** | Stop calling failing service; fail fast; periodically probe |
| **Bulkhead** | Isolate resources (thread pools, connections) per dependency |
| **Graceful Degradation** | Reduce functionality instead of total failure |

---

### Q&A — Resilience

#### BASIC

**Q1: Explain the states of a circuit breaker. When does it transition between them?**

**A:** Closed: normal; requests pass through. Open: after failure threshold; requests fail immediately (no call to dependency). Half-open: after timeout; allow limited test requests. If test succeeds → closed. If test fails → open. Prevents cascading failures and wasted calls to a down service.

---

**Q2: Why use exponential backoff for retries? What about jitter?**

**A:** Exponential backoff: wait longer after each retry (e.g., 1s, 2s, 4s). Gives failing service time to recover; avoids thundering herd. Jitter: add randomness to delay. Prevents synchronized retries from many clients that could cause spikes. Use both for robust retries.

---

**Q3: What is the bulkhead pattern? Give an example.**

**A:** Bulkhead: isolate resources so failure in one area doesn't drain shared resources. Example: separate thread pools per downstream service. If service A is slow, its pool fills but B and C keep their pools. Without bulkhead, one slow service could exhaust all threads. Like ship compartments that limit flooding.

---

#### MEDIUM

**Q4: Design retry logic for an API client. Consider: idempotency, max retries, backoff, and when not to retry.**

**A:** Retry on: timeouts, 5xx, network errors. Don't retry on: 4xx (except 429), non-idempotent operations without idempotency key. Config: max 3–5 retries, exponential backoff (base 1s, max 30s), jitter. Use idempotency keys for POST/PUT. Implement: retry with exponential backoff + jitter; respect Retry-After if present (429, 503).

---

**Q5: When would you choose graceful degradation over failing fast? How do you implement it?**

**A:** Graceful degradation when: partial service is better than none (e.g., show cached data, disable non-critical features). Fail fast when: incorrect partial response is worse than error (e.g., payment). Implement: identify critical vs optional features; on dependency failure, disable optional, serve from cache or simplified path; communicate clearly to user ("some features temporarily unavailable").

---

**Q6: A circuit breaker is open. What are the implications for the failing service when it recovers? How do you avoid a stampede when it closes?**

**A:** When open, no traffic goes to the service; it may recover. When closed, traffic returns. Stampede: many requests at once can overload a recovering service. Mitigations: (1) Half-open with limited concurrency (e.g., 1–2 test requests). (2) Gradual traffic increase. (3) Rate limit requests when transitioning to closed. (4) Ensure dependency has recovered (health checks) before closing.

---

#### COMPLEX

**Q7: Design a resilient service that calls 5 downstream dependencies. One is critical; four are optional. Handle timeouts, retries, and cascading failures.**

**A:** Critical: circuit breaker, retry with backoff, timeout. Fail the request if critical fails after retries. Optional: circuit breaker per dependency, no retry (or 1 retry), short timeout. Use bulkheads: separate connection pools/thread pools per dependency. Call optional in parallel where possible; don't let one block others. Aggregate: return partial success with flags for which optional data is missing. Use fallbacks: cache, default values for optional.

---

**Q8: Implement a distributed circuit breaker. Single-node is easy; how do you coordinate state across multiple service instances?**

**A:** Options: (1) Local circuit breaker per instance—simplest; each instance may open/close independently; eventual consistency. (2) Shared state: Redis stores circuit state (open/closed/half-open, failure count); all instances read/write. Need atomic updates. (3) Central coordinator: one instance decides; others query (adds dependency). (4) Event broadcast: instance that opens broadcasts; others open locally. Tradeoff: local is simpler but can send traffic during recovery; shared is coordinated but adds latency and dependency on Redis.

---

---

## 07-Security

### Topic Introduction

Security covers authentication vs authorization, OAuth/JWT, encryption at rest and in transit, and secrets management. Essential for protecting systems and data.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Authentication** | Verifying identity (who are you?) |
| **Authorization** | Verifying permission (what can you do?) |
| **OAuth 2.0** | Delegation protocol for authorization |
| **JWT** | Stateless token with claims; signed |
| **Encryption at rest** | Encrypt stored data |
| **Encryption in transit** | TLS for data in flight |

---

### Q&A — Security

#### BASIC

**Q1: What is the difference between authentication and authorization?**

**A:** Authentication: proving identity (e.g., password, MFA). Authorization: checking permission to perform an action (e.g., can user X delete resource Y?). AuthN first; then AuthZ. Example: login is AuthN; "can this user access /admin" is AuthZ.

---

**Q2: When would you use JWT vs session cookies?**

**A:** JWT: stateless, good for APIs, microservices, cross-domain; can't easily revoke before expiry. Session: stateful server; easy revocation; simpler for traditional web apps. Use JWT for: API-to-API, mobile, stateless scaling. Use sessions for: web apps with easy logout, when revocation is critical.

---

**Q3: Explain OAuth 2.0 authorization code flow. Why use authorization code instead of returning tokens directly?**

**A:** Flow: (1) User redirected to auth server. (2) User logs in, approves. (3) Auth server redirects back with authorization code (not token). (4) Client exchanges code for token server-side. Why: code is short-lived, used once; tokens never sent in URL (visible in history, Referer). Safer than implicit flow where token is in redirect URL.

---

#### MEDIUM

**Q4: Design an API authentication strategy for: web app, mobile app, and third-party partners. Each has different requirements.**

**A:** Web app: session cookies (HttpOnly, Secure) or short-lived JWT with refresh token. Mobile: JWT or OAuth; store tokens securely (keychain/keystore); use refresh tokens. Third-party: OAuth 2.0 client credentials or API keys; rate limit per key; rotate keys. Use same auth service; different flows per client type. Validate tokens at API gateway.

---

**Q5: How do you manage secrets (DB passwords, API keys) in a cloud deployment? What are the pitfalls?**

**A:** Use secret manager (AWS Secrets Manager, Vault, GCP Secret Manager). Inject at runtime (env vars, sidecar) or fetch on startup. Pitfalls: (1) Don't commit to git. (2) Rotate regularly; automate rotation. (3) Least privilege—apps get only what they need. (4) Audit access. (5) Encrypt at rest. (6) Avoid long-lived credentials; use IAM roles where possible.

---

**Q6: Explain encryption at rest vs in transit. What happens if you have one but not the other?**

**A:** In transit: TLS; protects from eavesdropping, tampering on the wire. At rest: encrypt data on disk; protects if storage is stolen. Only in transit: data on disk is readable if storage is compromised. Only at rest: data is exposed on the network. Need both for defense in depth.

---

#### COMPLEX

**Q7: Design a zero-trust API architecture. Assume no implicit trust based on network position.**

**A:** Principles: (1) Verify every request—auth on every call, no "internal" bypass. (2) Least privilege—grant minimum access. (3) Assume breach—segment, encrypt, audit. Implementation: (1) mTLS or JWT for service-to-service. (2) API gateway validates all requests. (3) Policy engine (e.g., OPA) for fine-grained AuthZ. (4) Encrypt everything; no trusted network. (5) Audit logs for all access. (6) Short-lived credentials, no long-lived keys.

---

**Q8: A JWT is compromised. How do you revoke it before expiry? Design a solution that scales.**

**A:** JWTs are stateless; server doesn't track them. Options: (1) Short expiry (e.g., 15 min) + refresh token (stored, revocable). (2) Token blocklist: store revoked token IDs in Redis; check on each request. Doesn't scale for many revocations. (3) Version/epoch: include version in JWT; revoke by bumping version; all old tokens invalid. (4) Short-lived + sliding refresh: compromise has limited window. Best: short-lived JWT + revocable refresh token; for critical actions, re-auth or check blocklist.

---

---

## 08-Observability

### Topic Introduction

Observability enables understanding system behavior: logging, metrics, and tracing. SLIs, SLOs, and SLAs define and measure reliability. Critical for operations and debugging.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **Logging** | Discrete events; structured for search |
| **Metrics** | Numerical measurements over time |
| **Tracing** | Request flow across services |
| **SLI** | Service Level Indicator (what we measure) |
| **SLO** | Service Level Objective (target we aim for) |
| **SLA** | Service Level Agreement (contract with consequences) |

---

### Q&A — Observability

#### BASIC

**Q1: What is the difference between logging, metrics, and tracing? When would you use each?**

**A:** Logging: event records (errors, info); debug, audit. Metrics: numbers (latency, error rate, QPS); dashboards, alerting. Tracing: request flow across services; performance debugging. Use logs for details; metrics for trends and alerts; tracing for distributed request flow.

---

**Q2: Define SLI, SLO, and SLA. How are they related?**

**A:** SLI: measurable indicator (e.g., availability = successful requests / total). SLO: target (e.g., 99.9% availability). SLA: business contract with penalties (e.g., credits if < 99.9%). SLO is internal target; SLA is external promise. SLO often stricter than SLA to allow buffer.

---

**Q3: What makes a good SLI?**

**A:** Good SLI: (1) Reflects user experience (e.g., latency as perceived by user). (2) Measurable automatically. (3) Actionable—we can improve it. (4) Aligned with business. Examples: availability (successful requests), latency (p99), error rate. Avoid vanity metrics that don't reflect user impact.

---

#### MEDIUM

**Q4: Design a monitoring strategy for a microservices architecture. What do you measure, and how do you avoid alert fatigue?**

**A:** Measure: RED (Rate, Errors, Duration) per service; dependency health; queue depth; resource utilization. Avoid fatigue: (1) Few high-signal alerts—page only for user impact. (2) Tiered: critical (page), warning (ticket), info (dashboard). (3) Runbooks for every alert. (4) Avoid alerting on symptoms; alert on causes or user impact. (5) SLO-based alerting: burn rate, error budget.

---

**Q5: How does distributed tracing work? What must be propagated across service boundaries?**

**A:** Tracing: assign trace ID to request; each service creates spans (operation, duration); spans have parent-child relationship. Propagate: trace ID, span ID, parent span ID (e.g., via headers). Backend aggregates spans by trace ID for full picture. Standards: OpenTelemetry, Zipkin, Jaeger. Enables finding latency bottlenecks across services.

---

**Q6: Explain error budget. How do you use it for release decisions?**

**A:** Error budget: 1 - SLO (e.g., 99.9% availability = 0.1% budget = ~43 min downtime/month). Consumed by incidents. Use: (1) If budget exhausted, freeze risky releases until budget resets. (2) Prioritize reliability work when budget is low. (3) Allow calculated risk: small releases consume little budget. Balances reliability and velocity.

---

#### COMPLEX

**Q7: Design an observability stack for 50+ microservices: logging, metrics, tracing. Address scale, cost, and retention.**

**A:** Logging: centralized (ELK, Loki); ship from agents or sidecar; structure logs (JSON); sample at high volume (e.g., 10% of success, 100% of errors); retention 7–30 days; archive to cold storage. Metrics: Prometheus or vendor; scrape or push; aggregate (recording rules); retention 15–90 days; downsampling for long retention. Tracing: OTel collectors; sample (e.g., 1% or tail-based on errors); store in Jaeger/Tempo; retention 7 days. Cost: sampling, retention policies, tiered storage.

---

**Q8: A production incident occurs. Walk through your debugging process using logs, metrics, and traces. How do you correlate them?**

**A:** (1) Start with metrics: when did latency/errors spike? Which service? (2) Traces: find slow or failed traces in that window; identify bottleneck span. (3) Logs: filter by trace ID for full context; look for errors. (4) Correlate: trace ID in logs and traces; timestamp alignment. (5) Dependency: check downstream services in trace. (6) Correlate with deployments: time of change. Use correlated IDs (trace_id, request_id) across all three pillars.

---

---

## 09-Cloud Design

### Topic Introduction

Cloud design covers service models (IaaS, PaaS, SaaS), multi-region deployment, disaster recovery, and cost optimization. Critical for building robust, cost-effective cloud-native systems.

### Basic Explanations

| Concept | Definition |
|---------|------------|
| **IaaS** | Infrastructure (VMs, storage); you manage OS and above |
| **PaaS** | Platform (e.g., app runtime); you manage app only |
| **SaaS** | Software as a service; consume only |
| **Active-Active** | Multiple regions serve traffic; write to all |
| **Active-Passive** | Primary serves; standby for failover |

---

### Q&A — Cloud Design

#### BASIC

**Q1: Compare IaaS, PaaS, and SaaS. When would you choose each?**

**A:** IaaS: max control, max ops (e.g., Kubernetes on VMs). PaaS: less ops, less control (e.g., App Engine, Lambda). SaaS: no infra (e.g., Salesforce). Choose IaaS for customization; PaaS for speed and managed runtime; SaaS for non-differentiating functions. Many orgs use mix.

---

**Q2: What is the difference between active-active and active-passive multi-region?**

**A:** Active-active: all regions serve reads and writes; lower latency globally; need conflict resolution. Active-passive: primary serves; standby replicates; failover on primary loss; simpler, no conflict resolution; standby may have stale data. Use active-active for global apps; active-passive when simplicity or consistency matters more.

---

**Q3: Define RTO and RPO. How do they influence disaster recovery design?**

**A:** RPO (Recovery Point Objective): max acceptable data loss (e.g., 1 hour). Drives backup/replication frequency. RTO (Recovery Time Objective): max acceptable downtime (e.g., 4 hours). Drives failover automation and readiness. Lower RPO/RTO = more replication, automation, cost.

---

#### MEDIUM

**Q4: Design a multi-region deployment for a globally distributed app. Address latency, data consistency, and failover.**

**A:** Regions: deploy in 3+ regions (e.g., US, EU, Asia). Latency: route users to nearest region (GeoDNS, CDN); cache static assets. Data: primary region for writes; replicate to others (async or sync); consider CRDTs or last-writer-wins for conflict resolution. Failover: health checks; automatic DNS or LB failover; runbooks. Accept eventual consistency for non-critical data; strong consistency where required (e.g., primary region only).

---

**Q5: How do you optimize cloud costs without sacrificing reliability?**

**A:** (1) Right-size: match instance to workload; use metrics. (2) Reserved/savings plans for steady workload. (3) Spot for fault-tolerant, interruptible workload. (4) Auto-scale: scale down when idle. (5) Storage tiers: hot/warm/cold. (6) Delete unused resources. (7) Use managed services to reduce ops cost. (8) Monitor with cost allocation tags. Balance cost vs reliability (e.g., multi-AZ for critical workloads).

---

**Q6: Design a disaster recovery plan. What are the key steps and how do you test it?**

**A:** Steps: (1) Define RTO/RPO. (2) Backup strategy: frequency, retention, encryption. (3) Replication: sync/async to DR region. (4) Runbooks: failover steps, contacts. (5) Test regularly: DR drill (quarterly). Test: (1) Failover to DR; verify app and data. (2) Failback. (3) Document lessons. (4) Chaos engineering for practice. Automation reduces human error during real DR.

---

#### COMPLEX

**Q7: Design a multi-region database strategy with strong consistency for critical data and eventual consistency for the rest. How do you handle failover and conflict resolution?**

**A:** Critical data (e.g., payments): single primary region; sync replica in DR; automatic failover; RPO near zero, RTO minutes. Non-critical: multi-region with async replication; conflict resolution (last-writer-wins, vector clocks, or CRDTs). Failover: automated for primary; promote replica; update DNS. Conflict: avoid for critical (single writer); for rest, define resolution rules and surface conflicts to users when needed. Use managed DB with multi-region (e.g., Aurora Global DB, Cosmos DB).

---

**Q8: A company runs entirely on a single cloud. What are the risks of vendor lock-in? How would you architect for portability without sacrificing cloud benefits?**

**A:** Risks: price increases, service discontinuation, regional issues, negotiation leverage. Portability: (1) Abstraction layers: Kubernetes, Terraform, interfaces for DB/cache/messaging. (2) Prefer open-source or standards (Postgres, Kafka, S3-compatible). (3) Avoid proprietary features where possible. (4) Multi-cloud for critical workloads (complex, costly). Tradeoff: full portability can limit use of differentiated services. Target: ability to migrate with effort, not zero effort.

---

---

## 10-System Design Cases

### Topic Introduction

System design cases are end-to-end exercises combining multiple concepts. Key cases: URL shortener, rate limiter, chat system, notification system, feed system. Practice applying the framework and making tradeoffs.

---

### Q&A — System Design Cases

#### BASIC

**Q1: Design a URL shortener. What are the main components? How do you generate short codes?**

**A:** Components: API (create, redirect), storage (short → long URL), redirect service. Short codes: (1) Hash (MD5/SHA) + truncate—collision possible, use collision handling. (2) Base62 encode of auto-increment ID—unique, predictable length. (3) Random string—check uniqueness. Storage: key-value (short → long). Redirect: 301 (cached) or 302 (track clicks). Scale: cache hot URLs; DB for persistence.

---

**Q2: Design a rate limiter. What algorithms can you use?**

**A:** Algorithms: (1) Fixed window: count per window; simple, boundary issue. (2) Sliding window: smooth, more accurate. (3) Token bucket: allow bursts. (4) Leaky bucket: smooth output. Storage: in-memory for single node; Redis for distributed. Key: user_id or IP. Implementation: Redis INCR with TTL, or sliding window log. Return 429 with Retry-After.

---

**Q3: What are the main challenges in designing a chat system? How would you approach presence (online/offline)?**

**A:** Challenges: real-time delivery, scaling connections, message ordering, persistence. Presence: (1) Heartbeat from client; server tracks last seen. (2) Distribute presence via pub/sub (Redis, etc.). (3) Offline after N seconds without heartbeat. (4) Consider "typing" and "last seen" as extensions. Scale: connection manager (e.g., WebSocket servers) + message queue + persistence.

---

#### MEDIUM

**Q4: Design a notification system that supports push (mobile), email, and in-app. How do you ensure delivery and handle user preferences?**

**A:** Components: (1) API to trigger notifications. (2) Template engine. (3) Channels: push (FCM/APNS), email (SES/SendGrid), in-app (WebSocket or poll). (4) User preferences store (channels, frequency). (5) Queue for async processing. Delivery: retries, dead-letter, idempotency. Preferences: check before send; respect opt-out and frequency limits. Batch for email to reduce cost.

---

**Q5: Design a feed system (like Twitter's timeline). Discuss fan-out strategies: push vs pull vs hybrid.**

**A:** Push (fan-out on write): on post, write to all followers' feeds. Fast read, slow write; storage cost for popular users. Pull (fan-out on read): on read, fetch from followed users. Fast write, slow read; need to optimize (cache, limit). Hybrid: push for most users; pull for celebrities (many followers). Store: feed table (user_id, post_id, timestamp) for push; post table for pull. Cache hot feeds.

---

#### COMPLEX

**Q6: Design a distributed rate limiter that works across multiple API gateway instances. Consider consistency and performance.**

**A:** Challenge: each instance must enforce global limit. Solution: Redis as shared store. Sliding window: Lua script for atomic INCR + ZREMRANGEBYSCORE + ZADD. Token bucket: store (tokens, last_update) in Redis; Lua for atomic check-and-update. Consistency: Redis is single source of truth; eventual consistency if Redis is clustered. Performance: local cache for "under limit" with short TTL to reduce Redis calls. Consider sliding window log for accuracy.

---

**Q7: Design a real-time collaborative document editor (like Google Docs). Address conflict resolution, presence, and scale.**

**A:** Conflict resolution: (1) OT (Operational Transformation) or (2) CRDTs. CRDTs allow concurrent edits without central coordination. Presence: broadcast cursor/selection via WebSocket; throttle updates. Architecture: (1) Clients send ops to server. (2) Server broadcasts to collaborators. (3) Persist to DB (full doc or op log). (4) Scale WebSocket with multiple servers + pub/sub (Redis). (5) Load document on connect; apply missed ops. Consider Yjs, Automerge for CRDT impl.

---

**Q8: Design a system to detect and prevent fraudulent transactions in real-time. 100M transactions/day, <100ms decision latency. What's your approach?**

**A:** Flow: (1) Transaction → API. (2) Extract features (amount, merchant, user history, velocity, etc.). (3) Rule engine: fast, deterministic rules (e.g., amount > X, new merchant). (4) ML model: score for risk (pre-computed features, low-latency model). (5) Decision: allow, deny, manual review. Latency: cache user/merchant features; async enrich where possible; model in-memory or low-latency service. Scale: shard by user_id; use stream processing for feature aggregation. Storage: feature store; transaction log for feedback loop.

---

---

## 11-Interview Playbook

### Topic Introduction

The playbook covers how to approach system design interviews: structured framework, common interviewer questions, tradeoff patterns, and red flags to avoid. Practice the process, not just the content.

---

### Q&A — Interview Playbook

#### BASIC

**Q1: What is a good framework for tackling a system design interview?**

**A:** (1) Clarify requirements: functional, non-functional, scale. (2) Estimate: QPS, storage, bandwidth (back of envelope). (3) High-level design: core components, data flow. (4) Deep dive: drill into 2–3 areas (e.g., DB, API). (5) Identify bottlenecks and scaling. (6) Tradeoffs: what we chose and why. Communicate throughout; ask questions; think out loud.

---

**Q2: What are common tradeoffs you should be able to discuss?**

**A:** Consistency vs availability (CAP). Latency vs throughput. Cost vs complexity. Strong consistency vs performance. Sync vs async. Build vs buy. Optimization vs readability. Always state the tradeoff and your reasoning for the choice.

---

**Q3: What are red flags to avoid in system design interviews?**

**A:** (1) Jumping to solution without clarifying. (2) Ignoring scale and numbers. (3) Over-engineering for the problem. (4) Not considering failure modes. (5) One-size-fits-all (e.g., "always use microservices"). (6) Not asking about constraints. (7) Giving up when stuck. Instead: ask, estimate, iterate, acknowledge tradeoffs.

---

#### MEDIUM

**Q4: How do you handle a design question you're unfamiliar with? Walk through your approach.**

**A:** (1) Admit lack of direct experience; relate to similar systems. (2) Ask clarifying questions to narrow scope. (3) Start with first principles: what are the core operations? (4) Use known building blocks (DB, cache, queue). (5) Reason about scale and bottlenecks. (6) Identify what you'd need to learn. Interviewers value reasoning over knowing every system.

---

**Q5: An interviewer asks "how would you scale this to 10x?" What are they probing? How do you answer?**

**A:** They're probing: bottleneck identification, scaling strategies, awareness of limits. Answer: (1) Identify bottleneck (DB? CPU? Network?). (2) Propose scaling (horizontal, cache, async). (3) Check for new bottlenecks. (4) Consider cost and operational complexity. (5) Mention monitoring to validate. Be specific: "shard by user_id" not "add more servers."

---

**Q6: How do you demonstrate senior-level thinking in a system design interview?**

**A:** (1) Consider tradeoffs explicitly. (2) Discuss failure modes and resilience. (3) Address operational concerns (deployment, monitoring, DR). (4) Think about evolution and migration. (5) Ask about business context to inform design. (6) Acknowledge uncertainty and alternatives. (7) Consider security and compliance. Show judgment, not just knowledge.

---

#### COMPLEX

**Q7: Design a system in 45 minutes. The interviewer keeps adding requirements. How do you manage scope and demonstrate progress?**

**A:** (1) Prioritize: nail core flow first. (2) Park extras: "Good point; I'll add that after we lock the core." (3) Time-box deep dives. (4) Use a two-pass approach: breadth first, then depth. (5) Summarize what's done and what's next. (6) If overwhelmed, propose: "We've covered X and Y; should we go deeper on X or add Z?" Interviewer may be testing prioritization and composure.

---

**Q8: You're asked to critique your own design. What do you look for? Give a structured approach.**

**A:** (1) Single points of failure—did we add redundancy? (2) Scalability bottlenecks—what breaks at 10x? (3) Consistency—did we address it? (4) Security—auth, encryption, injection? (5) Operational complexity—can we run this? (6) Cost—is it reasonable? (7) Alternative approaches—what did we not choose and why? (8) Migration—how do we get from current state? Structured self-critique shows maturity.

---

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
