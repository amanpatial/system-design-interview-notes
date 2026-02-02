# TOGAF Practical Application

## Introduction

This section covers real-world scenarios, case studies, and practical application of TOGAF concepts in enterprise architecture roles.

---

## Q&A — Practical Application

### Basic

**Q: Walk through the first 3 phases of ADM for a new CRM implementation project.**

**A:**

**Preliminary Phase:**
- Confirm organization's architecture framework (TOGAF-based)
- Identify stakeholders: Sales VP, Marketing VP, IT Director, Data Privacy Officer
- Review enterprise architecture principles

**Phase A (Architecture Vision):**

**Activities:**
- Define scope: CRM for sales and marketing; integration with existing ERP
- Stakeholder concerns: Sales wants mobile access; Marketing wants campaign analytics; IT wants cloud; Privacy wants GDPR compliance
- High-level vision: Cloud-based CRM with mobile app, integrated with ERP and marketing automation
- Business case: Increase sales productivity 20%, improve customer data quality

**Deliverables:**
- Architecture Vision document
- Statement of Architecture Work
- Stakeholder Map

**Phase B (Business Architecture):**

**Activities:**
- Baseline: Current sales process (manual entry, spreadsheets)
- Target: Automated lead-to-cash process with workflow
- Gap: Need lead scoring, opportunity management, quote generation capabilities

**Artifacts:**
- Business process models (BPMN)
- Business capability map
- Organization structure impact analysis

**Output:** Business Architecture document with gap analysis

---

**Q: What are Architecture Principles and give examples?**

**A:** Architecture Principles are general rules and guidelines that inform and support the way an organization fulfills its mission.

**Structure:**

- **Name:** Principle title
- **Statement:** Concise rule
- **Rationale:** Why this principle exists
- **Implications:** Impact of following this principle

**Examples:**

**Principle 1: Data is an Asset**
- Statement: Data is shared and accessible across the enterprise
- Rationale: Shared data improves decision-making and reduces duplication
- Implications: Invest in master data management; define data ownership; create data sharing mechanisms

**Principle 2: Buy Before Build**
- Statement: Purchase commercial solutions where available before building custom
- Rationale: Reduces development cost and time; leverages vendor innovation
- Implications: Conduct build-vs-buy analysis; maintain vendor relationships; customize minimally

**Principle 3: Security by Design**
- Statement: Security is built into solutions from inception, not added afterward
- Rationale: Retrofitting security is costly and less effective
- Implications: Security review at each architecture phase; security requirements in all projects; threat modeling mandatory

---

### Medium

**Q: A business unit wants to implement a SaaS solution that doesn't integrate well with enterprise standards. How do you evaluate this using TOGAF?**

**A:** Evaluation Approach:

**1. Requirements Analysis (Requirements Management):**

**Business Drivers:**
- What business need does SaaS solve?
- Time-to-value requirement?
- Cost comparison vs. standard solution?

**2. Architecture Impact Assessment:**

**Integration Assessment:**
- How does it integrate with existing systems (CRM, ERP, etc.)?
- Does it support standard APIs (REST, SOAP)?
- Data synchronization requirements?

**Data Assessment:**
- What data is stored (PII, financial)?
- Data residency requirements?
- Master data conflicts?

**Security Assessment:**
- SSO integration capability?
- Compliance (GDPR, SOC2, ISO27001)?
- Vendor security posture?

**3. Apply Architecture Principles:**

**Principle: "Buy Before Build":**
- ✓ Supports using SaaS

**Principle: "Interoperability":**
- ✗ Poor integration capability
- Can we work around it (middleware, custom connectors)?

**Principle: "Data is an Asset":**
- ✗ Data silo risk
- Can we extract data for enterprise use?

**4. Options Analysis:**

**Option 1: Approve with Conditions**
- Use SaaS but require integration via iPaaS (MuleSoft, Boomi)
- Extract data nightly to enterprise data warehouse
- SSO via SAML

**Option 2: Alternative Solution**
- Use enterprise-standard platform with similar capability
- Longer implementation but better integration

**Option 3: Dispensation**
- Approve as pilot for one business unit
- Require integration plan for enterprise adoption
- Time-limited (1 year; re-evaluate)

**5. Decision:**
- Present options to Architecture Board
- Recommend based on business value vs. architecture impact
- Document decision and rationale

**Example Decision:**
"Approve SaaS for 1-year pilot with conditions: (1) SSO integration mandatory, (2) Data extract to enterprise warehouse weekly, (3) Business unit funds integration costs, (4) Re-evaluate after 1 year for enterprise adoption."

---

**Q: How do you use TOGAF to drive a cloud migration program?**

**A:** Cloud Migration Using TOGAF:

**Preliminary Phase:**
- Establish cloud principles (cloud-first, multi-cloud vs. single-cloud)
- Define cloud governance model
- Select cloud providers (AWS, Azure, GCP)

**Phase A (Architecture Vision):**
- Cloud migration vision: "80% of workloads in cloud within 3 years"
- Business drivers: Agility, cost reduction, innovation
- Stakeholder buy-in: CFO (cost), CTO (innovation), CISO (security)

**Phases B-E (Baseline & Target):**

**Baseline (Current State):**
- Application portfolio: 200 apps, 120 on-premise, 50 colo, 30 SaaS
- Infrastructure: 500 VMs, 50 physical servers
- Data centers: 2 owned DCs

**Target (Cloud-Native):**
- Applications:
  - 100 apps on cloud IaaS/PaaS
  - 60 apps replaced with SaaS
  - 40 apps retired (redundant)
- Infrastructure: Multi-region cloud deployment
- Data centers: Decommissioned

**Gap Analysis:**
- 140 apps need migration
- Skills gap: cloud expertise needed
- Security: Cloud security model different
- Compliance: Data residency requirements

**Phase E (Technology Architecture):**
- Landing zone design (networking, security, governance)
- Migration patterns: Rehost (lift-and-shift), Replatform, Refactor, Retire, Retain
- Hybrid connectivity (VPN, Direct Connect)

**Phase F (Opportunities & Solutions):**

**Migration Waves:**
- Wave 1 (Months 1-6): Non-critical, stateless apps (rehost)
- Wave 2 (Months 7-12): Databases and stateful apps (replatform)
- Wave 3 (Months 13-24): Refactor to cloud-native
- Wave 4 (Months 25-36): Complex systems, mainframe

**6R Strategy:**
- Rehost: 40 apps (quick wins)
- Replatform: 30 apps (modernize slightly)
- Refactor: 30 apps (cloud-native)
- Retire: 40 apps (redundant)
- Retain: 20 apps (mainframe, not migrating)
- Replace: 40 apps (with SaaS)

**Phase G (Migration Planning):**
- Detailed project plans per wave
- Resource allocation
- Training plan (cloud certifications)
- Risk mitigation: Pilot migrations, rollback procedures

**Phase H (Change Management):**
- Monitor migrations
- Capture lessons learned
- Update architecture repository with cloud patterns
- Establish cloud center of excellence

**Success Metrics:**
- 80% workloads in cloud (target achieved)
- 30% cost reduction
- 50% faster provisioning
- Improved disaster recovery (multi-region)

---

### Complex

**Q: An enterprise has business units in 15 countries with different regulations and IT systems. How would you use TOGAF to create a federated architecture approach?**

**A:** Federated Enterprise Architecture Strategy:

**1. Architecture Governance Model:**

**Centralized (Enterprise Level):**
- Enterprise-wide principles and standards
- Strategic direction
- Critical shared capabilities

**Federated (Regional/BU Level):**
- Regional architectures within enterprise guardrails
- Local implementation decisions
- Adapt to local regulations

**2. Preliminary Phase:**

**Define Federation Principles:**

**Principle: "Global Standards, Local Implementation"**
- Statement: Enterprise defines "what"; regions define "how"
- Example: Enterprise mandates API gateway (what); regions choose vendor (how)

**Principle: "Mandatory Interoperability"**
- Statement: All regional systems must integrate with global systems
- Example: All regions connect to global customer MDM

**Principle: "Comply or Explain"**
- Statement: Follow enterprise standards unless justified exception
- Example: Region can use local payment gateway if global doesn't support local methods

**3. Architecture Structure:**

**Enterprise Architecture Layer:**

**Mandatory (Non-Negotiable):**
- Security standards (SSO, encryption, access control)
- Data governance (PII handling, retention, sovereignty)
- Integration standards (API specs, event formats)
- Financial reporting (single ERP)
- Compliance monitoring

**Reference (Recommended):**
- Cloud platform recommendations
- Application architecture patterns
- Technology stack options

**Regional Architecture Layer:**

**Autonomy Areas:**
- Local applications (within approved platforms)
- Regional infrastructure (within approved providers)
- Vendor selection (from approved list)
- Implementation approach

**Regional Responsibilities:**
- Comply with local regulations
- Implement enterprise standards
- Maintain regional architecture repository
- Report compliance to enterprise

**4. ADM Application:**

**Phase A (Architecture Vision):**
- Enterprise Vision: Unified global platform with regional flexibility
- Regional Visions: Align with enterprise; add local context

**Phases B-D:**

**Enterprise Level:**
- **Business:** Global business capabilities (customer management, finance)
- **Data:** Global canonical data model; regional extensions allowed
- **Application:** Global application categories; regional instances
- **Technology:** Approved platforms (AWS, Azure); regions pick one

**Regional Level:**
- **Business:** Regional process variants (comply with local laws)
- **Data:** Regional data residency; local master data
- **Application:** Regional application portfolio; map to enterprise categories
- **Technology:** Regional deployment of approved platforms

**5. Integration Architecture:**

**Hub-and-Spoke Model:**
- Enterprise Hub: Global customer MDM, financial consolidation, analytics
- Regional Spokes: Regional systems integrate with hub via standard APIs

**Patterns:**
- Customer created in Region A → Synced to Global MDM → Available to all regions
- Global product catalog → Replicated to regions → Regional pricing/availability

**6. Data Sovereignty:**

**Approach:**
- Data stored in-region (GDPR, local laws)
- Metadata/summary at global level
- Cross-border transfers: anonymized or consented
- Regional data lake → Global analytics (aggregated, anonymized)

**7. Governance:**

**Enterprise Architecture Board:**
- Meets quarterly
- Approves enterprise standards
- Resolves cross-regional conflicts
- Strategic decisions

**Regional Architecture Boards:**
- Meet monthly
- Regional compliance
- Escalate to enterprise board when needed

**Federated Review Process:**
- Regional standards reviewed by enterprise (alignment check)
- Enterprise standards reviewed by regional representatives (feasibility check)

**8. Example: Global CRM Implementation:**

**Enterprise Decision:**
- Standard: Salesforce as enterprise CRM platform
- Integration: All regions connect via Salesforce APIs
- Data: Customer master data in Salesforce (global)

**Regional Implementations:**
- North America: Full Salesforce Sales Cloud + Service Cloud
- Europe: Salesforce + local marketing automation (GDPR-specific)
- Asia-Pacific: Salesforce + local payment gateway integrations
- Latin America: Lighter Salesforce config (cost sensitivity)

**Common:**
- SSO integration (global Okta)
- API specifications (OpenAPI standard)
- Data model (customer, account, opportunity)

**Regional Variations:**
- Language/localization
- Regional compliance fields
- Local integrations

**Outcome:**
- 80% common architecture
- 20% regional adaptation
- All regions interoperable

**9. Success Factors:**

**Key Enablers:**
- Clear demarcation of enterprise vs. regional decisions
- Strong communication and collaboration
- Regional architects feel empowered, not constrained
- Enterprise standards enable, not block regional needs
- Regular architecture forums (global + regional)

**Pitfalls to Avoid:**
- Too much centralization → regions feel stifled
- Too much autonomy → fragmentation, silos
- One-size-fits-all → doesn't fit anyone

**Balance:** 80/20 rule: standardize 20% that matters most; allow flexibility on the rest.

---

**Q: You're asked to conduct a TOGAF architecture assessment for a potential M&A target. What do you assess and what are red flags?**

**A:** M&A Architecture Due Diligence:

**1. Architecture Maturity Assessment:**

**Evaluate:**
- Is there formal enterprise architecture?
- TOGAF or similar framework in use?
- Architecture governance established?

**Red Flags:**
- No architecture documentation
- "Heroic" architecture (knowledge in individuals' heads)
- No architecture standards

**2. Application Portfolio Assessment:**

**Inventory:**
- Application count and categories
- Age of applications (average age >10 years is concern)
- Technology stack diversity

**Analysis:**
- Critical applications (revenue-impacting)
- Redundant applications (multiple HR systems)
- Integration complexity (point-to-point vs. standardized)

**Red Flags:**
- High number of custom-built apps (hard to maintain)
- End-of-life technologies
- Heavy customization of COTS products
- No application portfolio management

**Example Finding:** "Target has 15 HR/payroll systems (one per region) with no integration. Consolidation will be complex."

**3. Technical Architecture Assessment:**

**Infrastructure:**
- Data center locations and ownership
- Cloud adoption (or lack thereof)
- Hosting models (owned, colo, cloud)

**Technology Standards:**
- Diversity of platforms and languages
- Use of proprietary vs. open standards
- Technical debt assessment

**Red Flags:**
- Heavy reliance on single-vendor proprietary tech
- Mainframe with no modernization plan
- No virtualization/containerization
- Multiple overlapping platforms

**4. Data Architecture Assessment:**

**Data Landscape:**
- Number of databases and types
- Master data management approach
- Data quality maturity

**Data Governance:**
- Data ownership defined?
- Data cataloging in place?
- Privacy compliance (GDPR, CCPA)?

**Red Flags:**
- No MDM (customer data scattered across 50 systems)
- Poor data quality (duplicates, inconsistencies)
- No data governance
- Compliance violations or exposures

**Example Finding:** "Customer data in 40+ systems with no single source of truth. No GDPR documentation."

**5. Integration Architecture:**

**Integration Patterns:**
- Number of integrations (point-to-point vs. hub)
- Integration technologies (ESB, APIs, file transfers, DB links)
- API management

**Red Flags:**
- Spaghetti integrations (point-to-point everywhere)
- No API strategy
- Synchronous tightly-coupled integrations
- No integration standards

**Example Finding:** "500+ point-to-point integrations; no API gateway; mostly batch file transfers."

**6. Security Architecture:**

**Assessment:**
- Identity & access management
- Network security
- Data protection (encryption, DLP)
- Incident response capability

**Red Flags:**
- No centralized IAM (multiple user directories)
- Weak authentication (no MFA)
- Unencrypted sensitive data
- Recent security breaches

**7. Cost Structure:**

**Financial Analysis:**
- IT spend breakdown (apps, infra, support)
- Licensing costs
- Technical debt (cost to maintain legacy)

**Red Flags:**
- High maintenance costs (>70% of IT budget)
- Expensive mainframe contracts
- Out-of-support software
- Shadow IT (unmanaged spend)

**8. Skills & Capability:**

**Team Assessment:**
- Architecture team size and experience
- Skills inventory
- Dependency on key individuals

**Red Flags:**
- No architecture team
- Skills concentrated in few people
- High attrition
- Offshore dependency without knowledge transfer

**9. Compliance & Risk:**

**Regulatory:**
- Industry regulations (HIPAA, PCI-DSS, SOX)
- Evidence of compliance
- Audit findings

**Red Flags:**
- Failed audits
- Outstanding compliance issues
- No compliance framework
- Regulatory fines

**10. Integration Complexity Scoring:**

**Calculate Integration Effort:**

**Low Complexity (Months 0-6):**
- Similar tech stacks
- Well-documented APIs
- Cloud-native both sides
- Example: Both use Salesforce CRM → Easy to merge

**Medium Complexity (Months 6-18):**
- Different tech but standard protocols
- Some legacy but documented
- Integration layer feasible

**High Complexity (Months 18-36):**
- Mainframe + cloud mix
- Custom protocols
- No documentation
- Heavy data migration

**Very High Complexity (Months 36+):**
- Incompatible architectures
- No integration capability
- Regulatory barriers
- May require parallel running indefinitely

**11. Due Diligence Report:**

**Executive Summary:**
- Architecture maturity: Low/Medium/High
- Integration complexity: Low/Medium/High/Very High
- Estimated integration cost: $XXM
- Estimated integration time: XX months
- Key risks and mitigations

**Recommendations:**

**Go/No-Go Factors:**
- Deal-breakers: Major security issues, incompatible compliance, impossible integration
- Negotiation points: Lower price due to technical debt, require remediation before close
- Post-merger priorities: Integration roadmap, quick wins, risky items

**Example Scenarios:**

**Scenario A: Good Fit**
- Modern cloud architecture
- Similar tech stack
- Strong architecture practice
- Recommendation: Proceed; low integration risk

**Scenario B: High Risk**
- Legacy mainframe-centric
- No architecture governance
- Major security gaps
- Recommendation: Proceed only if: (1) Price adjusted for $50M modernization cost, (2) 3-year integration timeline accepted, (3) Key personnel retained

**Scenario C: Walk Away**
- Critical regulatory non-compliance
- Impossible to integrate with core systems
- Technical debt exceeds acquisition value

**12. Post-Acquisition Integration Plan:**

**If Proceed:**
- Use ADM phases to plan integration
- Priority: Integrate customer-facing and revenue systems first
- Create target architecture for merged entity
- Define transition architectures
- Establish integration governance

---

**Q: Design an approach to implement TOGAF in an organization currently using agile/DevOps with no formal architecture.**

**A:** TOGAF for Agile/DevOps Environment:

**Challenge:** TOGAF perceived as heavyweight and slow; agile values working software and rapid iteration.

**Strategy: "Architecture as Code" + Lightweight TOGAF**

**1. Mindset Shift:**

**From:** Big upfront architecture documents
**To:** Evolutionary architecture with continuous design

**From:** Architecture approval gates
**To:** Architecture guardrails with automation

**From:** Centralized decisions
**To:** Decentralized decisions within boundaries

**2. Tailored ADM:**

**Preliminary Phase:**
- Define architecture principles aligned with agile manifesto
- Establish lightweight governance
- Architecture as enabler, not gate

**Phase A (Agile Iteration Planning):**
- Architecture Vision per epic or major feature
- 1-page vision (not 50-page document)
- Stakeholder buy-in in sprint planning

**Phases B-D (Iterative):**
- Architecture evolves with sprints
- Document decisions as ADRs (Architecture Decision Records)
- Use C4 diagrams, not heavyweight UML

**Phase E (Technology):**
- Infrastructure as Code (Terraform)
- Platform services via internal developer platform

**Phase F-G (Continuous):**
- Roadmap integrated with product roadmap
- Backlog items for architecture improvements
- Technical debt tracked and prioritized

**Phase H (Continuous):**
- Architecture evolves with every sprint
- Retrospectives include architecture reflection

**3. Governance Integration:**

**Shift-Left Governance:**
- Architecture principles → Linting rules (automated)
- Standards → Golden paths (paved roads)
- Compliance → Policy-as-code (OPA, Sentinel)

**Example:**
- Principle: "APIs must be versioned"
- Implementation: Linter checks for version in API path
- CI/CD: Fails build if not compliant

**Shift-Right Monitoring:**
- Fitness functions: Automated tests for architecture characteristics
- Runtime monitoring: Alerts on architecture violations
- Example: Alert if service exceeds latency budget

**4. Architecture Artifacts:**

**Lightweight Deliverables:**

**Instead of:** 100-page Architecture Definition Document
**Use:** Architecture wiki with:
- System Context diagram (C4)
- Key ADRs
- API specifications (OpenAPI)
- Data models (ER diagrams)
- Deployment architecture (Terraform)

**Living Documentation:**
- Docs in code repo
- Diagrams generated from code (PlantUML, Mermaid)
- Versioned with application

**5. Architecture Board → Architecture Guild:**

**Guild Model:**
- Open membership (any interested engineer)
- Meet weekly (30 min)
- Review ADRs
- Share patterns
- Collaborative, not authoritative

**Architecture Champions:**
- One champion per team
- Represents team in guild
- Brings architecture insights back to team

**6. Building Blocks as Inner Source:**

**Enterprise Building Blocks:**
- Published as libraries, containers, Terraform modules
- Documented with examples
- Inner source: Teams can contribute improvements

**Example:**
- ABB: "Authentication Service"
- SBB: `auth-service:v2.3` Docker image
- Usage: `docker run enterprise/auth-service:v2.3`
- Contribution: Team improves it, submits PR, others benefit

**7. Repository = Developer Portal:**

**Content:**
- Service catalog (all microservices)
- API documentation (auto-generated)
- Architecture guidelines
- Getting started guides
- Reusable components

**Tools:** Backstage (Spotify), internal GitHub

**8. Metrics:**

**Agile-Friendly Metrics:**
- Lead time for architecture approval: <1 day
- Reuse rate of building blocks: 70%
- Standards violations detected in CI/CD: 90% caught pre-merge
- Developer satisfaction with architecture: >75%

**9. Culture:**

**Architecture Principles for Agile:**

**Principle: "You Build It, You Run It"**
- Teams own architecture of their services
- Architects provide consultation, not approval

**Principle: "Architecture Emerges"**
- Start simple, refactor as needed
- Architect for now, not for all possible futures

**Principle: "Make Reversible Decisions Quickly"**
- For low-risk, reversible decisions: teams decide
- For high-risk, irreversible decisions: architect reviews

**10. Example Integration:**

**User Story:** "As a customer, I want to view my order history"

**Architecture Integration:**
- Team designs API endpoint
- References enterprise "Order" data model (standardized)
- Uses enterprise API gateway pattern (standard building block)
- Implements caching per architecture guidance
- Writes ADR: "We chose Redis for caching (aligns with enterprise standard)"
- CI/CD runs architecture compliance checks
- Deploys with monitoring (architecture fitness functions check latency)

**Result:**
- Team maintains agility
- Architecture coherence maintained
- Compliance automated
- No heavyweight reviews

**11. Success Story:**

**Transformation:**
- **Before:** 6-week architecture review process; 40% of projects get dispensations; frustration
- **After:** <1 day for standard patterns; 90% automated compliance; architecture seen as enabler

**Outcome:**
- Faster delivery
- Better architecture (automated enforcement)
- Higher satisfaction
- Innovation within guardrails

---

## See Also

- [ADM Phases](./adm-phases.md)
- [Architecture Governance](./architecture-governance.md)
- [Architecture Capability Framework](./architecture-capability-framework.md)
- [TOGAF Fundamentals](./togaf-fundamentals.md)
