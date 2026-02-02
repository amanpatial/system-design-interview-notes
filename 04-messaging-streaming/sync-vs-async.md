# Sync vs Async

## Introduction

**Synchronous** communication blocks until a response; **asynchronous** allows fire-and-forget or callback. Choice affects coupling, scalability, and resilience.

## Definitions

| Type | Definition |
|------|------------|
| **Sync** | Caller waits for response; tight coupling |
| **Async** | Fire-and-forget or callback; loose coupling |

## Q&A

### Basic

**Q: When would you use sync vs async communication between services?**

**A:** Sync when: need immediate response (e.g., auth check, fetch user), simple request-response, client must have result to continue. Async when: fire-and-forget (notifications), long-running work, decoupling (producer doesn't need to know consumers), reliability (queue buffers if consumer is down). Prefer async for scalability and resilience; use sync only when necessary.

---

## See Also

- [Message Queues](./message-queues.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
