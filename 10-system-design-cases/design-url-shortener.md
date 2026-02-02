# Design: URL Shortener

## Introduction

A URL shortener converts long URLs to short codes. Key concerns: short code generation, storage, redirect flow, and scale.

## Q&A

### Basic

**Q: Design a URL shortener. What are the main components? How do you generate short codes?**

**A:** Components: API (create, redirect), storage (short → long URL), redirect service. Short codes:

- (1) Hash (MD5/SHA) + truncate—collision possible, use collision handling.
- (2) Base62 encode of auto-increment ID—unique, predictable length.
- (3) Random string—check uniqueness.

Storage: key-value (short → long). Redirect: 301 (cached) or 302 (track clicks). Scale: cache hot URLs; DB for persistence.

---

## See Also

- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
- [02-Data Storage](../02-data-storage/) — storage choices
- [03-Caching](../03-caching/) — caching hot URLs
