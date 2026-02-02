# OAuth & JWT

## Introduction

**OAuth 2.0** is a delegation protocol for authorization. **JWT** (JSON Web Token) is a stateless, signed token format. Together they support APIs, SSO, and mobile apps.

## Definitions

| Concept | Definition |
|---------|------------|
| **OAuth 2.0** | Delegation protocol for authorization |
| **JWT** | Stateless token with claims; signed |

## Q&A

### Basic

**Q: When would you use JWT vs session cookies?**

**A:** JWT: stateless, good for APIs, microservices, cross-domain; can't easily revoke before expiry. Session: stateful server; easy revocation; simpler for traditional web apps. Use JWT for: API-to-API, mobile, stateless scaling. Use sessions for: web apps with easy logout, when revocation is critical.

**Q: Explain OAuth 2.0 authorization code flow. Why use authorization code instead of returning tokens directly?**

**A:** Flow:

- (1) User redirected to auth server.
- (2) User logs in, approves.
- (3) Auth server redirects back with authorization code (not token).
- (4) Client exchanges code for token server-side.

Why: code is short-lived, used once; tokens never sent in URL (visible in history, Referer). Safer than implicit flow where token is in redirect URL.

### Medium

**Q: Design an API authentication strategy for: web app, mobile app, and third-party partners. Each has different requirements.**

**A:** Web app: session cookies (HttpOnly, Secure) or short-lived JWT with refresh token. Mobile: JWT or OAuth; store tokens securely (keychain/keystore); use refresh tokens. Third-party: OAuth 2.0 client credentials or API keys; rate limit per key; rotate keys. Use same auth service; different flows per client type. Validate tokens at API gateway.

### Complex

**Q: A JWT is compromised. How do you revoke it before expiry? Design a solution that scales.**

**A:** JWTs are stateless; server doesn't track them. Options:

- (1) Short expiry (e.g., 15 min) + refresh token (stored, revocable).
- (2) Token blocklist: store revoked token IDs in Redis; check on each request. Doesn't scale for many revocations.
- (3) Version/epoch: include version in JWT; revoke by bumping version; all old tokens invalid.
- (4) Short-lived + sliding refresh: compromise has limited window.

Best: short-lived JWT + revocable refresh token; for critical actions, re-auth or check blocklist.

---

## See Also

- [Authentication vs Authorization](./authentication-vs-authorization.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
