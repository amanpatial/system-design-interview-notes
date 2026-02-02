# Secrets Management

## Introduction

**Secrets** (passwords, API keys, certs) must be stored and injected securely. Secret managers provide rotation, audit, and least-privilege access.

## Q&A

### Medium

**Q: How do you manage secrets (DB passwords, API keys) in a cloud deployment? What are the pitfalls?**

**A:** Use secret manager (AWS Secrets Manager, Vault, GCP Secret Manager). Inject at runtime (env vars, sidecar) or fetch on startup. Pitfalls:

- (1) Don't commit to git.
- (2) Rotate regularly; automate rotation.
- (3) Least privilege—apps get only what they need.
- (4) Audit access.
- (5) Encrypt at rest.
- (6) Avoid long-lived credentials; use IAM roles where possible.

---

## See Also

- [Encryption at Rest & in Transit](./encryption-at-rest-in-transit.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
