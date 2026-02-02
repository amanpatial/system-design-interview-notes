# Architecture Content Framework

## Introduction

The Architecture Content Framework provides a structural model for architectural content, including deliverables, artifacts, and building blocks produced during the ADM.

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Deliverable** | Work product contractually specified and formally reviewed (e.g., Architecture Vision document) |
| **Artifact** | Architectural work product describing an aspect of architecture (e.g., use-case diagram, requirements catalog) |
| **Building Block** | Component of enterprise capability (ABB = specification; SBB = implementation) |
| **Architecture Repository** | Holds all architecture-related information |

---

## Q&A — Architecture Content Framework

### Basic

**Q: What is the difference between deliverables and artifacts?**

**A:**

**Deliverables:**
- Contractually specified work products
- Formally reviewed and signed off
- Examples: Architecture Vision, Architecture Definition Document, Architecture Requirements Specification

**Artifacts:**
- Work products that describe aspects of architecture
- Comprise deliverables
- Examples: Business process diagrams, data models, application portfolios, network diagrams

Relationship: Deliverables contain one or more artifacts.

---

**Q: What are the main components of the Architecture Repository?**

**A:**

- **Architecture Metamodel:** Describes structure and content of repository
- **Architecture Landscape:** Shows state of architectures (baseline, target, transition)
- **Standards Information Base:** Standards with which architectures must comply
- **Reference Library:** Guidelines, templates, patterns, reference architectures
- **Governance Log:** Decisions, dispensations, compliance assessments

---

**Q: Explain the Architecture Content Metamodel.**

**A:** The metamodel defines relationships between architectural concepts:

**Core Entities:**
- Actor → performs Role → interacts with Business Service
- Business Service → accesses Data Entity
- Application Component → uses Data Entity
- Technology Component → hosts Application Component

**Benefits:**
- Ensures consistency
- Enables traceability
- Supports tool implementation
- Provides common language

---

### Medium

**Q: How do you create an Architecture Definition Document and what should it contain?**

**A:** Architecture Definition Document (ADD) consolidates architectural output.

**Structure:**

- **Scope:** Boundaries, domains covered, time period
- **Architecture Overview:** High-level summary, key decisions
- **Business Architecture:** Process models, organization structure, business capabilities
- **Data Architecture:** Data entity/relationship models, data management strategy
- **Application Architecture:** Application portfolio, interfaces, migrations
- **Technology Architecture:** Platform services, technology standards, deployment models
- **Gaps, Solutions & Dependencies:** Gap analysis results, work packages
- **Impact Assessment:** Stakeholder impact, cost/benefit analysis

**Best Practices:**
- Tailor level of detail to audience
- Include rationale for key decisions
- Link to requirements
- Version control with baseline/target/transition views

---

**Q: What is a Building Block and how do you define one?**

**A:**

**Building Block Characteristics:**
- Defined functionality
- Clear interfaces
- Publishable service contract
- Reusable
- Can be combined with other building blocks

**Specification Process:**

**1. Identify:**
- From gap analysis or requirements
- Through decomposition of services/capabilities

**2. Define Architecture Building Block (ABB):**
- Name and description
- Functional requirements
- Non-functional requirements (performance, security)
- Interfaces (inputs/outputs)
- Dependencies on other ABBs

**3. Map to Solution Building Block (SBB):**
- Vendor product or custom solution
- Specific versions and configurations
- Deployment requirements

**Example:**

**ABB:** "Payment Processing Service"
- Function: Process credit card payments
- Interface: REST API (charge, refund, query)
- Requirements: PCI-DSS compliant, 99.9% availability

**SBB:** "Stripe Payment Gateway v3.2"
- Implementation of payment processing
- Specific Stripe API configuration
- AWS deployment specification

---

**Q: How do you maintain traceability from business requirements to technology components?**

**A:** Traceability using Content Framework:

**Levels of Traceability:**

**1. Requirements → Business Architecture:**
- Business requirement links to business capability
- Capability realized by business service
- Service performed by business process

**2. Business → Data:**
- Business process creates/reads/updates/deletes data entities
- Data entity relationships documented

**3. Business → Application:**
- Business service supported by application function
- Application component provides function
- Application interface enables integration

**4. Application → Technology:**
- Application component deployed on technology component
- Technology platform provides infrastructure services

**Traceability Matrix:**

| Requirement | Business Service | Application | Technology | Status |
|-------------|-----------------|-------------|------------|--------|
| REQ-001: Process order | Order Management | OrderApp | AWS ECS | Implemented |
| REQ-002: Customer 360 | Customer Service | CRM | Salesforce | Planned |

**Tools:** Requirements management tool integrated with architecture repository.

---

### Complex

**Q: Design a Building Block Catalog for a financial services enterprise. Include architecture and solution building blocks.**

**A:** Financial Services Building Block Catalog:

**Business Architecture Building Blocks:**

**Customer Management:**
- ABB: Customer Onboarding Service
  - KYC verification, document management, compliance checks
- ABB: Customer 360 View Service
  - Unified customer profile, interaction history

**Product Services:**
- ABB: Loan Origination Service
  - Application processing, credit decisioning, approval workflow
- ABB: Account Management Service
  - Account opening, maintenance, closure

**Core Banking:**
- ABB: Transaction Processing Service
  - Debits, credits, transfers, reconciliation
- ABB: Interest Calculation Service
  - Accrual, compounding, payment

**Application Architecture Building Blocks:**

**ABB Categories:**
- **Channel:** Mobile banking app, web portal, branch systems
- **Integration:** API gateway, ESB, message broker
- **Core:** Core banking platform, CRM, document management
- **Analytics:** Risk engine, fraud detection, reporting

**Solution Building Blocks (Example Mapping):**

| ABB | SBB Options | Selected | Rationale |
|-----|------------|----------|-----------|
| Core Banking Platform | Temenos T24 / FIS Profile / Custom | Temenos T24 | Market leader, cloud-ready |
| API Gateway | Kong / Apigee / AWS API Gateway | Apigee | Advanced security, analytics |
| CRM | Salesforce Financial Services Cloud / Custom | Salesforce FSC | Industry-specific features |
| Fraud Detection | FICO Falcon / SAS Fraud / Custom ML | FICO Falcon | Proven in banking |

**Technology Architecture Building Blocks:**

**Infrastructure:**
- ABB: Container Orchestration Platform → SBB: Kubernetes on AWS EKS
- ABB: Database Platform → SBB: PostgreSQL (transactional), MongoDB (documents)
- ABB: Message Queue → SBB: Apache Kafka

**Security:**
- ABB: Identity & Access Management → SBB: Okta
- ABB: Secrets Management → SBB: HashiCorp Vault
- ABB: Security Monitoring → SBB: Splunk SIEM

**Governance:**
- Version control for building blocks
- Reuse metrics and tracking
- Approval process for new building blocks
- Retirement criteria for obsolete blocks

---

**Q: An organization has 200+ applications. How would you use the Architecture Content Framework to rationalize this portfolio?**

**A:** Application Rationalization Approach:

**Phase 1: Inventory & Classification**

**Artifact Creation:**
- Application Portfolio Catalog (artifact)
  - For each app: Name, owner, business service, users, cost, tech stack, age

**Classification Dimensions:**
- **Business Value:** High / Medium / Low
- **Technical Health:** Good / Fair / Poor
- **Strategic Fit:** Core / Support / Utility

**Phase 2: Assess Against Architecture**

**Map to Business Capabilities:**
- Which business capabilities does each app support?
- Are capabilities supported by multiple apps (redundancy)?
- Are there capability gaps (no app support)?

**Map to Building Blocks:**
- Define target ABBs for each business capability
- Identify which apps align with target ABBs
- Flag apps that don't fit target architecture

**Phase 3: Rationalization Matrix**

**TIME Framework (Tolerate, Invest, Migrate, Eliminate):**

| App | Business Value | Technical Health | Decision | Rationale |
|-----|----------------|------------------|----------|-----------|
| Legacy CRM | High | Poor | **Migrate** | Critical to business; replace with Salesforce (SBB) |
| Custom reporting | Medium | Fair | **Tolerate** | Adequate; no budget for replacement |
| Excel-based tool | Low | Poor | **Eliminate** | Capability covered by new BI platform |
| Modern API gateway | High | Good | **Invest** | Strategic; expand usage |

**Phase 4: Consolidation Plan**

**Identify Overlaps:**
- 5 different customer databases → Consolidate to 1 MDM
- 3 reporting tools → Standardize on 1 BI platform
- Multiple integration patterns → Standardize on API gateway + ESB

**Create Work Packages:**
- WP-01: CRM Migration (Phases B, C, D involved)
- WP-02: BI Platform Consolidation
- WP-03: Application Decommissioning (15 apps)

**Phase 5: Deliverables**

- **Architecture Definition Document:** Target application architecture
- **Gap Analysis:** Current vs target
- **Migration Plan:** Roadmap with priorities
- **Cost-Benefit Analysis:** TCO reduction projections
- **Risk Assessment:** Dependencies, data migration risks

**Metrics:**
- Reduce 200 apps → 120 apps (40% reduction)
- Reduce annual maintenance cost by 30%
- Eliminate technical debt
- Improve capability coverage

---

## See Also

- [ADM Phases](./adm-phases.md)
- [Enterprise Continuum](./enterprise-continuum.md)
- [Architecture Governance](./architecture-governance.md)
