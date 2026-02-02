# Encryption at Rest & in Transit

## Introduction

**Encryption at rest** protects stored data. **Encryption in transit** (TLS) protects data on the network. Both are needed for defense in depth.

## Definitions

| Concept | Definition |
|---------|------------|
| **Encryption at rest** | Encrypt stored data |
| **Encryption in transit** | TLS for data in flight |

## Q&A

### Medium

**Q: Explain encryption at rest vs in transit. What happens if you have one but not the other?**

**A:** In transit: TLS; protects from eavesdropping, tampering on the wire. At rest: encrypt data on disk; protects if storage is stolen. Only in transit: data on disk is readable if storage is compromised. Only at rest: data is exposed on the network. Need both for defense in depth.

### Complex

**Q: Design a zero-trust API architecture. Assume no implicit trust based on network position.**

**A:** Principles:

- (1) Verify every request—auth on every call, no "internal" bypass.
- (2) Least privilege—grant minimum access.
- (3) Assume breach—segment, encrypt, audit.

Implementation:

- (1) mTLS or JWT for service-to-service.
- (2) API gateway validates all requests.
- (3) Policy engine (e.g., OPA) for fine-grained AuthZ.
- (4) Encrypt everything; no trusted network.
- (5) Audit logs for all access.
- (6) Short-lived credentials, no long-lived keys.

---

## See Also

- [Secrets Management](./secrets-management.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
