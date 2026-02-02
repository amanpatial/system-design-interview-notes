# Retries & Timeouts

## Introduction

**Retries** handle transient failures. **Timeouts** prevent hanging on slow or unresponsive services. Exponential backoff and jitter make retries safer.

## Definition

| Concept | Definition |
|---------|------------|
| **Retry** | Retry failed requests; use backoff to avoid overload |

## Q&A

### Basic

**Q: Why use exponential backoff for retries? What about jitter?**

**A:** Exponential backoff: wait longer after each retry (e.g., 1s, 2s, 4s). Gives failing service time to recover; avoids thundering herd. Jitter: add randomness to delay. Prevents synchronized retries from many clients that could cause spikes. Use both for robust retries.

### Medium

**Q: Design retry logic for an API client. Consider: idempotency, max retries, backoff, and when not to retry.**

**A:** Retry on: timeouts, 5xx, network errors. Don't retry on: 4xx (except 429), non-idempotent operations without idempotency key. Config: max 3–5 retries, exponential backoff (base 1s, max 30s), jitter. Use idempotency keys for POST/PUT. Implement: retry with exponential backoff + jitter; respect Retry-After if present (429, 503).

---

## See Also

- [Circuit Breaker](./circuit-breaker.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
