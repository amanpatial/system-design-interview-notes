# TOGAF Fundamentals

## Introduction

TOGAF (The Open Group Architecture Framework) is a framework for enterprise architecture that provides an approach for designing, planning, implementing, and governing enterprise information architecture.

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Enterprise Architecture** | Conceptual blueprint that defines structure and operation of an organization |
| **Architecture Development Method (ADM)** | Core of TOGAF; iterative process for developing architectures |
| **Architecture Domains** | Business, Data, Application, Technology |
| **Stakeholder** | Individual, team, or organization with interests/concerns in architecture |
| **Architecture Vision** | High-level aspirational view of target architecture |
| **Building Block** | Component of business capability that can be combined with other building blocks |

---

## Q&A — TOGAF Fundamentals

### Basic

**Q: What is TOGAF and why is it used?**

**A:** TOGAF is The Open Group Architecture Framework, a proven enterprise architecture methodology and framework used by leading organizations to improve business efficiency. It helps:

- Reduce complexity
- Improve alignment between IT and business
- Provide a systematic approach to architecture development
- Enable reuse of architecture assets
- Improve ROI on IT investments

---

**Q: What are the four architecture domains in TOGAF?**

**A:**

- **Business Architecture:** Defines business strategy, governance, organization, and key business processes
- **Data Architecture:** Describes structure of logical and physical data assets and data management resources
- **Application Architecture:** Blueprint for individual applications, their interactions, and relationships to core business processes
- **Technology Architecture:** Describes logical software and hardware capabilities required to support deployment of business, data, and application services

---

**Q: What is the Architecture Development Method (ADM)?**

**A:** The ADM is the core of TOGAF. It's an iterative process model that provides:

- A tested and repeatable process for developing architectures
- Techniques for architecture development
- Guidelines for using the ADM within an organization

The ADM consists of phases: Preliminary, A-H (Vision through Change Management), and Requirements Management.

---

### Medium

**Q: Explain the relationship between Architecture Content Framework, Enterprise Continuum, and ADM.**

**A:**

- **ADM:** The process/method for developing architectures
- **Architecture Content Framework:** Structured model for architectural work products (deliverables, artifacts, building blocks)
- **Enterprise Continuum:** Classification system and repository for architecture assets (generic to organization-specific)

Relationship: ADM uses the Content Framework to create work products, which are stored and classified in the Enterprise Continuum for reuse.

---

**Q: What is the difference between Architecture Building Blocks (ABBs) and Solution Building Blocks (SBBs)?**

**A:**

**ABBs (Architecture Building Blocks):**
- Define required capability
- Capture architecture requirements
- Vendor-neutral
- Specification-focused

**SBBs (Solution Building Blocks):**
- Define implementation
- Vendor-specific products/components
- Implementation-focused
- More detailed than ABBs

Example: ABB = "Authentication Service"; SBB = "Okta SSO Implementation"

---

**Q: How does TOGAF support stakeholder management?**

**A:** TOGAF provides structured stakeholder management through:

- **Stakeholder Map:** Identifies all stakeholders
- **Power/Interest Grid:** Classifies stakeholders by power and interest
- **Architecture Vision phase:** Explicit stakeholder identification and concern capture
- **Requirements Management:** Continuous tracking of stakeholder concerns
- **Architecture Contracts:** Formal agreements with stakeholders
- **Communications Plan:** Structured stakeholder engagement

---

### Complex

**Q: An organization has both legacy mainframe systems and modern cloud applications. How would you use TOGAF to plan a transformation while maintaining business continuity?**

**A:** Approach:

- **Phase A (Vision):** Define transformation scope; identify critical legacy dependencies; establish business continuity as key constraint
- **Phase B-D (Architecture):**
  - Baseline Architecture: Document current mainframe dependencies and integration points
  - Target Architecture: Cloud-native with defined migration path
  - Gap Analysis: Identify coexistence requirements
- **Phase E (Opportunities):** Incremental migration work packages; strangler pattern; parallel run capabilities
- **Phase F (Migration Planning):** Phased approach with rollback plans; prioritize by business criticality
- **Phase G (Implementation Governance):** Stage gates with business continuity validation
- **Phase H (Change Management):** Monitor both environments; establish sunset criteria

Key: Use Transition Architectures (intermediate states) to show coexistence of mainframe and cloud.

---

**Q: How would you tailor TOGAF ADM for an agile enterprise with rapid delivery cycles?**

**A:** Tailoring approach:

- **Iteration Cycles:** Shorter ADM iterations (weeks, not months); align with agile release cycles
- **Phase Compression:** Combine phases where appropriate (B-C-D can be iterative sprints)
- **Lightweight Deliverables:** Replace heavy documentation with architecture decision records, diagrams, and wikis
- **Continuous Requirements:** Requirements Management runs as continuous backlog refinement
- **Architecture Board:** Embedded architects in agile teams; lightweight architecture reviews
- **Incremental Governance:** Automated compliance checks; architecture fitness functions
- **Just-Enough Design:** Focus on critical decisions; defer low-risk details

Balance: Maintain architectural coherence while enabling team autonomy.

---

**Q: Compare TOGAF with Zachman Framework. When would you use each?**

**A:**

**TOGAF:**
- Process-oriented (how to develop architecture)
- ADM provides methodology
- Practical implementation focus
- Strong governance and migration planning
- Use when: Need end-to-end transformation methodology; want proven process; need stakeholder management

**Zachman:**
- Structure-oriented (what to document)
- Classification scheme (6x6 matrix)
- Comprehensive documentation focus
- No prescribed process
- Use when: Need complete architectural taxonomy; want classification system; focus on completeness over process

**Combined Approach:** Use Zachman for organizing artifacts; use TOGAF ADM for development process. Many enterprises use both.

---

## See Also

- [ADM Phases](./adm-phases.md)
- [Architecture Content Framework](./architecture-content-framework.md)
- [INTERVIEW-BASE.md](../INTERVIEW-BASE.md)
