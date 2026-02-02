# Metrics

## Introduction

**Metrics** are numerical measurements over time—latency, error rate, QPS. Used for dashboards, alerting, and capacity planning.

## Q&A

### Medium

**Q: Design a monitoring strategy for a microservices architecture. What do you measure, and how do you avoid alert fatigue?**

**A:** Measure: RED (Rate, Errors, Duration) per service; dependency health; queue depth; resource utilization. Avoid fatigue:

- (1) Few high-signal alerts—page only for user impact.
- (2) Tiered: critical (page), warning (ticket), info (dashboard).
- (3) Runbooks for every alert.
- (4) Avoid alerting on symptoms; alert on causes or user impact.
- (5) SLO-based alerting: burn rate, error budget.

### Complex

**Q: Design an observability stack for 50+ microservices: logging, metrics, tracing. Address scale, cost, and retention.**

**A:** Logging: centralized (ELK, Loki); ship from agents or sidecar; structure logs (JSON); sample at high volume (e.g., 10% of success, 100% of errors); retention 7–30 days; archive to cold storage.

Metrics: Prometheus or vendor; scrape or push; aggregate (recording rules); retention 15–90 days; downsampling for long retention.

Tracing: OTel collectors; sample (e.g., 1% or tail-based on errors); store in Jaeger/Tempo; retention 7 days.

Cost: sampling, retention policies, tiered storage.

---

## See Also

- [Logging](./logging.md)
- [Tracing](./tracing.md)
- [SLIs, SLOs, SLAs](./slis-slos-slas.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
