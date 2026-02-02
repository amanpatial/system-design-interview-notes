# Design: Notification System

## Introduction

A notification system delivers push, email, and in-app messages. Key concerns: delivery reliability, user preferences, and channel integration.

## Q&A

### Medium

**Q: Design a notification system that supports push (mobile), email, and in-app. How do you ensure delivery and handle user preferences?**

**A:** Components: (1) API to trigger notifications. (2) Template engine. (3) Channels: push (FCM/APNS), email (SES/SendGrid), in-app (WebSocket or poll). (4) User preferences store (channels, frequency). (5) Queue for async processing. Delivery: retries, dead-letter, idempotency. Preferences: check before send; respect opt-out and frequency limits. Batch for email to reduce cost.

---

## See Also

- [04-Messaging & Streaming](../04-messaging-streaming/)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
