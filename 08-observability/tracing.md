# Tracing

## Introduction

**Distributed tracing** tracks request flow across services. Trace IDs and spans show latency and dependencies end-to-end.

## Q&A

### Medium

**Q: How does distributed tracing work? What must be propagated across service boundaries?**

**A:** Tracing: assign trace ID to request; each service creates spans (operation, duration); spans have parent-child relationship. Propagate: trace ID, span ID, parent span ID (e.g., via headers). Backend aggregates spans by trace ID for full picture. Standards: OpenTelemetry, Zipkin, Jaeger. Enables finding latency bottlenecks across services.

---

## See Also

- [Logging](./logging.md)
- [Metrics](./metrics.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
