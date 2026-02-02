# Eviction Policies

## Introduction

Eviction policies decide what to remove when the cache is full. LRU, LFU, and TTL each suit different access patterns.

## Definition

| Concept | Definition |
|---------|------------|
| **Eviction** | LRU, LFU, TTL—deciding what to remove when full |

## Q&A

### Basic

**Q: Compare LRU vs LFU eviction. Which is better for a news feed cache?**

**A:** LRU: evicts least recently used. Good for temporal locality. LFU: evicts least frequently used. Good for popularity. News feed: mix of trending (high frequency) and new (recent). LRU can evict popular older items; LFU can hold old popular items and evict new hot items. Consider: LRU with TTL for freshness, or hybrid (e.g., TinyLFU, W-TinyLFU) that considers both recency and frequency.

### Complex

**Q: A cache has 90% hit rate but still high DB load. Diagnose and propose solutions.**

**A:** Possible causes:

- (1) 10% miss handling high traffic—even 1% of large traffic is big.
- (2) Popular keys evicted—hot keys not fitting in cache.
- (3) Cache key design—too specific, low reuse (e.g., per-user keys for shared data).
- (4) Thundering herd on miss.
- (5) Expensive queries on miss—single miss triggers heavy query.

Solutions:

- (1) Increase cache size or optimize eviction for hot keys.
- (2) Cache at coarser granularity where possible.
- (3) Request coalescing, lock, or stale-while-revalidate.
- (4) Pre-warm cache for known hot keys.
- (5) Optimize DB queries and add indexes.
- (6) Add read replicas for cache miss traffic.

---

## See Also

- [Cache-Aside](./cache-aside.md)
- [Cache Hit/Miss](./cache-hit-miss.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
