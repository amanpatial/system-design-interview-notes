# Idempotency

## Introduction

**Idempotency** means performing the same operation multiple times produces the same result as performing it once. Critical for safe retries and duplicate handling.

## Definition

| Concept | Definition |
|---------|------------|
| **Idempotency** | Same request multiple times = same effect as once |

## Q&A

### Basic

**Q: What is idempotency and why does it matter for APIs?**

**A:** Idempotency means repeating the same request produces the same result as executing it once. Critical for:

- Retries (network failures, timeouts).
- Duplicate submissions (user double-clicks).
- Exactly-once processing.

Implement via idempotency keys: client sends unique key; server stores key with result; duplicate requests return cached result. Essential for payment and order APIs.

### Medium

**Q: How would you design an API that supports both synchronous and asynchronous processing? When would a client use each?**

**A:** Sync: immediate response (e.g., GET, simple POST). Async: return 202 Accepted with `Location` header to poll for result, or use webhooks/callbacks.

Use sync for: fast operations (< few seconds), simple CRUD.

Use async for: long-running jobs (report generation, bulk imports), resource-intensive ops.

Design: POST creates job → 202 + job ID; GET /jobs/{id} returns status; optionally webhook on completion. Client chooses based on operation type and UX requirements. Ensure async operations are idempotent when retried.

---

## See Also

- [REST vs gRPC vs GraphQL](./rest-vs-grpc-vs-graphql.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
