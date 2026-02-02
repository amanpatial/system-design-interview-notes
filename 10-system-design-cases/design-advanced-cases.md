# Design: Advanced Cases

## Introduction

Advanced system design cases: collaborative document editor, real-time fraud detection. These combine multiple concepts and require deeper analysis.

## Q&A

### Complex

**Q: Design a real-time collaborative document editor (like Google Docs). Address conflict resolution, presence, and scale.**

**A:** Conflict resolution: (1) OT (Operational Transformation) or (2) CRDTs. CRDTs allow concurrent edits without central coordination. Presence: broadcast cursor/selection via WebSocket; throttle updates. Architecture:

- (1) Clients send ops to server.
- (2) Server broadcasts to collaborators.
- (3) Persist to DB (full doc or op log).
- (4) Scale WebSocket with multiple servers + pub/sub (Redis).
- (5) Load document on connect; apply missed ops.

Consider Yjs, Automerge for CRDT impl.

**Q: Design a system to detect and prevent fraudulent transactions in real-time. 100M transactions/day, <100ms decision latency. What's your approach?**

**A:** Flow:

- (1) Transaction → API.
- (2) Extract features (amount, merchant, user history, velocity, etc.).
- (3) Rule engine: fast, deterministic rules (e.g., amount > X, new merchant).
- (4) ML model: score for risk (pre-computed features, low-latency model).
- (5) Decision: allow, deny, manual review.

Latency: cache user/merchant features; async enrich where possible; model in-memory or low-latency service. Scale: shard by user_id; use stream processing for feature aggregation. Storage: feature store; transaction log for feedback loop.

---

## See Also

- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
