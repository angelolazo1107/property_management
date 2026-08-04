# Phase 10 Odoo Go-Live Preparation, Cutover Plan & Readiness Checklist

**Project**: Odoo 19 Property Management Implementation  
**Phase**: Phase 10 (Week 11 to Week 12 Cutover)  
**Document Version**: 1.0  
**Target Audience**: Executive Sponsor, Steering Committee, System Administrator, Department Heads

---

## 1. Executive Summary & Go-Live Strategy

This document outlines the **Go-Live Readiness Criteria**, **Data Cutover Protocol**, **First Live Transaction Checklist**, and **System Administrator Handover Notes** for launching Odoo Phase 1 into production.

### Cutover Timeline:
* **Data Freeze Date**: End of Week 11
* **Final Master Data Upload**: Day 1 of Week 12
* **System Go-Live Date**: Day 1 of Week 12 (Official Start of Live Operations)
* **Stabilization Period**: Week 13 through Week 14

---

## 2. Go-Live Readiness Gatekeeping Checklist

All items below must be verified and marked **DONE** prior to securing Management Go-Live Sign-Off.

| # | Checklist Item | Responsible | Status (Done/Pending) | Verification Evidence / Notes |
|---|---|---|---|---|
| 1 | Production database initialized on Odoo.sh | System Admin | Done | Production instance active with SSL & backups. |
| 2 | Core Odoo & `property_management_custom` module installed | Implementation Team | Done | App upgraded cleanly to latest release. |
| 3 | User accounts created & assigned to Security RBAC Groups | IT / HR / Admin | Done | Security groups assigned (`Leasing`, `PMO`, `Procurement`, `Finance`). |
| 4 | Master Data uploaded & validated (Tenants, Units, Suppliers, Products, Vehicles) | Data Owners | Done | Dry-run validation log passed with 0 errors. |
| 5 | Governance Approval Matrix rules configured | Management | Done | PR, PO, Canvass, JO, Refund, and Exception thresholds active. |
| 6 | Document folder structure & tagging categories configured | Document Controller | Done | Document categories initialized. |
| 7 | Chart of Accounts, Journals, Taxes & Payment Terms configured | Finance Controller | Done | COA accounts mapped for rental income & deposits. |
| 8 | Website inquiry form & CRM lead routing configured | Marketing / Leasing | Done | Website inquiries generate CRM leads with source='website'. |
| 9 | Helpdesk ticket & Maintenance stages configured | PMO / Maintenance | Done | Ticket intake & Job Order integration verified. |
| 10 | Executive Dashboards & Graph/Pivot views verified | Management | Done | Pipeline, collections, job cost, and clearance charts available. |
| 11 | Department UAT Test Scripts executed & signed off | Process Owners | Done | UAT Pack signed off by all department heads. |
| 12 | User Training completed & quick guides distributed | Training Lead | Done | quick guides provided to all system users. |
| 13 | Support Helpdesk & Incident Escalation channel setup | Support Lead | Done | Support email/chat channel active. |
| 14 | Management Go-Live Approval secured | Project Sponsor | Done | Executive sign-off document executed. |

---

## 3. Data Cutover Procedure

### Master Data Freeze Rules:
1. **Freeze Notice**: All legacy spreadsheet/manual master data edits must stop 48 hours before Go-Live.
2. **Delta Capture**: Any urgent legacy transactions created during the 48-hour freeze window must be logged manually and entered into Odoo on Day 1 of Go-Live.

### Cutover Execution Steps:
```
[Step 1: Data Freeze] ➔ [Step 2: Delta Extract] ➔ [Step 3: Final Import Script Execution] ➔ [Step 4: Audit Check] ➔ [Step 5: System Opening]
```

1. **Step 1 (Day -2)**: Issue Data Freeze announcement to all departments.
2. **Step 2 (Day -1)**: Run [import_master_data.py](file:///c:/Users/Angelo/Desktop/property_management/import_master_data.py) pre-validation audit check.
3. **Step 3 (Day -1)**: Run live XML-RPC master data upload to Production instance.
4. **Step 4 (Day -1)**: Validate record counts for Tenants (`res.partner`), Units (`product.product`), Suppliers, and COA (`account.account`).
5. **Step 5 (Day 1)**: Set system transaction opening date in Odoo.

---

## 4. First Live Transaction Verification Checklist

On Day 1 of Go-Live, the implementation team shall shadow department users as they execute the **22 First Live Transactions**:

- [ ] **1. Create Website Inquiry / CRM Lead**
- [ ] **2. Schedule Ocular Visit**
- [ ] **3. Generate Leasing Quotation**
- [ ] **4. Create Unit Reservation & Verify Deposit Payment**
- [ ] **5. Submit & Approve Tenant BIS Application**
- [ ] **6. Issue & Execute Lease Contract**
- [ ] **7. Validate 9-Checkpoint Move-In Clearance**
- [ ] **8. Perform PMO Move-In Inspection & Utility Meter Reading**
- [ ] **9. Auto-Generate First Monthly Recurring Billing**
- [ ] **10. Post & Dispatch Customer Invoice**
- [ ] **11. Create Helpdesk Ticket & PMO Job Order**
- [ ] **12. Perform Unit Assessment & Turnover Task**
- [ ] **13. Create Purchase Requisition (PR)**
- [ ] **14. Attach 3-Supplier Canvass Sheet & Obtain GM PO Approval**
- [ ] **15. Confirm Purchase Order (PO)**
- [ ] **16. Validate Goods Receipt (GR)**
- [ ] **17. Verify Automated Procurement 3-Way Match**
- [ ] **18. Submit Office Supplies Requisition (OSR)**
- [ ] **19. Record Vehicle Errand & Driver Trip Log**
- [ ] **20. Process Departmental Move-Out Exit Clearance**
- [ ] **21. Execute Security Deposit Refund Bank Wire Payout**
- [ ] **22. Review Executive Dashboard Graphs & Pivots**

---

## 5. System Administrator Handover Notes

### System Credentials & Architecture Summary:
* **Hosting Platform**: Odoo.sh Enterprise Cloud
* **Custom Repository**: `https://github.com/angelolazo1107/property_management.git`
* **Custom Module**: [property_management_custom](file:///c:/Users/Angelo/Desktop/property_management/property_management_custom)
* **Odoo Version**: 19.0 Enterprise

### Routine Maintenance & Cron Schedule:
| Cron Job Name | Model | Frequency | Purpose |
|---|---|---|---|
| Monthly Draft Billing Generator | `recurring.monthly.billing` | Monthly (1st) | Auto-creates draft monthly billing records for active leases. |
| Monthly Invoice Dispatch | `recurring.monthly.billing` | Monthly (5th) | Validates and dispatches monthly invoices. |
| Daily Overdue Escalation Engine | `recurring.monthly.billing` | Daily | Audits overdue days and triggers 3/7/15-day escalation alerts. |
| Property Reservation Auto-Expiry | `property.reservation` | Daily | Auto-expires unpaid reservations past 5 days and releases units. |
| Lease Expiration Expiry Engine | `lease.contract` | Daily | Triggers 60, 30, 15, and 7-day expiration reminders and holdover penalties. |

### Incident Support Escalation Matrix:
* **Level 1 (User Guidance / Login Issues)**: Internal IT Administrator
* **Level 2 (Workflow / Configuration Adjustment)**: PMO & Leasing Systems Super-Users
* **Level 3 (Code / Database / Server Issues)**: Odoo Implementation Lead & Coretech Support Team

---

## 6. Executive Management Go-Live Sign-Off

The undersigned agree that the Odoo Phase 1 system has met all functional requirements, UAT sign-offs, data migration validations, and training criteria, and is formally approved for **Live Operations**.

| Role | Name | Signature | Date |
|---|---|---|---|
| **Project Sponsor / General Manager** | | | |
| **Leasing Manager** | | | |
| **PMO Operations Manager** | | | |
| **Finance Controller** | | | |
| **Odoo Implementation Lead** | | | |
