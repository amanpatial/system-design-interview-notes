# Load Balancing

## Introduction

**Load balancers** distribute traffic across instances. L4 (transport) vs L7 (application) and algorithms (round-robin, least connections, consistent hashing) suit different needs.

## Definition

| Concept | Definition |
|---------|------------|
| **Load Balancer** | Distribute traffic across instances |

## Q&A

### Basic

**Q: Explain L4 vs L7 load balancing. When would you use each?**

**A:** L4 (transport): IP + port; no awareness of HTTP. Fast, low overhead; can't route by path, header, or content. L7 (application): HTTP-aware; route by URL, header, cookie. Enables canary, A/B, path-based routing. Use L4 for raw throughput (e.g., TCP); L7 when you need content-based routing, SSL termination, or HTTP features.

### Medium

**Q: Compare round-robin, least connections, and consistent hashing for load balancing. When is each appropriate?**

**A:** Round-robin: rotate evenly. Simple; ignores actual load. Least connections: send to instance with fewest active connections. Better for varying request duration. Consistent hashing: same key always to same instance (or small set). Good for caching, session affinity. Use round-robin for similar requests; least connections for mixed durations; consistent hashing when locality matters.

### Complex

**Q: A load balancer is a single point of failure. How do you make it highly available?**

**A:** (1) Active-passive: standby LB; failover via health checks (e.g., VRRP, keepalived). (2) Active-active: multiple LBs; DNS round-robin or anycast; each can handle full load. (3) Cloud LB: use managed service (ALB, ELB) with multiple AZs. (4) DNS failover: multiple LB IPs; health-based DNS. (5) Eliminate LB: client-side load balancing (service mesh, client knows all endpoints). Tradeoff: complexity vs availability.

---

## See Also

- [Horizontal vs Vertical Scaling](./horizontal-vs-vertical-scaling.md)
- [Stateless vs Stateful](./stateless-vs-stateful.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
