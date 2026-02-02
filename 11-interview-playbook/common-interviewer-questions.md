# Common Interviewer Questions

## Introduction

Interviewers probe different aspects: unfamiliar problems, scaling, senior thinking. Practice handling each.

## Q&A

### Medium

**Q: How do you handle a design question you're unfamiliar with? Walk through your approach.**

**A:** (1) Admit lack of direct experience; relate to similar systems. (2) Ask clarifying questions to narrow scope. (3) Start with first principles: what are the core operations? (4) Use known building blocks (DB, cache, queue). (5) Reason about scale and bottlenecks. (6) Identify what you'd need to learn. Interviewers value reasoning over knowing every system.

**Q: An interviewer asks "how would you scale this to 10x?" What are they probing? How do you answer?**

**A:** They're probing: bottleneck identification, scaling strategies, awareness of limits. Answer: (1) Identify bottleneck (DB? CPU? Network?). (2) Propose scaling (horizontal, cache, async). (3) Check for new bottlenecks. (4) Consider cost and operational complexity. (5) Mention monitoring to validate. Be specific: "shard by user_id" not "add more servers."

**Q: How do you demonstrate senior-level thinking in a system design interview?**

**A:** (1) Consider tradeoffs explicitly. (2) Discuss failure modes and resilience. (3) Address operational concerns (deployment, monitoring, DR). (4) Think about evolution and migration. (5) Ask about business context to inform design. (6) Acknowledge uncertainty and alternatives. (7) Consider security and compliance. Show judgment, not just knowledge.

---

## See Also

- [System Design Framework](./system-design-framework.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
