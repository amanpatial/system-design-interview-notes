# SQL vs NoSQL

## Introduction

Database selection hinges on access patterns, consistency requirements, and scale. SQL and NoSQL each excel in different scenarios.

## Definitions

| Type | Definition |
|------|------------|
| **SQL** | Relational, ACID, structured schema, joins |
| **NoSQL** | Document, key-value, wide-column, graph; flexible schema |

## Q&A

### Basic

**Q: When would you choose SQL over NoSQL, and vice versa?**

**A:** SQL when: complex queries, joins, transactions, strong consistency, relational data (orders, users, inventory). NoSQL when: flexible schema, high write throughput, horizontal scaling, specific access patterns (key-value lookup, document by ID, graph traversals). Choose based on access patterns and consistency requirements, not hype.

---

## See Also

- [Consistency Models](./consistency-models.md)
- [Partitioning vs Sharding](./partitioning-vs-sharding.md)
- [Replication Strategies](./replication-strategies.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
