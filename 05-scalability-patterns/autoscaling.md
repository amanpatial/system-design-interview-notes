# Autoscaling

## Introduction

**Autoscaling** adjusts capacity based on load. Metrics, thresholds, and cooldowns must be tuned to avoid flapping and overspend.

## Q&A

### Medium

**Q: Design autoscaling for a web API. What metrics would you use? How do you avoid flapping?**

**A:** Metrics: CPU, request rate, latency (p99), queue depth. Scale up: high CPU or latency, or queue building. Scale down: low CPU and latency. Flapping: scale up/down repeatedly. Avoid:

- (1) Cooldown period after scale action.
- (2) Different thresholds for scale-up vs scale-down (hysteresis).
- (3) Scale-down more slowly than scale-up.
- (4) Use multiple metrics (e.g., scale up if CPU > 70% for 3 min; scale down if CPU < 30% for 10 min).

---

## See Also

- [Horizontal vs Vertical Scaling](./horizontal-vs-vertical-scaling.md)
- [Load Balancing](./load-balancing.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
