# Red Flags to Avoid

## Introduction

Avoid common mistakes that signal lack of experience or poor process.

## Q&A

### Basic

**Q: What are red flags to avoid in system design interviews?**

**A:** (1) Jumping to solution without clarifying. (2) Ignoring scale and numbers. (3) Over-engineering for the problem. (4) Not considering failure modes. (5) One-size-fits-all (e.g., "always use microservices"). (6) Not asking about constraints. (7) Giving up when stuck. Instead: ask, estimate, iterate, acknowledge tradeoffs.

### Complex

**Q: You're asked to critique your own design. What do you look for? Give a structured approach.**

**A:** (1) Single points of failure—did we add redundancy? (2) Scalability bottlenecks—what breaks at 10x? (3) Consistency—did we address it? (4) Security—auth, encryption, injection? (5) Operational complexity—can we run this? (6) Cost—is it reasonable? (7) Alternative approaches—what did we not choose and why? (8) Migration—how do we get from current state? Structured self-critique shows maturity.

---

## See Also

- [System Design Framework](./system-design-framework.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
