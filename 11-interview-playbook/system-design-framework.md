# System Design Framework

## Introduction

A structured approach for tackling system design interviews. Clarify, estimate, design, deep dive, and discuss tradeoffs.

## Q&A

### Basic

**Q: What is a good framework for tackling a system design interview?**

**A:**

- (1) Clarify requirements: functional, non-functional, scale.
- (2) Estimate: QPS, storage, bandwidth (back of envelope).
- (3) High-level design: core components, data flow.
- (4) Deep dive: drill into 2–3 areas (e.g., DB, API).
- (5) Identify bottlenecks and scaling.
- (6) Tradeoffs: what we chose and why.

Communicate throughout; ask questions; think out loud.

### Complex

**Q: Design a system in 45 minutes. The interviewer keeps adding requirements. How do you manage scope and demonstrate progress?**

**A:**

- (1) Prioritize: nail core flow first.
- (2) Park extras: "Good point; I'll add that after we lock the core."
- (3) Time-box deep dives.
- (4) Use a two-pass approach: breadth first, then depth.
- (5) Summarize what's done and what's next.
- (6) If overwhelmed, propose: "We've covered X and Y; should we go deeper on X or add Z?"

Interviewer may be testing prioritization and composure.

---

## See Also

- [Common Interviewer Questions](./common-interviewer-questions.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
