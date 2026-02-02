# Design: Chat System

## Introduction

A chat system requires real-time delivery, scaling connections, message ordering, and persistence. Presence (online/offline) adds complexity.

## Q&A

### Basic

**Q: What are the main challenges in designing a chat system? How would you approach presence (online/offline)?**

**A:** Challenges: real-time delivery, scaling connections, message ordering, persistence. Presence:

- (1) Heartbeat from client; server tracks last seen.
- (2) Distribute presence via pub/sub (Redis, etc.).
- (3) Offline after N seconds without heartbeat.
- (4) Consider "typing" and "last seen" as extensions.

Scale: connection manager (e.g., WebSocket servers) + message queue + persistence.

---

## See Also

- [04-Messaging & Streaming](../04-messaging-streaming/)
- [05-Scalability / Stateless vs Stateful](../05-scalability-patterns/stateless-vs-stateful.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
