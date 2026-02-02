# Logging

## Introduction

**Logging** records discrete events for debugging, audit, and analysis. Structured logs (e.g., JSON) enable search and correlation.

## Q&A

### Basic

**Q: What is the difference between logging, metrics, and tracing? When would you use each?**

**A:** Logging: event records (errors, info); debug, audit. Metrics: numbers (latency, error rate, QPS); dashboards, alerting. Tracing: request flow across services; performance debugging. Use logs for details; metrics for trends and alerts; tracing for distributed request flow.

### Complex

**Q: A production incident occurs. Walk through your debugging process using logs, metrics, and traces. How do you correlate them?**

**A:**

- (1) Start with metrics: when did latency/errors spike? Which service?
- (2) Traces: find slow or failed traces in that window; identify bottleneck span.
- (3) Logs: filter by trace ID for full context; look for errors.
- (4) Correlate: trace ID in logs and traces; timestamp alignment.
- (5) Dependency: check downstream services in trace.
- (6) Correlate with deployments: time of change.

Use correlated IDs (trace_id, request_id) across all three pillars.

---

## See Also

- [Metrics](./metrics.md)
- [Tracing](./tracing.md)
- [SLIs, SLOs, SLAs](./slis-slos-slas.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
