# Cache-Aside

## Introduction

**Cache-aside** (lazy loading) is the most common caching pattern. The application manages the cache: on miss, it loads from the database and populates the cache.

## Definition

| Concept | Definition |
|---------|------------|
| **Cache-Aside** | App manages cache; on miss, load from DB and populate cache |

## Q&A

### Basic

**Q: Explain cache-aside vs read-through. When would you use each?**

**A:** Cache-aside: application checks cache; on miss, loads from DB and populates cache. Gives app full control. Read-through: cache layer loads from DB on miss; app only talks to cache. Simpler for app; cache must integrate with DB. Use cache-aside when using generic cache (Redis, Memcached). Use read-through when cache is built into storage (e.g., DAX for DynamoDB) or you want app simplicity.

### Medium

**Q: Design a caching strategy for an e-commerce product catalog. Products change occasionally; some are popular. Handle cache invalidation.**

**A:** Cache product by ID. Invalidation:

- (1) TTL (e.g., 1 hr) for eventual consistency.
- (2) Event-driven: on product update, publish event; cache layer invalidates or updates.
- (3) Version/ETag: cache stores version; on update, version changes; conditional fetch.
- (4) Categories/listing: invalidate category cache when product in category changes.

Use cache-aside with Redis. For popular products: longer TTL or pre-warm. Consider CDN for static product images.

**Q: How do you prevent cache stampede (thundering herd) when a popular key expires?**

**A:** Stampede: many requests miss simultaneously, all hit DB. Solutions:

- (1) Probabilistic early expiration: before TTL, with low probability refresh in background.
- (2) Lock/mutex: first request acquires lock, loads, others wait or get stale.
- (3) Request coalescing: single in-flight load per key; others wait for result.
- (4) Stale-while-revalidate: serve stale, refresh async.
- (5) Random jitter on TTL to spread expirations.

Implement with Redis SETNX for locking or use libraries (e.g., cache-aside with coalescing).

### Complex

**Q: Design a multi-layer cache (L1 in-process, L2 Redis) for a high-throughput API. When does data go to each layer? How do you handle invalidation across layers?**

**A:** L1 (in-process): hottest keys, nanosecond access, limited size (e.g., 10K keys). L2 (Redis): broader set, millisecond access, larger. Flow: read from L1 → miss → L2 → miss → DB. Write: invalidate or update both layers. Invalidation:

- (1) Pub/Sub: on write, publish invalidation; all app nodes subscribed, clear L1.
- (2) TTL: both layers have TTL; L1 shorter than L2 to avoid long staleness.
- (3) Version in key: new version = new key; old expires.

Challenge: ensuring all nodes get invalidation; Redis Pub/Sub or broadcast. Consider cache stampede at L2; use coalescing.

---

## See Also

- [Read-Through Cache](./read-through-cache.md)
- [Eviction Policies](./eviction-policies.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
