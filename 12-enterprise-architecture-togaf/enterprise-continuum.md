# Enterprise Continuum & Architecture Repository

## Introduction

The Enterprise Continuum provides a classification scheme for architecture assets, from generic foundation architectures to organization-specific architectures.

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Enterprise Continuum** | View of Architecture Repository showing evolution from generic to specific |
| **Architecture Continuum** | Classification of architectures (Foundation → Common Systems → Industry → Organization-specific) |
| **Solutions Continuum** | Classification of solutions that implement architectures |
| **Architecture Repository** | Storage for all architectural assets |

---

## Q&A — Enterprise Continuum

### Basic

**Q: What is the Enterprise Continuum and what problem does it solve?**

**A:** The Enterprise Continuum is a model for structuring architecture assets from generic to specific.

**Problem it solves:**
- **Reuse:** Leverage existing architectures rather than starting from scratch
- **Consistency:** Common language and classification
- **Efficiency:** Find relevant reference models quickly
- **Best practices:** Learn from industry patterns

**Structure:**

**Architecture Continuum:**
- Foundation Architectures (e.g., TOGAF TRM)
- Common Systems Architectures (e.g., Generic IT systems)
- Industry Architectures (e.g., Banking, Healthcare)
- Organization-Specific Architectures

**Solutions Continuum:**
- Foundation Solutions (e.g., Operating systems)
- Common Systems Solutions (e.g., ERP packages)
- Industry Solutions (e.g., Core banking systems)
- Organization-Specific Solutions

---

**Q: What is TOGAF's Technical Reference Model (TRM)?**

**A:** The TRM is a Foundation Architecture providing taxonomy and visual representation of platform services.

**Purpose:**
- Common vocabulary for infrastructure services
- Reference for gap analysis
- Basis for selecting standards

**Key Service Categories:**
- Application Platform Services (data management, transaction processing)
- Application Platform Interface (APIs for application access)
- Communications Infrastructure Interface
- Qualities (security, availability, performance)

**Usage:** Compare organization's platform against TRM to identify gaps or redundancies.

---

### Medium

**Q: How would you use the Enterprise Continuum in practice when starting a new architecture project?**

**A:** Practical Usage Steps:

**1. Start with Foundation:**
- Review TOGAF TRM for platform services taxonomy
- Understand generic patterns and principles

**2. Leverage Industry Assets:**
- Search for industry reference architectures (e.g., BIAN for banking, HL7 for healthcare)
- Adopt industry standards and best practices
- Review industry solution patterns

**3. Review Organizational Assets:**
- Check Architecture Repository for existing org architectures
- Reuse proven building blocks
- Adopt organization's architecture principles and standards

**4. Adapt and Extend:**
- Customize industry patterns to org context
- Create organization-specific extensions
- Store new assets back in repository

**Example:** Building customer portal:
- Foundation: Standard web architecture patterns (TOGAF TRM)
- Industry: Retail customer experience patterns
- Organization: Existing authentication ABBs, brand guidelines
- New: Custom loyalty integration (add to org-specific catalog)

---

**Q: Explain how the Solutions Continuum relates to the Architecture Continuum.**

**A:**

**Relationship:**
- Architectures (specifications) → Solutions (implementations)
- Each level in Architecture Continuum has corresponding Solutions Continuum level

**Parallel Structure:**

| Architecture Level | Solutions Level | Example |
|-------------------|-----------------|---------|
| Foundation Architecture | Foundation Solution | Network protocol (TCP/IP) implemented in OS |
| Common Systems | Common Systems Solution | Authentication pattern → OAuth 2.0 |
| Industry Architecture | Industry Solution | Banking architecture → Temenos core banking |
| Org-Specific Architecture | Org-Specific Solution | Custom CRM architecture → Custom CRM implementation |

**Usage:**
- During architecture development, reference Architecture Continuum
- During implementation, select from Solutions Continuum
- Ensure alignment: chosen solutions must implement target architectures

---

### Complex

**Q: Design an Architecture Repository structure for a large multinational corporation with multiple business units.**

**A:** Enterprise Architecture Repository Design:

**1. Repository Structure:**

```
/Enterprise-Architecture-Repository
├── /Architecture-Metamodel
│   ├── Entity definitions
│   ├── Relationship rules
│   └── Validation schemas
│
├── /Architecture-Landscape
│   ├── /Strategic-Architectures
│   │   ├── Enterprise target architecture
│   │   └── Domain architectures
│   ├── /Segment-Architectures
│   │   ├── Business-Unit-A
│   │   ├── Business-Unit-B
│   │   └── Shared-Services
│   ├── /Capability-Architectures
│   │   ├── Customer-Management
│   │   ├── Product-Catalog
│   │   └── Order-to-Cash
│   └── /Transition-Architectures
│       ├── Current-State (baseline)
│       ├── 6-month-state
│       ├── 12-month-state
│       └── Target-State
│
├── /Standards-Information-Base
│   ├── Technology standards (languages, platforms)
│   ├── Data standards (canonical models)
│   ├── Integration standards (API specs)
│   ├── Security standards
│   └── Compliance requirements
│
├── /Reference-Library
│   ├── /Foundation-Assets
│   │   ├── TOGAF TRM
│   │   └── Architecture patterns
│   ├── /Industry-Assets
│   │   ├── Industry reference models
│   │   └── Industry standards (BIAN, HL7, etc.)
│   ├── /Organization-Assets
│   │   ├── Enterprise patterns
│   │   ├── Reusable building blocks
│   │   ├── Solution blueprints
│   │   └── Case studies
│   └── /Templates
│       ├── Document templates
│       └── Diagram templates
│
└── /Governance-Log
    ├── Architecture Board decisions
    ├── Compliance assessments
    ├── Waivers and dispensations
    └── Audit trail
```

**2. Classification Taxonomy:**

**By Maturity:**
- Draft → Review → Approved → Published → Deprecated

**By Scope:**
- Enterprise-wide → Business-Unit → Capability-specific

**By Domain:**
- Business → Data → Application → Technology

**3. Access Control:**

**Role-Based Access:**
- **Enterprise Architects:** Full access to all sections
- **Domain Architects:** Read all; write to their domain
- **Business Unit Architects:** Read enterprise/industry; write to their BU
- **Project Teams:** Read approved assets; submit new assets for review
- **Executive Stakeholders:** Read published summaries

**4. Governance Process:**

**Contribution Workflow:**
- Submit → Review (architecture team) → Approval (Architecture Board) → Publish → Notify stakeholders

**Versioning:**
- Major version: Breaking changes
- Minor version: Enhancements
- Patch: Corrections

**5. Integration & Tools:**

**Repository Tool Selection:**
- Central tool (e.g., Sparx EA, Ardoq, Avolution ABACUS)
- Integration with collaboration tools (Confluence, SharePoint)
- API for automated access
- Search and discovery capabilities

**Integrations:**
- CMDB (configuration items)
- Service catalog
- Project portfolio management
- Requirements management

**6. Metrics & KPIs:**

**Repository Health:**
- Asset reuse rate (# times referenced)
- Coverage (% of capabilities with documented architecture)
- Currency (age of assets, last update)
- Compliance (% projects following standards)

**Example Metrics:**
- 75% of projects reuse existing building blocks
- 95% of capabilities have architecture documentation
- Average asset age < 18 months
- 90% of projects pass architecture compliance review

---

**Q: How do you balance standardization (enforced by Enterprise Continuum) with innovation and local autonomy?**

**A:** Balancing Act Strategy:

**1. Define "Non-Negotiables" (Standardize):**

**Enterprise-Wide Standards:**
- Security & compliance (mandatory)
- Data governance and privacy (mandatory)
- Integration standards (API gateway, event formats)
- Identity & access management
- Core infrastructure platforms

**Rationale:** These provide cohesion, reduce risk, enable interoperability.

**2. Define "Innovation Zones" (Autonomy):**

**Areas for Experimentation:**
- Application frameworks (within approved languages)
- UI/UX approaches
- Algorithm implementation
- Tool selection (within budget and support constraints)
- Development methodologies

**Rationale:** Enable teams to adopt best-of-breed solutions, innovate, maintain agility.

**3. Governance Model:**

**"Principles + Patterns" Approach:**
- Prescribe principles, not implementation details
- Provide reference implementations, not mandates
- Exception process for justified deviations

**Example:**
- **Principle:** "APIs must be RESTful and OpenAPI-documented"
- **Freedom:** Choose any framework (Spring, Express, Flask)
- **Pattern:** Reference implementation available but not mandatory

**4. Architecture Review Tiers:**

**Tier 1 (Lightweight):** Projects using standard building blocks
- Self-service approval
- Automated compliance checks
- Spot reviews

**Tier 2 (Standard):** Projects with minor customizations
- Architecture review meeting
- Documented deviations
- Approved by domain architect

**Tier 3 (Heavyweight):** Major innovation or deviations
- Architecture Board review
- Business case for deviation
- Approved by enterprise architect

**5. Feedback Loop:**

**Innovation → Standardization Path:**
- Successful innovations captured as patterns
- Patterns promoted to organization-specific assets
- Best patterns promoted to standards

**Example:** Team experiments with serverless (innovation) → Success documented (pattern) → Added to approved patterns (standard)

**6. Balanced Scorecard:**

**Measure Both:**
- Standardization metrics (compliance, reuse)
- Innovation metrics (new patterns, time-to-market, satisfaction)

**Target:** High compliance on non-negotiables + High satisfaction with autonomy

**Example Culture:**
- "Standards for what; autonomy for how"
- "Standardize integration; innovate implementation"
- "Centralized governance; decentralized execution"

---

## See Also

- [Architecture Content Framework](./architecture-content-framework.md)
- [Architecture Governance](./architecture-governance.md)
- [TOGAF Fundamentals](./togaf-fundamentals.md)
