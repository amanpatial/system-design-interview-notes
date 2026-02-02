# Cost Optimization

## Introduction

Cloud cost optimization balances spend with reliability and performance. Right-sizing, reserved instances, autoscaling, and storage tiers are key levers.

## Q&A

### Medium

**Q: How do you optimize cloud costs without sacrificing reliability?**

**A:** (1) Right-size: match instance to workload; use metrics. (2) Reserved/savings plans for steady workload. (3) Spot for fault-tolerant, interruptible workload. (4) Auto-scale: scale down when idle. (5) Storage tiers: hot/warm/cold. (6) Delete unused resources. (7) Use managed services to reduce ops cost. (8) Monitor with cost allocation tags. Balance cost vs reliability (e.g., multi-AZ for critical workloads).

### Complex

**Q: A company runs entirely on a single cloud. What are the risks of vendor lock-in? How would you architect for portability without sacrificing cloud benefits?**

**A:** Risks: price increases, service discontinuation, regional issues, negotiation leverage. Portability: (1) Abstraction layers: Kubernetes, Terraform, interfaces for DB/cache/messaging. (2) Prefer open-source or standards (Postgres, Kafka, S3-compatible). (3) Avoid proprietary features where possible. (4) Multi-cloud for critical workloads (complex, costly). Tradeoff: full portability can limit use of differentiated services. Target: ability to migrate with effort, not zero effort.

---

## See Also

- [Multi-Region Design](./multi-region-design.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
