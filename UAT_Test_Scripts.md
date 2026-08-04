# Phase 1 Odoo User Acceptance Testing (UAT) Test Scripts & Validation Pack

**Project**: Odoo 19 Property Management Implementation  
**Target System**: Odoo Enterprise (Property Management Extensions)  
**Document Version**: 1.0  
**Sign-Off Requirement**: All Critical & Major test scenarios must be executed and signed off by Department Process Owners prior to Go-Live.

---

## Executive Summary & Instructions for Testers

This document contains step-by-step User Acceptance Testing (UAT) scripts for the 19 core business process scenarios.

### Tester Guidelines:
1. Perform test steps sequentially.
2. Record the status for each step (`Pass`, `Fail`, `Blocked`).
3. If a step fails, record details in the **UAT Issue Log** section with severity (`Critical`, `Major`, `Minor`, `Enhancement`).
4. Sign and date your department section upon completion.

---

## 1. CRM & Leasing Workstream

### UAT-SCRIPT-01: Website Inquiry to CRM Lead Routing
* **Target Model**: `crm.lead`
* **Department**: Leasing / Marketing
* **Objective**: Verify that website inquiries create CRM leads with proper unit preferences.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 1.1 | Open Website Inquiry form or create lead in CRM (`CRM > Pipeline`). | New lead record created. | | |
| 1.2 | Select **Target Unit / Property**, Intended Move-In Date, and Budget. | Target Unit links to `product.product`. | | |
| 1.3 | Check Parking, Wi-Fi, or Pet requirements. | Requirement flags saved on Lead. | | |
| 1.4 | Move Lead stage to `Ocular Visit`. | Lead stage updates to Ocular Visit. | | |

---

### UAT-SCRIPT-02: Ocular Visit Scheduling & Security Gate Pass
* **Target Model**: `ocular.visit`, `visitor.gate.pass`
* **Department**: Leasing / PMO Security
* **Objective**: Schedule ocular visit and generate security visitor gate pass.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 2.1 | From CRM Lead, click **Ocular Visits** stat button -> `Create`. | Ocular visit form opens with lead pre-filled. | | |
| 2.2 | Set visit date, time, visitor name, and contact details. | Schedule saved. | | |
| 2.3 | Click **Schedule Visit & Notify Security**. | Ocular status becomes `scheduled`. Visitor Gate Pass created. | | |
| 2.4 | Click **Mark Visit Completed**. | Status updates to `completed`. | | |

---

### UAT-SCRIPT-03: Leasing Quotation Creation & Template Selection
* **Target Model**: `sale.order`
* **Department**: Leasing / Sales
* **Objective**: Generate itemized leasing quotation using pre-configured templates.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 3.1 | On CRM Lead, click **Create Leasing Quotation**. | Sales Order created with tenant info. | | |
| 3.2 | Select quotation template (e.g. `Furnished Unit Rental` or `Rental with Parking`). | Line items populate (Rent, Deposit, Parking, Wi-Fi). | | |
| 3.3 | Confirm price unit matches target unit list price. | Unit list price populated automatically. | | |
| 3.4 | Send quotation by email or confirm order. | Quotation sent or confirmed. | | |

---

### UAT-SCRIPT-04: Unit Reservation Payment Verification & Hold
* **Target Model**: `property.reservation`
* **Department**: Leasing / Billing Accounting
* **Objective**: Verify reservation deposit payment and lock property unit status.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 4.1 | Navigate to `CRM > Unit Reservations` -> `Create`. | Reservation form opens. Auto-ref `RES-YYYY-#####`. | | |
| 4.2 | Select Tenant, Target Unit, and Fee Structure (e.g. `PHP 5,000`). | Fee amount populated. | | |
| 4.3 | Attach proof of payment and click **Submit Payment for Verification**. | State updates to `for_verification`. | | |
| 4.4 | Click **Verify Payment & Issue AR**. | Payment verified. Auto Acknowledgement Receipt (`AR-#####`) issued. Unit `occupancy_status` becomes `reserved`. | | |

---

### UAT-SCRIPT-05: Buyer/Tenant Information Sheet (BIS) Application
* **Target Model**: `tenant.application.bis`
* **Department**: Leasing / Legal / Billing
* **Objective**: Process tenant background info sheet and ID validation.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 5.1 | Navigate to `CRM > Tenant BIS Applications` -> `Create`. | BIS form opens. Auto-ref `BIS-YYYY-#####`. | | |
| 5.2 | Attach **Valid ID** and **Proof of Income**. | Attachments saved. | | |
| 5.3 | Click **Submit to Billing Review**. | State updates to `billing_review`. Valid ID gate enforced. | | |
| 5.4 | Click **Submit to Legal Review**. | State updates to `legal_review`. Both ID & Income proof enforced. | | |
| 5.5 | Click **Approve BIS**. | State updates to `approved`. Lease contract auto-created & tenant document subfolders initialized. | | |

---

### UAT-SCRIPT-06: Lease Contract Preparation & Notarization
* **Target Model**: `lease.contract`
* **Department**: Leasing / Legal
* **Objective**: Execute contract lifecycle from draft to notarized released copy.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 6.1 | Open Lease Contract (`LEASE-YYYY-PROPERTY-UNIT-#####`). | Contract form displays financial terms & legal clauses. | | |
| 6.2 | Click **Send for Signing** -> **Mark Signed by Tenant**. | Attached signed copy enforced before stage update. | | |
| 6.3 | Click **Submit to Billing** -> **Forward to Legal for Notarization**. | Stage updates to `submitted_legal`. | | |
| 6.4 | Click **Notarize Contract** -> **Release Executed Copy**. | Notary status set to `done`, stage `released_tenant`. | | |

---

### UAT-SCRIPT-07: 9-Checkpoint Move-In Clearance Gatekeeping
* **Target Model**: `lease.contract`
* **Department**: PMO / Billing / Accounting
* **Objective**: Verify strict 9-point financial & operational move-in clearance checks.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 7.1 | Click **Create Move-In Settlement Invoice**. | Itemized Move-In invoice created (`account.move`). | | |
| 7.2 | Post and register payment on Move-In invoice. | Invoice marked `paid`. | | |
| 7.3 | Click **Validate Move-In Readiness (9 Checkpoints)**. | System validates 9 points (Reservation, Invoice, Deposit, Cards, Parking, Wi-Fi, Contract, Assessment, Inspection). | | |
| 7.4 | Verify outcome upon successful validation. | `move_in_cleared` becomes `True`, stage updates to `active`, property unit `occupancy_status` becomes `occupied`. | | |

---

## 2. PMO & Maintenance Workstream

### UAT-SCRIPT-08: PMO Move-In Inspection & Utility Meter Baseline
* **Target Model**: `pmo.inspection`, `pmo.utility.reading`
* **Department**: PMO / Maintenance
* **Objective**: Record move-in inspection checklist and baseline electric/water meter readings.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 8.1 | Navigate to `PMO Operations > Move-In/Out Inspections` -> `Create`. | Inspection form opens (`Move-In Baseline`). | | |
| 8.2 | Fill unit condition ratings and key/access badge counts. | Inspection data saved. | | |
| 8.3 | Navigate to `PMO Operations > Electric & Water Readings` -> `Create`. | Utility reading form opens. Auto-ref `UTIL-#####`. | | |
| 8.4 | Enter current electric (kWh) and water (cbm) readings. Click **Verify Reading**. | Status becomes `verified`. Unit `latest_electric_reading` and `latest_water_reading` updated. | | |

---

### UAT-SCRIPT-09: Unit Assessment & Turnover Task (11-Point Check)
* **Target Model**: `unit.assessment.task`
* **Department**: PMO Admin / Housekeeping
* **Objective**: Perform unit turnover assessment replacing external SARA tool.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 9.1 | Navigate to `PMO Operations > Unit Assessments & Turnover` -> `Create`. | Assessment task created. | | |
| 9.2 | Execute 11-point physical checklist (Cleanliness, Damage, Lights, HVAC, Plumbing, Locks, Windows, Furniture, Photos, Admin Sign-off, Housekeeping Sign-off). | All 11 points checked. | | |
| 9.3 | Click **Pass & Mark Ready for Move-In**. | Task stage set to `ready_move_in`. Unit status updated to `available`. | | |

---

### UAT-SCRIPT-10: Helpdesk Ticket to PMO Job Order & Payment Control
* **Target Model**: `helpdesk.ticket`, `pmo.job.order`
* **Department**: Helpdesk / Maintenance / Accounting
* **Objective**: Route helpdesk ticket to PMO Job Order with payment-before-work enforcement.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 10.1 | Create Helpdesk Ticket (`Helpdesk > Tickets`). Click **Convert to PMO Job Order**. | Job Order created (`JO-YYYY-#####`). | | |
| 10.2 | Set `is_chargeable = True` and enter Estimated Job Cost. | Costing recorded. | | |
| 10.3 | Try clicking **Schedule MST Maintenance** while `payment_verified` is False. | System blocks scheduling with payment validation error. | | |
| 10.4 | Check `payment_verified = True` (or GM Waiver) and click **Schedule MST Maintenance**. | MST scheduling allowed. Stage set to `scheduled`. | | |

---

## 3. Accounting & Billing Workstream

### UAT-SCRIPT-11: Recurring Monthly Billing Batch Generation
* **Target Model**: `recurring.monthly.billing`
* **Department**: Accounting / Billing
* **Objective**: Auto-generate recurring rental invoices on 1st of month and dispatch on 5th.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 11.1 | Navigate to `Leasing Finance > Monthly Billing & Collections` -> `Create` (or run 1st-of-month cron). | Billing record created (`BILL-YYYY-MM-#####`). Charges populated from active lease. | | |
| 11.2 | Click **Generate Draft Invoice**. | Draft customer invoice (`account.move`) created. | | |
| 11.3 | Click **Validate & Send Invoice**. | Invoice posted, status set to `sent`, collection status set to `due`. | | |

---

### UAT-SCRIPT-12: Overdue Escalation Engine (3, 7, 15 Days)
* **Target Model**: `recurring.monthly.billing`
* **Department**: Accounting / Finance / Legal
* **Objective**: Verify automated overdue days audit and 3-level escalation engine.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 12.1 | On an unpaid billing record past due date, click **Run Overdue Escalation Engine**. | Overdue days calculated. | | |
| 12.2 | If overdue >= 3 days: | Escalation level set to `level_1` (1st Payment Reminder). | | |
| 12.3 | If overdue >= 7 days: | Escalation level set to `level_2` (Manager Escalation). | | |
| 12.4 | If overdue >= 15 days: | Escalation level set to `level_3` (Legal & Executive Escalation). | | |

---

### UAT-SCRIPT-13: Move-Out Clearance & 8-Departmental Sign-Offs
* **Target Model**: `move.out.clearance`
* **Department**: PMO / Billing / IT / Security / Legal / Finance
* **Objective**: Process move-out exit clearance with 8 mandatory departmental sign-offs.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 13.1 | Navigate to `PMO Operations > Move-Out Clearances` -> `Create`. | Clearance ref created (`MCLR-YYYY-#####`). | | |
| 13.2 | Select Lease Contract. | Tenant, unit, deposit, and unpaid balance auto-populate. | | |
| 13.3 | Check 8 departmental clearances (Billing, Admin, Housekeeping, IT, Security, Parking, Legal, Finance). | Checkboxes toggled. | | |
| 13.4 | Click **Approve Finance SOA Clearance** -> **Grant Final Exit Clearance**. | Exit clearance granted. | | |
| 13.5 | Click **Close Move-Out File**. | Lease contract terminated. Unit status set to `vacated`. | | |

---

### UAT-SCRIPT-14: Security Deposit Refund & Bank Wire Settlement
* **Target Model**: `security.deposit.refund`
* **Department**: Accounting / Finance
* **Objective**: Process security deposit refund with bank wire details and journal entry.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 14.1 | Navigate to `Leasing Finance > Security Deposit Refunds` -> `Create`. | Refund ref created (`REFUND-YYYY-#####`). | | |
| 14.2 | Select Move-Out Clearance. | Original deposit, deductions, and net refundable amount populated. | | |
| 14.3 | Enter Bank Name, Account Name, and Account Number. Click **Submit Refund Application**. | Bank credentials validated. | | |
| 14.4 | Click **Finance Approve Payout**. | Finance approved. Misc Accounting Journal Entry clearing liability created. | | |
| 14.5 | Attach proof of wire transfer and click **Mark Refund Paid**. | Payment status set to `paid`. Lease stage set to `deposit_refund`. | | |

---

## 4. Procurement, Fleet & Admin Workstream

### UAT-SCRIPT-15: Purchase Requisition, 3-Supplier Canvass & PO Approval
* **Target Model**: `purchase.order`, `procurement.approval`
* **Department**: Procurement / Management
* **Objective**: Enforce 3-supplier comparison sheet and multi-level approval matrix.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 15.1 | Create Purchase Order (`Purchase > Purchase Orders`). Fill PR ref and justification. | PO created. | | |
| 15.2 | Attach 3-Supplier Canvass Sheet and fill Supplier 1, 2, and 3 quotes. | Canvass details attached. | | |
| 15.3 | Click **Dept Head Approve PR** and **GM Approve PO**. | Approvals recorded with user ID and timestamp. | | |
| 15.4 | Click **Confirm Order**. | Confirm order succeeds. (Blocked if approvals missing). | | |

---

### UAT-SCRIPT-16: Automated Procurement 3-Way Match Checkpoint
* **Target Model**: `purchase.order`
* **Department**: Procurement / Accounting
* **Objective**: Verify automated 3-way match sync upon Goods Receipt and Vendor Bill.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 16.1 | On confirmed PO, receive products and validate Goods Receipt (`stock.picking` state `done`). | `goods_receipt_matched` automatically becomes `True`. | | |
| 16.2 | Create and post Vendor Bill (`account.move` state `posted`). | `invoice_matched` automatically becomes `True`. | | |
| 16.3 | Verify 3-way match completion. | `three_way_match_verified` and `payment_request_cleared` automatically set to `True`. | | |

---

### UAT-SCRIPT-17: Office Supplies Requisition (OSR) & Auto-PR Trigger
* **Target Model**: `office.supply.request`
* **Department**: Admin / Warehouse / Procurement
* **Objective**: Requisition office supplies, check inventory stock, and auto-trigger PR if out of stock.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 17.1 | Navigate to `Purchases > Office Supply Requisitions` -> `Create`. | Requisition form created (`SUPPLY-YYYY-#####`). | | |
| 17.2 | Add requested supply items and quantities. Click **Dept Head Approve**. | Status set to `dept_approved`. | | |
| 17.3 | If stock is available, click **Stock Available** -> **Release Supplies**. | Status set to `released`. | | |
| 17.4 | If out of stock, click **Out of Stock - PR Required**. | Status set to `pr_raised`. Auto PR ref generated (`PR-OSR-SUPPLY-#####`). | | |

---

### UAT-SCRIPT-18: Vehicle Request & Driver Trip Log
* **Target Model**: `fleet.trip.request`
* **Department**: Admin / Fleet Services / Accounting
* **Objective**: Record vehicle errand/special client trip, odometer mileage, and GSD collection.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 18.1 | Navigate to `Fleet > Vehicle Trips & Fleet Logs` -> `Create`. | Trip request created (`TRIP-YYYY-#####`). | | |
| 18.2 | Select Vehicle, Driver, Passenger, Destination, and Trip Category (`internal_errand` vs `special_client`). | Details recorded. | | |
| 18.3 | Enter Odometer Start and End mileage. | Total distance (km) computed automatically. | | |
| 18.4 | Click **Complete Trip** -> **Accounting Verify & Close**. | Trip verified and closed. Billing rate & GSD AR ref logged. | | |

---

## 5. Executive Dashboards & Analytics Workstream

### UAT-SCRIPT-19: Executive Dashboard Graph & Pivot Views
* **Target Models**: `lease.contract`, `recurring.monthly.billing`, `pmo.job.order`, `move.out.clearance`
* **Department**: Executive Management / Department Heads
* **Objective**: Verify interactive graph charts and pivot data tables.

| Step | Action | Expected Outcome | Result (Pass/Fail) | Tester Initials |
|---|---|---|---|---|
| 19.1 | Navigate to `CRM > Lease Contracts Pipeline`. Click **Graph View** and **Pivot View** icons in top-right. | Bar chart by contract stage and pivot rent matrix display cleanly. | | |
| 19.2 | Navigate to `Leasing Finance > Monthly Billing & Collections`. Toggle Graph & Pivot views. | Collection status chart and billing cycle pivot table display. | | |
| 19.3 | Navigate to `PMO Operations > Job Orders & Maintenance`. Toggle Graph & Pivot views. | Job order expense chart by category and maintenance pivot display. | | |
| 19.4 | Navigate to `PMO Operations > Move-Out Clearances`. Toggle Graph & Pivot views. | Exit reason chart and deposit deduction pivot display. | | |

---

## 📋 UAT Sign-Off & Defect Logging Sheet

### Defect Log Template
| Defect ID | UAT Script Ref | Description / Observed Behavior | Severity (Critical/Major/Minor) | Assigned Developer | Resolution Status |
|---|---|---|---|---|---|
| DEF-001 | UAT-SCRIPT-XX | | | | |

### Department Sign-Off Matrix
| Department | Process Owner Name | Signature | Date | Overall Result (Approved / Conditional) |
|---|---|---|---|---|
| Leasing & Sales | | | | |
| PMO & Admin | | | | |
| Maintenance / MST | | | | |
| Procurement & Inventory | | | | |
| Accounting & Finance | | | | |
| Executive Sponsor | | | | |
