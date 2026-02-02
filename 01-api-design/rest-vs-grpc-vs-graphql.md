# REST vs gRPC vs GraphQL

## Introduction

Different API styles suit different use cases. REST, gRPC, and GraphQL each have distinct tradeoffs for public APIs, microservices, and client needs.

## Definitions

| Style | Definition |
|-------|------------|
| **REST** | Resource-oriented, HTTP verbs, stateless, JSON/XML |
| **gRPC** | RPC over HTTP/2, binary (Protobuf), streaming, low latency |
| **GraphQL** | Query language; client specifies needed fields; single endpoint |

## Q&A

### Basic

**Q: When would you choose REST over gRPC, and vice versa?**

**A:** Choose REST when:

- Public APIs, browser clients, wide tooling support, human-readable payloads, CRUD-heavy.

Choose gRPC when:

- Microservice-to-microservice, performance-critical, need streaming (bidirectional), strong typing with code generation, mobile/low-bandwidth (binary).

GraphQL when clients need flexible querying and you want to avoid over/under-fetching.

### Medium

**Q: Explain the tradeoffs between REST, gRPC, and GraphQL for a B2B platform with 50+ integrating partners.**

**A:** REST: partners expect it, easy onboarding, wide SDK support; risk of over-fetching and version sprawl.

gRPC: great for internal services; many partners lack gRPC tooling; consider gRPC-Web or REST gateway.

GraphQL: flexible queries reduce over-fetching; schema evolution is easier; but exposes more surface, requires auth/rate limit at query level, and some partners prefer REST.

Recommendation: offer REST for public API (adoption), GraphQL as optional for power users; use gRPC internally.

### Complex

**Q7: Design an API gateway that handles versioning, rate limiting, authentication, and routing for 100+ microservices. What components and data flows would you use?**

**A:** Components:

- (1) Gateway (Kong, AWS API Gateway, Envoy)—single entry, routing, middleware.
- (2) Auth: validate JWT/OAuth; optionally call auth service.
- (3) Rate limiting: Redis-backed, per API key + endpoint.
- (4) Version routing: path/header → service version; maintain mapping.
- (5) Service discovery: route to healthy instances.

Flow: Request → TLS termination → Auth → Rate limit check → Version resolution → Route to backend → Response (aggregate, transform if needed). Consider: caching at gateway, circuit breaker for backends, request/response logging for audit.

**Q8: How would you evolve an existing REST API to GraphQL without breaking existing clients? Describe migration strategy and compatibility concerns.**

**A:** Strategy:

- (1) Add GraphQL endpoint alongside REST (`/graphql`).
- (2) Build GraphQL schema that mirrors REST resources; resolvers call existing REST services or shared logic.
- (3) Run both in parallel; new clients use GraphQL.
- (4) Deprecate REST endpoints gradually with long notice.

Compatibility: shared auth, rate limits, and SLAs. Ensure GraphQL doesn't create N+1 or expensive queries—implement query complexity analysis, depth limits, and pagination. Use schema stitching if services expose their own GraphQL. Consider Apollo Federation for microservice GraphQL.

---

## See Also

- [Idempotency](./idempotency.md)
- [API Versioning](./api-versioning.md)
- [Rate Limiting](./rate-limiting.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
