# Architecture Development Method (ADM) Phases

## Introduction

The ADM is TOGAF's core methodology. It's an iterative process for developing enterprise architectures, consisting of a Preliminary phase, 8 main phases (A-H), and continuous Requirements Management.

## ADM Phase Overview

| Phase | Name | Purpose |
|-------|------|---------|
| **Preliminary** | Framework & Principles | Prepare organization for architecture work |
| **A** | Architecture Vision | Define scope, stakeholders, vision |
| **B** | Business Architecture | Develop baseline/target business architecture |
| **C** | Information Systems (Data) | Develop baseline/target data architecture |
| **D** | Information Systems (Application) | Develop baseline/target application architecture |
| **E** | Technology Architecture | Develop baseline/target technology architecture |
| **F** | Opportunities & Solutions | Initial implementation planning |
| **G** | Migration Planning | Detailed migration plan |
| **H** | Architecture Change Management | Manage changes to architecture |
| **Requirements** | Requirements Management | Continuous management of requirements |

---

## Q&A — ADM Phases

### Basic

**Q: What is the purpose of the Preliminary Phase?**

**A:** The Preliminary Phase prepares the organization for successful architecture projects. Key activities:

- Define enterprise and architecture scope
- Establish architecture capability and maturity
- Define architecture principles
- Establish governance framework
- Select and tailor architecture framework
- Define relationships with management frameworks

Output: Architecture framework tailored to organization's needs.

---

**Q: What are the key deliverables of Phase A (Architecture Vision)?**

**A:** Key deliverables:

- **Architecture Vision document:** High-level aspirational view
- **Stakeholder Map Matrix:** Identified stakeholders and concerns
- **Communication Plan:** How to engage stakeholders
- **Statement of Architecture Work:** Defines scope, approach, schedule
- **Architecture Principles:** Refined/confirmed principles
- **Capability Assessment:** Current maturity and gaps

Purpose: Secure stakeholder buy-in and approval to proceed.

---

**Q: What is the difference between Phases B, C, D, and E?**

**A:**

- **Phase B (Business):** Business processes, organizational structure, business capabilities, value streams
- **Phase C (Data):** Data entities, relationships, data management
- **Phase D (Application):** Application portfolio, application interactions, interfaces
- **Phase E (Technology):** Infrastructure, networks, platforms, deployment

All follow same pattern: Baseline → Target → Gap Analysis

---

### Medium

**Q: Explain the relationship between Phase F (Opportunities & Solutions) and Phase G (Migration Planning).**

**A:**

**Phase F:** High-level implementation planning

- Consolidates gap analysis from B-C-D-E
- Groups changes into work packages
- Identifies Transition Architectures (intermediate states)
- Performs cost/benefit analysis
- Assesses risks and dependencies

**Phase G:** Detailed migration roadmap

- Prioritizes projects
- Creates detailed Implementation and Migration Plan
- Establishes migration schedule
- Defines resource requirements
- Creates architecture contracts

Relationship: F defines WHAT to implement; G defines WHEN and HOW in detail.

---

**Q: What is Requirements Management and how does it interact with other ADM phases?**

**A:** Requirements Management is a continuous process that operates throughout all ADM phases.

Purpose:

- Capture requirements at each phase
- Store requirements in repository
- Feed requirements into and out of ADM phases
- Manage changes to requirements
- Track requirements through lifecycle

Interaction:

- Each ADM phase generates requirements
- Changes in requirements may trigger iteration of phases
- Ensures requirements traceability
- Maintains baseline of accepted requirements

---

**Q: What are Transition Architectures and why are they important?**

**A:** Transition Architectures are intermediate target architectures between baseline and target state.

Purpose:

- Provide manageable steps in transformation
- Reduce risk of big-bang changes
- Allow business value delivery in increments
- Accommodate organizational change capacity
- Enable course correction

Example: Migrating from on-premise to cloud:

- Baseline: 100% on-premise
- Transition 1: Hybrid (non-critical workloads to cloud)
- Transition 2: Hybrid (50/50 split)
- Transition 3: Cloud-first (90% cloud, legacy on-premise)
- Target: 100% cloud-native

---

### Complex

**Q: A project is in Phase D (Application Architecture) when new business requirements emerge that impact Phase B (Business Architecture). How do you handle this using ADM?**

**A:** This demonstrates ADM's iterative nature:

**Immediate Actions:**

- Capture new requirements in Requirements Management
- Assess impact on work completed in Phases A, B, C
- Determine if changes are within scope (Phase A)

**Decision Path:**

**Minor Impact (refinement):**
- Update Phase B artifacts
- Continue Phase D with adjusted inputs
- Document as architecture change

**Significant Impact (new capability):**
- Escalate to Architecture Board
- Consider iteration: return to Phase B
- Re-baseline affected phases
- Update Architecture Vision if scope changes
- Revise stakeholder approvals if needed

**Governance:**
- Use Architecture Compliance review
- Update Statement of Architecture Work
- Manage stakeholder expectations
- Document decision rationale

Key: Requirements Management enables this flexibility while maintaining control.

---

**Q: How would you conduct a gap analysis across all four architecture domains (B-C-D-E) and consolidate findings?**

**A:** Structured approach:

**1. Individual Domain Gap Analysis (B, C, D, E):**
- Baseline vs Target comparison
- Identify gaps: elements to be added, removed, modified, carried forward
- Document gap impact (cost, time, risk, business value)

**2. Cross-Domain Dependencies:**
- Application gaps requiring data changes
- Technology gaps needed for application capability
- Business process changes requiring application support

**3. Consolidation (Phase F input):**
- Create unified gap register
- Group related gaps into work packages
- Identify dependencies between packages
- Assess portfolio impact

**4. Prioritization Matrix:**

| Gap | Business Value | Technical Complexity | Dependencies | Priority |
|-----|---------------|---------------------|--------------|----------|
| CRM replacement | High | High | Data migration | P1 |
| API Gateway | Medium | Low | None | P2 |

**5. Output:**
- Consolidated Architecture Roadmap
- Work package definitions
- Resource requirements
- Risk assessment

---

**Q: Design an approach to use TOGAF ADM for a merger and acquisition (M&A) scenario where two companies with different architectures must integrate.**

**A:** M&A TOGAF Approach:

**Preliminary Phase:**
- Rapid architecture maturity assessment of both companies
- Identify governance structure for merged entity
- Establish integration principles (best-of-breed, consolidate, retire, harmonize)

**Phase A (Architecture Vision):**
- Define integration scope and boundaries
- Identify all stakeholders from both companies
- Create integration vision and business case
- Define success criteria and constraints
- Critical: Identify "must-keep" systems (regulatory, customer-facing)

**Phases B-D (Parallel Baseline Creation):**
- Document both companies' architectures (as-is)
- Business: Identify process overlaps and gaps
- Data: Map data models, identify master data conflicts
- Application: Application portfolio of both; identify duplicates
- Technology: Infrastructure inventory

**Target Architecture:**
- Rationalized portfolio (single CRM, single ERP, etc.)
- Integrated business processes
- Unified data model with reconciliation rules
- Consolidated technology platform

**Phase E-F:**
- Transition Architecture 1: Day-1 (immediate integration - critical systems)
- Transition Architecture 2: 6-month (quick wins, decommission duplicates)
- Transition Architecture 3: 18-month (deep integration)
- Target: 24+ month (fully integrated)

**Phase G (Migration):**
- Integration roadmap with business priorities
- Cultural change management
- Data migration and reconciliation strategy
- Risk mitigation: parallel running, rollback plans

**Key Considerations:**
- Speed vs Risk trade-off
- Regulatory compliance for both entities
- Customer/employee communication
- Preserve revenue-generating capabilities

---

## See Also

- [TOGAF Fundamentals](./togaf-fundamentals.md)
- [Architecture Content Framework](./architecture-content-framework.md)
- [Migration Planning](./practical-application.md)
