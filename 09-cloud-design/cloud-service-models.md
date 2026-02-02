# Cloud Service Models

## Introduction

**IaaS**, **PaaS**, and **SaaS** represent different levels of abstraction. Choice affects control, ops burden, and flexibility.

## Definitions

| Model | Definition |
|-------|------------|
| **IaaS** | Infrastructure (VMs, storage); you manage OS and above |
| **PaaS** | Platform (e.g., app runtime); you manage app only |
| **SaaS** | Software as a service; consume only |

## Q&A

### Basic

**Q: Compare IaaS, PaaS, and SaaS. When would you choose each?**

**A:** IaaS: max control, max ops (e.g., Kubernetes on VMs). PaaS: less ops, less control (e.g., App Engine, Lambda). SaaS: no infra (e.g., Salesforce). Choose IaaS for customization; PaaS for speed and managed runtime; SaaS for non-differentiating functions. Many orgs use mix.

---

## See Also

- [Multi-Region Design](./multi-region-design.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
