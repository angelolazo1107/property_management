# Odoo 19.4 Studio Configuration Guide (Property Management)

This guide provides step-by-step instructions for customizing standard Odoo Enterprise apps on **Odoo.sh** using **Odoo Studio**, matching the requirements of the Process Assessment Report.

---

## 1. CRM Module Configuration (Inquiries & Lead-to-Lease)

### Navigation: `CRM > Pipeline` -> Open Odoo Studio

#### A. Custom Fields on `crm.lead` Model
Add the following fields via Studio onto the CRM Lead form view:
1. **Target Unit / Property** (`x_studio_target_unit`): Many2one field linked to `product.product` or Custom Unit model.
2. **Ocular Visit Date** (`x_studio_ocular_visit_date`): Date & Time field.
3. **Ocular Visit Status** (`x_studio_ocular_status`): Selection field (`Scheduled`, `Completed`, `Cancelled`, `Rescheduled`).
4. **Buyer/Tenant Information Sheet (BIS) Data** (`x_studio_bis_status`): Selection field (`Draft`, `Submitted`, `Verified`, `Rejected`).
5. **Reservation Deposit Proof** (`x_studio_reservation_proof`): Attachment / Binary field.
6. **Lease Intended Start Date** (`x_studio_intended_move_in`): Date field.

#### B. Pipeline Stages
Update the Stage bar in CRM to represent the Leasing funnel:
`New Inquiry` ➔ `Ocular Visit` ➔ `Quotation / Proposal` ➔ `Reservation & BIS` ➔ `Legal & Contract` ➔ `Move-In Clearance` ➔ `Won (Active Tenant)`.

---

## 2. PMO & Operations (Move-in, Move-out & Job Orders)

### Navigation: `Helpdesk / Maintenance` -> Open Odoo Studio

#### A. Move-In & Move-Out Inspection Checklists (`maintenance.request` or `helpdesk.ticket`)
Add fields for PMO inspections:
1. **Inspection Type** (`x_studio_inspection_type`): Selection (`Move-In Baseline`, `Move-Out Turnover`, `Routine PMO`).
2. **Unit Condition Rating** (`x_studio_unit_condition`): Selection (`Pass`, `Conditional`, `Fail - Repairs Needed`).
3. **Electricity Meter Reading** (`x_studio_electric_reading`): Float field.
4. **Water Meter Reading** (`x_studio_water_reading`): Float field.
5. **Keys & Access Badges Count** (`x_studio_access_items_returned`): Integer / Text field.
6. **Tenant Acknowledgment Signature** (`x_studio_tenant_signature`): Signature field.

#### B. Automated Action (Studio Automation)
* **Trigger:** When Stage changes to `Move-Out Final Inspection`.
* **Action:** Automatically create an Activity assigned to the Accounting team: *"Verify outstanding utility balances and security deposit deductions for tenant."*

---

## 3. Procurement Controls (PR, PO & 3-Way Match)

### Navigation: `Purchase App` -> Open Odoo Studio

#### A. Purchase Request & Canvassing Fields (`purchase.order` / custom model)
1. **PR Justification** (`x_studio_pr_justification`): Text area.
2. **Comparison / Canvass Sheet Attachment** (`x_studio_canvass_attachment`): Binary / Attachment field.
3. **Department Head Approval** (`x_studio_dept_head_approved`): Boolean + Date + User signature block.
4. **General Manager Approval** (`x_studio_gm_approved`): Boolean + Date + User signature block.

#### B. Approval Rules (Studio Approval Checkpoints)
* Add a Studio **Approval Button** on the Purchase Order `Confirm Order` button:
  * **Rule 1:** Requires `Department Head` approval for amounts > 0.
  * **Rule 2:** Requires `General Manager` approval for amounts > 50,000.

---

## 4. Admin & Fleet Services

### Navigation: `Fleet App` -> Open Odoo Studio

#### A. Custom Fields on Fleet Vehicle Logs (`fleet.vehicle.log.services`)
1. **Trip Purpose** (`x_studio_trip_purpose`): Selection (`Internal Errand`, `Guest Transport`, `Property Inspection`, `Maintenance`).
2. **Is Chargeable to Tenant** (`x_studio_is_chargeable`): Boolean.
3. **Chargeable Tenant Account** (`x_studio_chargeable_tenant`): Many2one (`res.partner`).
4. **Driver Trip Mileage Start/End** (`x_studio_mileage_start`, `x_studio_mileage_end`): Integer fields.
5. **Accounting Billing Clearance** (`x_studio_accounting_cleared`): Boolean.

---

## 5. Accounting Verification Layer

### Navigation: `Accounting > Vendor Bills / Customer Invoices` -> Open Odoo Studio

#### Studio Approval Rules for Financial Actions
1. **Deposit Refund Control:** Security Deposit refund invoices/bills require `Accounting Manager` validation signature before payment posting.
2. **3-Way Match Checkpoint:** Vendor bills cannot be marked `Paid` without an attached `Goods Receipt` document reference.

---

## 6. Sales App: Quotation & Reservation Setup (Stage 3)

### Navigation: `Sales > Quotation Templates / Products` -> Open Odoo Studio

#### A. Custom Line Item Products & Accounting Mappings
Navigate to `Sales > Products > Products` and ensure the following 8 products exist with respective Accounting treatment:
1. **Monthly Rental** (Service -> Income Account `400100 - Rental Income`)
2. **Furniture Rental Fee** (Service -> Income Account `400200 - Furniture Rental Income`)
3. **Parking Space Rental Fee** (Service -> Income Account `400300 - Parking Fee Income`)
4. **Wi-Fi / Internet Subscription Fee** (Service -> Income Account `400400 - Internet Fee Income`)
5. **Building Access Card Fee** (Service -> Income Account `400500 - Access Card Fee Income`)
6. **Pet Registration & Permit Fee** (Service -> Income Account `400900 - Pet Registration & Other Income`)
7. **Lease Reservation Deposit Fee** (Service -> Current Liability `210100 - Unearned Revenue / Customer Deposit`)
8. **Lease Security Deposit** (Service -> Current Liability `210200 - Security Deposit Payable`)

#### B. Quotation Templates Configuration
Navigate to `Sales > Configuration > Quotation Templates`:
1. **Bare Unit Rental**: Monthly Rental + Lease Reservation Deposit Fee + Lease Security Deposit.
2. **Furnished Unit Rental**: Monthly Rental + Furniture Rental Fee + Reservation Fee + Security Deposit.
3. **Rental with Parking**: Monthly Rental + Parking Space Fee + Reservation Fee + Security Deposit.
4. **Rental with Wi-Fi**: Monthly Rental + Wi-Fi Subscription Fee + Reservation Fee + Security Deposit.
5. **Rental with Access Card**: Monthly Rental + Access Card Fee + Reservation Fee + Security Deposit.
6. **Rental with Pet Registration**: Monthly Rental + Pet Registration Fee + Reservation Fee + Security Deposit.

#### C. Quotation Form Customization (`sale.order`)
Add custom fields onto `sale.order` via Studio or backend XML module:
* **Target Property Unit** (`target_unit_id`): Linked to `product.product`.
* **Intended Move-In Date** (`intended_move_in_date`): Date.
* **Lease Duration** (`lease_term_months`): Integer (default: 12).
* **Reservation Deposit Structure** (`reservation_fee_option`): Selection (`PHP 5,000`, `PHP 10,000`, `Custom`).
* **Proof of Payment Upload** (`reservation_proof`): Binary Attachment.
* **Reservation Status** (`reservation_payment_status`): Selection (`Pending`, `Submitted to Billing`, `Verified`, `Receipt Issued`).
* **Acknowledgement Receipt Ref** (`acknowledgement_receipt_no`): Char / Sequence.

---

## 8. Reservation Record Custom Model (`property.reservation`)

### Navigation: `CRM / Sales > Unit Reservations`

#### Model Fields & Controls (`property.reservation`):
1. **Tenant / Client** (`tenant_id`): Many2one to `res.partner`.
2. **Reserved Unit** (`unit_id`): Many2one to `product.product`.
3. **Reservation Fee Preset** (`reservation_amount_preset`): Selection (`PHP 5,000`, `PHP 10,000`, `Custom`).
4. **Reservation Amount** (`reservation_amount`): Monetary.
5. **Reservation Date Paid** (`reservation_date`): Date.
6. **Expiration Date** (`expiration_date`): Date (Optional).
7. **Payment Status** (`payment_status`): Selection (`Unpaid`, `For Verification`, `Paid`).
8. **Proof of Payment** (`proof_of_payment`): Binary attachment.
9. **Acknowledgement Receipt No.** (`acknowledgement_receipt_no`): Char (Auto-generated `AR-2026-XXXXX`).
10. **Billing Copy Attached** (`billing_copy_attached`): Boolean.
11. **Tenant Copy Issued** (`tenant_copy_issued`): Boolean.
12. **Reservation Status** (`state`): Selection (`Draft`, `For Payment`, `Paid & Reserved`, `Expired`, `Converted`, `Cancelled`).
13. **Manager Approval** (`manager_approval`): Boolean (Required for cancellation).
14. **Cancellation Reason** (`cancellation_reason`): Text.

#### Automated Business Controls:
* **Payment Confirmation Unit Lock:** Unit occupancy status changes to `Reserved` **ONLY AFTER** payment confirmation.
* **Lease Conversion:** Paid reservation converts into active lease contract and applies customer advance deposit.
* **Manager Cancellation Enforcement:** Cancellation button blocks execution if `manager_approval` is False, ensuring management policy compliance.



