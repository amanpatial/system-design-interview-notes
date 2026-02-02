# API Versioning

## Introduction

API versioning manages breaking changes over time while supporting existing clients. Different strategies balance clarity, tooling, and evolution.

## Q&A

### Basic

**Q: What are common API versioning strategies? What are their tradeoffs?**

**A:**

- (1) URL path: `/v1/users`—clear, cacheable; requires new routes.
- (2) Query param: `/users?version=1`—optional; messy for many versions.
- (3) Header: `Accept: application/vnd.api.v1+json`—clean URLs; less discoverable.
- (4) No versioning, backward-compatible changes—simplest but limits evolution.

For public APIs, path versioning is common; for internal, headers or backward compatibility often suffice.

---

## See Also

- [REST vs gRPC vs GraphQL](./rest-vs-grpc-vs-graphql.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
