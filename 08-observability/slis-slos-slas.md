# SLIs, SLOs & SLAs

## Introduction

**SLI** (Service Level Indicator) is what we measure. **SLO** (Service Level Objective) is the target. **SLA** (Service Level Agreement) is the contract with consequences.

## Definitions

| Concept | Definition |
|---------|------------|
| **SLI** | Service Level Indicator (what we measure) |
| **SLO** | Service Level Objective (target we aim for) |
| **SLA** | Service Level Agreement (contract with consequences) |

## Q&A

### Basic

**Q: Define SLI, SLO, and SLA. How are they related?**

**A:** SLI: measurable indicator (e.g., availability = successful requests / total). SLO: target (e.g., 99.9% availability). SLA: business contract with penalties (e.g., credits if < 99.9%). SLO is internal target; SLA is external promise. SLO often stricter than SLA to allow buffer.

**Q: What makes a good SLI?**

**A:** Good SLI:

- (1) Reflects user experience (e.g., latency as perceived by user).
- (2) Measurable automatically.
- (3) Actionable—we can improve it.
- (4) Aligned with business.

Examples: availability (successful requests), latency (p99), error rate. Avoid vanity metrics that don't reflect user impact.

### Medium

**Q: Explain error budget. How do you use it for release decisions?**

**A:** Error budget: 1 - SLO (e.g., 99.9% availability = 0.1% budget = ~43 min downtime/month). Consumed by incidents. Use:

- (1) If budget exhausted, freeze risky releases until budget resets.
- (2) Prioritize reliability work when budget is low.
- (3) Allow calculated risk: small releases consume little budget.

Balances reliability and velocity.

---

## See Also

- [Metrics](./metrics.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
