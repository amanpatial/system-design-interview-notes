# Stateless vs Stateful

## Introduction

**Stateless** servers don't store session state; any instance can serve any request. **Stateful** servers hold state; scaling and failover are more complex.

## Definitions

| Type | Definition |
|------|------------|
| **Stateless** | No server-side session; any instance can serve |
| **Stateful** | Server holds session state |

## Q&A

### Basic

**Q: Why is stateless design preferred for scalability?**

**A:** Stateless: any instance can serve any request; no server affinity. Enables: easy horizontal scaling, simple load balancing, no session migration on instance failure. Stateful: need sticky sessions or state replication; complicates scaling and failover. Store state in DB, cache, or client; keep servers stateless.

### Medium

**Q: How do you handle stateful workloads (e.g., WebSocket servers, gaming servers) in a horizontally scaled environment?**

**A:** Options: (1) Sticky sessions: load balancer routes same client to same instance; instance holds state. Risk: instance failure loses state. (2) Externalize state: Redis/DB for session; any instance can serve. (3) Sharding: assign users to instances by user_id; client reconnects to same shard. (4) State replication: replicate to backup (complex). (5) Accept reconnection: design for reconnect and state rebuild. Often: sticky sessions + externalized critical state + graceful shutdown with drain.

---

## See Also

- [Load Balancing](./load-balancing.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
