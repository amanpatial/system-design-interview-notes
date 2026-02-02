# Architecture Governance

## Introduction

Architecture Governance ensures that architecture development and implementation proceeds according to established policies, principles, and standards.

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Architecture Board** | Cross-functional group with responsibility for architecture governance |
| **Architecture Compliance** | Process ensuring implementation aligns with architecture |
| **Architecture Contract** | Joint agreement between parties on deliverables, quality, and fitness-for-purpose |
| **Dispensation** | Approved deviation from architecture standard |
| **SLA (Service Level Agreement)** | Formal commitment on service characteristics |

---

## Q&A — Architecture Governance

### Basic

**Q: What is the role of an Architecture Board?**

**A:** The Architecture Board provides governance and strategic direction for enterprise architecture.

**Responsibilities:**

- Review and approve architecture artifacts
- Ensure consistency across architecture domains
- Grant dispensations for deviations
- Resolve conflicts between stakeholders
- Monitor compliance with architecture
- Allocate architecture resources

**Composition:**

- Enterprise Architect (chair)
- Domain Architects
- Business representatives
- IT leadership
- Security/Compliance representatives
- Project representatives (as needed)

---

**Q: What is an Architecture Contract?**

**A:** An Architecture Contract is a formal agreement between development partners and sponsors on architecture deliverables.

**Purpose:**

- Define acceptance criteria
- Establish responsibilities
- Set quality expectations
- Enable governance

**Contents:**

- Scope and objectives
- Architecture description
- Architecture requirements
- Success criteria
- Acceptance procedures
- Risks and issues

**Types:**

- **Business-IT Contract:** Between business and IT for solution delivery
- **IT-Vendor Contract:** Between IT and vendors for products/services
- **Business-Business Contract:** Between business units for shared services

---

**Q: What is the Architecture Compliance review process?**

**A:** Architecture Compliance ensures implementations conform to target architecture.

**Process:**

**1. Project Start:**
- Project submits Architecture Compliance assessment request
- Reviews Statement of Architecture Work

**2. During Development:**
- Periodic compliance reviews at key milestones
- Review design documents, prototypes

**3. Pre-Implementation:**
- Final compliance review
- Assess against architecture requirements

**4. Post-Implementation:**
- Lessons learned
- Update architecture repository with as-built

**Outcomes:**

- **Compliant:** Proceed
- **Compliant with Recommendations:** Proceed with noted improvements
- **Non-Compliant:** Must resolve issues or obtain dispensation
- **Rejected:** Cannot proceed

---

### Medium

**Q: How do you handle a situation where a project requests a dispensation from architectural standards?**

**A:** Dispensation Process:

**1. Formal Request:**
- Project submits dispensation request
- Business justification
- Impact analysis
- Proposed mitigation
- Duration of dispensation

**2. Assessment:**
- Architecture team evaluates impact
- Check if similar dispensations exist
- Assess alternatives
- Cost-benefit analysis

**3. Decision Criteria:**

**Grant Dispensation If:**
- Critical business need with tight timeline
- Standard doesn't fit unique requirement
- Cost of compliance > benefit
- Temporary (will be resolved in future)
- Risks are acceptable and mitigated

**Deny Dispensation If:**
- Compromises security or compliance
- Sets bad precedent
- Alternative exists within standards
- Risk is unacceptable

**4. Approval:**
- Document in Governance Log
- Set expiration date
- Define conditions
- Communicate to stakeholders

**5. Monitor:**
- Track dispensation usage
- Review periodically
- Plan remediation if needed

**Example:**
- Request: Use MongoDB instead of standard PostgreSQL
- Justification: Document database better fits unstructured data use case
- Decision: Grant 2-year dispensation; plan data architecture review
- Condition: Must use standard API gateway for integration

---

**Q: Design an Architecture Governance framework for a large organization.**

**A:** Architecture Governance Framework:

**1. Governance Structure:**

**Tiered Boards:**

**Enterprise Architecture Board (Strategic):**
- Meets monthly
- Reviews enterprise-level decisions
- Approves major initiatives
- Sets architectural direction

**Domain Architecture Boards (Tactical):**
- Business, Data, Application, Technology
- Meet bi-weekly
- Domain-specific decisions
- Escalate to Enterprise Board

**Project Architecture Reviews (Operational):**
- Per-project compliance reviews
- Quick turnaround
- Delegate to domain architects

**2. Processes:**

**Architecture Development:**
- ADM governance at each phase
- Gate reviews (Phase A, completion of B-C-D-E, Phase G)
- Stakeholder sign-offs

**Architecture Compliance:**
- Project intake review
- Design review
- Implementation review
- Post-implementation review

**Standards Management:**
- Quarterly standards review
- Proposal → Review → Approval → Publish
- Deprecation process for outdated standards

**3. Policies:**

**Mandatory:**
- Security standards
- Data privacy/governance
- Regulatory compliance
- Audit requirements

**Recommended:**
- Integration patterns
- Technology stack
- Development practices

**4. Metrics & Reporting:**

**KPIs:**
- Architecture compliance rate (target: >90%)
- Dispensation rate (target: <5%)
- Standards adoption (% projects using approved tech)
- Time-to-approval (target: <2 weeks)

**Reports:**
- Monthly governance dashboard
- Quarterly trend analysis
- Annual maturity assessment

**5. Roles & Responsibilities:**

| Role | Responsibility |
|------|---------------|
| Enterprise Architect | Chair Architecture Board, set direction |
| Domain Architects | Domain standards, project reviews |
| Architecture Owners | Maintain segment architectures |
| Project Architects | Ensure project compliance |
| Compliance Officer | Monitor compliance, track metrics |

---

### Complex

**Q: A critical project is behind schedule and asks to skip architecture compliance review. How do you respond while balancing governance and business urgency?**

**A:** Balanced Response Strategy:

**Immediate Assessment:**

**1. Understand Urgency:**
- What is business impact of delay?
- What is risk of non-compliant implementation?
- Is this truly critical or just poor planning?

**2. Risk Analysis:**

**Low Risk Scenarios (Can Expedite):**
- Project uses all standard building blocks
- No integration with critical systems
- Temporary/pilot with limited scope
- Remediation is straightforward

**High Risk Scenarios (Must Review):**
- Security/compliance implications
- Integration with core systems
- Data management/privacy concerns
- Precedent-setting decisions

**Response Options:**

**Option 1: Accelerated Review (Preferred)**
- Fast-track review (48 hours instead of 2 weeks)
- Focus on high-risk areas only
- Conditional approval with follow-up
- Example: "Approved with condition: security review within 30 days post-launch"

**Option 2: Phased Approval**
- Approve MVP with limited scope
- Full review required before production scale
- Example: "Approved for 100-user pilot; full review before enterprise rollout"

**Option 3: Risk-Accepted Waiver**
- Business sponsor formally accepts risks
- Architecture issues documented
- Remediation plan required
- Example: "Launch without API gateway; must implement within 60 days"

**Option 4: No Compromise**
- If risk is truly unacceptable
- Offer alternatives (reduce scope, use existing solution)
- Escalate to executive level

**Communication:**
- Transparent about risks
- Document everything
- Set expectations clearly
- Provide support to meet requirements

**Example Resolution:**
"We'll fast-track review focusing on security and data privacy (our non-negotiables). If those pass, you can proceed with conditional approval. We'll defer the technology standards review to post-launch but require a remediation plan. Business sponsor must formally acknowledge this approach."

**Lessons Learned:**
- Engage architecture earlier in project planning
- Create "express lane" for low-risk projects
- Educate teams on why governance matters

---

**Q: Design a compliance monitoring system that provides ongoing visibility into architecture compliance across 100+ active projects.**

**A:** Architecture Compliance Monitoring System:

**1. Data Collection:**

**Automated Collection:**
- CI/CD pipeline integration (detect tech stack, dependencies)
- Repository scanning (GitLab/GitHub APIs)
- Cloud inventory (AWS Config, Azure Resource Graph)
- API gateway logs (detect integration patterns)
- Service mesh telemetry

**Manual Collection:**
- Project architecture questionnaire (quarterly)
- Compliance self-assessment (project teams)
- Architecture document repository

**2. Compliance Dimensions:**

**Technology Compliance:**
- Approved languages/frameworks (✓ or ✗)
- Library versions (outdated flagged)
- Infrastructure patterns

**Integration Compliance:**
- API standards (OpenAPI documented)
- Event schemas (Avro/Protobuf in registry)
- Authentication (OAuth 2.0, SSO)

**Data Compliance:**
- PII handling (encryption, access controls)
- Data classification labels
- Backup/retention policies

**Security Compliance:**
- Vulnerability scanning results
- Security review completion
- Secrets management (no hardcoded credentials)

**3. Scoring Model:**

**Per-Project Compliance Score:**

**Weighted Categories:**
- Security: 30% (non-negotiable, must be 100%)
- Data: 25%
- Integration: 20%
- Technology: 15%
- Documentation: 10%

**Example:**
- Project A: Security 100%, Data 80%, Integration 90%, Tech 70%, Docs 60%
- Score: (30×1.0 + 25×0.8 + 20×0.9 + 15×0.7 + 10×0.6) / 100 = 86%

**Thresholds:**
- 90-100%: Excellent (green)
- 75-89%: Acceptable (yellow)
- <75%: Non-compliant (red)

**4. Dashboard Views:**

**Executive Dashboard:**
- Portfolio-level compliance: 87% average
- Trends: +3% from last quarter
- Top issues: 15 projects using outdated libraries
- Risk projects: 5 in red zone

**Architecture Team Dashboard:**
- Project-by-project compliance scores
- Drill-down to specific violations
- Dispensation tracking
- Standards adoption rate by category

**Project Team Dashboard:**
- Their project's compliance score
- Specific issues to remediate
- Resources/guidance for remediation
- Timeline for resolution

**5. Alerting & Actions:**

**Proactive Alerts:**
- New vulnerability detected → notify affected projects
- Project score drops below threshold → alert architect
- Dispensation expiring → reminder to renew or remediate
- New standard published → notify teams

**Automated Actions:**
- Block PR if critical security check fails
- Flag PR for architect review if using non-standard tech
- Generate remediation tickets

**6. Remediation Workflow:**

**Issue Detection:**
- Automated scanning identifies non-compliance
- Issue logged with severity and details

**Assignment:**
- Auto-assign to project architect
- Escalate if critical or overdue

**Remediation:**
- Project team fixes issue
- Submit for re-scan
- Architect verifies

**Tracking:**
- SLA for remediation (Critical: 1 week, High: 1 month, Medium: 3 months)
- Metrics on remediation velocity

**7. Reporting:**

**Monthly Report:**
- Compliance trends
- Top violations
- Remediation progress
- Dispensation summary

**Quarterly Business Review:**
- Architecture maturity progress
- Cost of non-compliance (technical debt)
- ROI of governance
- Recommendations for standards updates

**8. Continuous Improvement:**

**Feedback Loop:**
- High violation rate on standard → Review if standard needs update
- Common dispensations → Consider making it a standard
- Compliance metrics inform architecture roadmap

**Example Insights:**
- 40% of projects request MongoDB dispensation → Consider adding NoSQL to standards
- Low API documentation compliance → Invest in better tooling/training
- Excellent security compliance → Share best practices

---

## See Also

- [ADM Phases](./adm-phases.md)
- [Architecture Capability Framework](./architecture-capability-framework.md)
- [Practical Application](./practical-application.md)
