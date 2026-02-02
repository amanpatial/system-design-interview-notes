# Authentication vs Authorization

## Introduction

**Authentication** verifies identity. **Authorization** verifies permission. Both are needed; they address different questions.

## Definitions

| Concept | Definition |
|---------|------------|
| **Authentication** | Verifying identity (who are you?) |
| **Authorization** | Verifying permission (what can you do?) |

## Q&A

### Basic

**Q: What is the difference between authentication and authorization?**

**A:** Authentication: proving identity (e.g., password, MFA). Authorization: checking permission to perform an action (e.g., can user X delete resource Y?). AuthN first; then AuthZ. Example: login is AuthN; "can this user access /admin" is AuthZ.

---

## See Also

- [OAuth & JWT](./oauth-jwt.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
