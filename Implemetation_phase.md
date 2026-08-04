Phase 1 Odoo Implementation Plan Schedule
From Kickoff Meeting to Go-Live and Post-Go-Live Stabilization
1. Implementation Overview
This implementation plan defines the recommended schedule, activities, deliverables, responsibilities, dependencies, and acceptance criteria for the Phase 1 Odoo implementation.
The Phase 1 implementation shall cover the following core modules:
1.	Lease Module Package

2.	CRM

3.	Accounting

4.	Sales

5.	Subscriptions

6.	Purchase

7.	Inventory

8.	Approvals

9.	Documents

10.	Studio

11.	Maintenance

12.	Helpdesk

13.	Fleet

14.	Website
The implementation shall cover the following process areas:
1.	Sales / Leasing

2.	Tenant Management

3.	PMO Move-In

4.	PMO Move-Out

5.	PMO Job Order

6.	Maintenance

7.	Tenant Helpdesk / Support

8.	Procurement

9.	Warehouse / Inventory

10.	Office Supplies Request

11.	Vehicle Request

12.	Vehicle Billing and Collection

13.	Accounting and Billing

14.	Approval Management

15.	Document Management

16.	Website Inquiry

17.	Reporting and Dashboards
2. Recommended Implementation Duration
The recommended Phase 1 implementation duration is:
12 weeks core implementation + 2 weeks post-go-live stabilization
Total estimated duration:
14 weeks
The timeline may be adjusted depending on:
1.	Availability of process owners

2.	Completeness of master data

3.	Timely approval of workflow design

4.	Readiness of the Lease Module Package

5.	Complexity of Studio configuration

6.	Number of users and departments

7.	Number of approval levels

8.	UAT participation

9.	Issue resolution speed

10.	Change requests during implementation
________________________________________
3. High-Level Implementation Schedule
Phase	Timeline	Main Objective
Phase 1	Week 1	Kickoff, governance, scope confirmation
Phase 2	Week 1 to Week 2	Business process validation and gap assessment
Phase 3	Week 2 to Week 3	Master data preparation and template finalization
Phase 4	Week 3 to Week 5	Core Odoo module configuration
Phase 5	Week 5 to Week 7	Studio configuration and workflow customization
Phase 6	Week 7 to Week 8	Integration of process flows and internal testing
Phase 7	Week 8 to Week 9	Data upload and validation
Phase 8	Week 9 to Week 10	User Acceptance Testing
Phase 9	Week 10 to Week 11	User training and process walkthrough
Phase 10	Week 11 to Week 12	Go-live preparation and cutover
Phase 11	Week 12	Go-live
Phase 12	Week 13 to Week 14	Post-go-live stabilization and support
________________________________________
4. Detailed Implementation Plan
________________________________________
Phase 1: Project Kickoff and Mobilization
Timeline
Week 1
Objective
To formally start the project, align all stakeholders, confirm project scope, define responsibilities, agree on communication rules, and validate the implementation approach.
Key Activities
Activity	Description	Responsible
Kickoff Meeting	Conduct official project kickoff with management and department heads	Implementer / Client
Project Scope Confirmation	Confirm modules, departments, process coverage, timeline, and exclusions	Project Sponsor / Implementer
Project Team Identification	Identify process owners, key users, approvers, and system administrator	Client
Governance Setup	Define decision makers, escalation path, meeting frequency, and reporting format	Client / Implementer
Communication Channel Setup	Establish email group, chat group, shared document folder, and issue tracker	Project Manager
Initial Risk Review	Identify possible risks such as data delay, approval delay, user availability, or scope change	Project Manager
Document Request List	Issue list of required forms, policies, templates, reports, master data, and approval matrix	Implementer
Required Participants
1.	Project Sponsor

2.	Project Manager

3.	Leasing Process Owner

4.	PMO/Admin Process Owner

5.	Procurement Process Owner

6.	Inventory/Warehouse Process Owner

7.	Accounting/Finance Process Owner

8.	Fleet/Admin Process Owner

9.	Maintenance/Helpdesk Process Owner

10.	Website/Marketing Representative

11.	IT/System Administrator

12.	Odoo Implementation Team
Deliverables
1.	Kickoff meeting minutes

2.	Final confirmed Phase 1 scope

3.	Project governance structure

4.	Communication plan

5.	Responsibility assignment matrix

6.	Initial project timeline

7.	Document and data request list

8.	Risk and issue register template
Output
Project officially started and all stakeholders aligned.
Acceptance Criteria
1.	Project sponsor confirms the implementation scope.

2.	Department process owners are assigned.

3.	Timeline and communication method are agreed.

4.	Required data and document list is acknowledged.
________________________________________
Phase 2: Business Process Validation and Gap Assessment
Timeline
Week 1 to Week 2
Objective
To validate the assessed procedures and convert them into confirmed Odoo workflows.
Key Activities
Workstream	Activities	Responsible
Leasing	Validate CRM inquiry, ocular visit, reservation, BIS, lease contract, move-in, billing, renewal, move-out, and deposit refund	Leasing / Implementer
PMO	Validate move-in, inspection, utility reading, move-out, final inspection, access return, unit acceptance, and filing	PMO/Admin / Implementer
Job Order	Validate tenant request, helpdesk ticket, admin review, job order form, payment verification, MST scheduling, completion, and closure	PMO/Admin / Maintenance
Procurement	Validate PR, department head checking, GM approval, sourcing, canvass, PO, delivery, goods receipt, 3-way match, payment request, and closure	Procurement / Accounting
Inventory	Validate product master, receiving, goods receipt, stock monitoring, office supplies, asset tagging, stock release, and replenishment	Warehouse / Admin
Office Supplies	Validate OSR, department approval, admin review, stock check, item issuance, PR if no stock, procurement, receipt, and distribution	Admin / Warehouse
Vehicle / Fleet	Validate internal errand and special client trip process, billing, GSD collection, AR issuance, trip record, and accounting verification	Admin / Fleet / GSD
Accounting	Validate billing, invoicing, reservation payment, move-in clearance, monthly billing, job order payment, move-out settlement, supplier payment, and vehicle collection	Accounting / Finance
Website	Validate website inquiry form and CRM lead routing	Marketing / Leasing
Approvals	Validate approval categories, approvers, approval levels, and exception handling	Management / Implementer
Documents	Validate required folders, document tags, attachment rules, and access restriction	Admin / Document Controller
Reporting	Validate required dashboards, reports, KPIs, and management views	Management / Implementer
Gap Assessment Areas
Area	Possible Gap
Lease Module Package	Existing package may not fully support assessed process fields
CRM	May require additional fields for unit preference and ocular visit details
Accounting	May require clear mapping of fees, deposits, and revenue accounts
Subscriptions	Monthly rental billing rules must be confirmed
PMO	Move-in and move-out checklists may need Studio configuration
Job Order	Payment-before-work control must be enforced
Procurement	Comparison sheet and PR controls may need Studio fields
Inventory	Asset tagging and stock release process may need additional fields
Fleet	Vehicle billing and collection verification may need Studio models
Documents	Folder access must be defined per department
Approvals	Approval matrix must be finalized before configuration
Website	Inquiry form fields and routing must be approved
Deliverables
1.	Validated process map

2.	Gap assessment report

3.	Final workflow confirmation

4.	Final approval matrix draft

5.	Department process sign-off

6.	Configuration requirement list
Output
All Phase 1 business processes confirmed for Odoo configuration.
Acceptance Criteria
1.	Process owners confirm their workflows.

2.	Gaps are documented.

3.	Required fields, statuses, approvals, and reports are identified.

4.	Management approves the process design for configuration.
________________________________________
Phase 3: Master Data Preparation
Timeline
Week 2 to Week 3
Objective
To prepare and clean the required master data before uploading into Odoo.
Master Data Requirements
Data Category	Required Data
Company Data	Company name, address, tax details, branches, departments
User Data	Employee names, email addresses, roles, departments, access level
Tenant Data	Tenant name, contact details, unit, lease reference, billing details
Unit Data	Building, floor, unit number, unit type, rental amount, occupancy status
Lease Data	Contract details, move-in date, lease term, deposit, rental amount
Product Data	Office supplies, consumables, assets, services, job order items
Supplier Data	Supplier name, contact details, address, terms, email
Customer Data	Tenants, clients, guests, agents, companies
Inventory Data	Stock on hand, unit of measure, category, reorder level
Vehicle Data	Vehicle details, plate number, assigned driver, status
Accounting Data	Chart of accounts, journals, taxes, payment terms, opening references
Approval Data	Approvers, levels, thresholds, categories
Document Data	Existing forms, templates, contracts, receipts, policies
Website Data	Website text, inquiry form fields, contact details
Key Activities
1.	Prepare master data templates.

2.	Issue templates to client process owners.

3.	Collect completed templates.

4.	Review data completeness.

5.	Identify missing or duplicate records.

6.	Clean data with client validation.

7.	Finalize upload-ready files.

8.	Secure sign-off before upload.
Deliverables
1.	Master data templates

2.	Completed client data sheets

3.	Data validation report

4.	Clean master data files

5.	Data upload approval
Output
Master data ready for upload into Odoo.
Acceptance Criteria
1.	Required data templates are completed.

2.	Duplicate and incomplete records are resolved.

3.	Process owners approve data for upload.
________________________________________
Phase 4: Core Odoo Module Configuration
Timeline
Week 3 to Week 5
Objective
To configure the core Odoo modules based on the approved Phase 1 workflows.
Module Configuration Schedule
Module	Configuration Activities	Target Week
Lease Module Package	Configure units, tenants, lease records, statuses, billing reference, move-in/move-out linkage	Week 3
CRM	Configure pipeline, lead stages, lead fields, activities, lead sources, assignment rules	Week 3
Sales	Configure quotation flow, products/services, pricing references, customer records	Week 3
Subscriptions	Configure recurring rental billing structure and recurring invoice references	Week 4
Accounting	Configure COA, journals, taxes, payment terms, receivables, payables, deposit accounts	Week 4
Invoicing	Configure invoice templates, billing items, payment status tracking	Week 4
Purchase	Configure RFQ, PO flow, supplier records, purchase products, approval references	Week 4
Inventory	Configure products, locations, receipts, stock rules, office supplies inventory	Week 4
Approvals	Configure approval categories, approvers, approval paths, required documents	Week 5
Documents	Configure folders, tags, access rights, file routing	Week 5
Maintenance	Configure maintenance teams, equipment/unit repair categories, work stages	Week 5
Helpdesk	Configure teams, ticket categories, stages, assignment rules, SLA if needed	Week 5
Fleet	Configure vehicles, drivers, vehicle request fields, trip record structure	Week 5
Website	Configure inquiry form, contact page, CRM lead generation, routing	Week 5
Key Configuration Activities
1.	Install and activate modules.

2.	Configure company information.

3.	Configure users and access groups.

4.	Configure master data structure.

5.	Configure process stages.

6.	Configure module-specific settings.

7.	Configure document folders.

8.	Configure accounting setup.

9.	Configure approval categories.

10.	Configure CRM lead pipeline.

11.	Configure website inquiry form.

12.	Configure Helpdesk and Maintenance teams.

13.	Configure Fleet vehicle records.
Deliverables
1.	Configured Odoo modules

2.	Configured user roles and access rights

3.	Initial accounting setup

4.	Initial CRM pipeline

5.	Initial lease package setup

6.	Initial purchase and inventory setup

7.	Initial helpdesk, maintenance, fleet, and website setup
Output
Core Odoo modules configured and ready for Studio customization.
Acceptance Criteria
1.	Required modules are installed.

2.	Main module settings are configured.

3.	Process stages are available.

4.	Users can access assigned modules.

5.	Core workflows are ready for detailed configuration.
________________________________________
Phase 5: Odoo Studio Configuration and Workflow Customization
Timeline
Week 5 to Week 7
Objective
To configure required fields, forms, statuses, checklists, dashboards, and workflow controls using Odoo Studio.
Studio Configuration by Process
Process Area	Studio Configuration
Leasing	Inquiry fields, ocular visit fields, reservation fields, BIS fields, lease status, move-in clearance fields, renewal/move-out fields
PMO Move-In	Move-in form fields, inspection checklist, initial meter reading, tenant signing status, turnover status, filing status
PMO Move-Out	Final inspection checklist, damage findings, final meter reading, access return, settlement status, unit acceptance
Job Order	Job order form, service category, rate reference, payment status, MST schedule, completion status
Procurement	PR fields, canvass/comparison sheet fields, PO approval status, payment request checklist
Inventory	Asset tagging fields, stock release form, receiving checklist, low-stock indicator
Office Supplies	OSR form, stock check status, PR required field, distribution status
Vehicle / Fleet	Vehicle request form, billing assessment, collection status, trip record fields
Accounting	Payment verification fields, refund status, deposit deduction, 3-way match status, collection verification
Approvals	Approval categories, required fields, approval status, approver comments
Documents	Document checklist, attachment fields, filing status
Website	Inquiry form fields and CRM routing references
Dashboards	Management KPI fields, filters, pivot and graph views
Key Activities
1.	Create custom fields.

2.	Create custom tabs.

3.	Modify form layouts.

4.	Configure required fields.

5.	Configure conditional visibility where possible.

6.	Configure list views.

7.	Configure Kanban views.

8.	Configure calendar views.

9.	Configure pivot and graph views.

10.	Configure automated activities.

11.	Configure status-based controls.

12.	Configure dashboards.

13.	Configure document attachment fields.
Deliverables
1.	Studio-configured leasing workflow

2.	Studio-configured PMO workflow

3.	Studio-configured job order workflow

4.	Studio-configured procurement fields

5.	Studio-configured inventory and office supplies fields

6.	Studio-configured fleet request fields

7.	Studio-configured accounting verification fields

8.	Studio-configured approval fields

9.	Studio-configured dashboards and reports
Output
Odoo system aligned with assessed operational procedures using Studio-based configuration.
Acceptance Criteria
1.	Required fields are available.

2.	Required process statuses are configured.

3.	Required checklists are available.

4.	Required dashboards are available.

5.	Key controls are represented in the system.
________________________________________
Phase 6: Workflow Integration and Internal Testing
Timeline
Week 7 to Week 8
Objective
To test the end-to-end workflow internally before presenting the system for formal UAT.
Internal Test Scenarios
Test Scenario	Expected Result
Website Inquiry to CRM Lead	Website inquiry creates CRM lead
CRM Lead to Reservation	Lead proceeds to reservation after ocular and quotation
Reservation Payment Verification	Accounting verifies payment and unit is blocked
BIS to Lease Contract	BIS details move into lease processing
Move-In Financial Clearance	Billing and Accounting clearance required before move-in
PMO Move-In	Inspection, utility reading, tenant signing, turnover, filing
Monthly Billing	Active lease generates monthly billing reference
Helpdesk Ticket to Job Order	Ticket becomes job order request
Job Order Payment Verification	No MST scheduling without payment
Move-Out Final Inspection	Final inspection creates billing settlement reference
Deposit Refund	Refund request follows clearance and approval
Office Supplies Request	OSR routes through approval, stock check, issuance or PR
Procurement PR to PO	PR approval, sourcing, PO, delivery, receiving, payment
Goods Receipt and 3-Way Match	PO, receipt, and invoice are matched
Vehicle Request	Vehicle request reviewed, scheduled, recorded, and closed
Special Client Trip	Billing, GSD collection, AR, trip record, Accounting verification
Document Filing	Documents upload, tag, link, and archive correctly
Approval Routing	Requests route to correct approvers
Dashboard Review	Management reports show correct data
Key Activities
1.	Conduct internal configuration review.

2.	Perform sample transactions.

3.	Validate workflow sequence.

4.	Validate required fields.

5.	Validate document attachments.

6.	Validate approval routing.

7.	Validate user access restrictions.

8.	Validate dashboard results.

9.	Record configuration issues.

10.	Apply corrections before UAT.
Deliverables
1.	Internal testing checklist

2.	Internal issue log

3.	Resolved configuration issues

4.	UAT-ready system
Output
System ready for User Acceptance Testing.
Acceptance Criteria
1.	Core workflows can be completed from start to finish.

2.	Critical controls are working.

3.	Major configuration issues are resolved.

4.	UAT test scripts are prepared.
________________________________________
Phase 7: Data Upload and Validation
Timeline
Week 8 to Week 9
Objective
To upload validated master data and confirm that users can transact using actual records.
Data Upload Activities
Data Set	Activity	Responsible
Users	Upload users and assign roles	Implementer / IT
Departments	Configure departments and teams	Implementer / HR/Admin
Tenants	Upload tenant records	Leasing
Units	Upload unit master list	Leasing / Admin
Suppliers	Upload supplier master list	Procurement
Products	Upload products, office supplies, assets, services	Inventory / Procurement
Vehicles	Upload vehicle master list	Fleet/Admin
Accounting	Upload COA, journals, opening references if applicable	Accounting
Approvers	Configure approvers and approval routes	Management / Implementer
Documents	Upload selected templates and required forms	Admin / Document Controller
Website	Upload approved website inquiry content	Marketing / Leasing
Validation Activities
1.	Check duplicate records.

2.	Validate tenant and unit mapping.

3.	Validate supplier records.

4.	Validate product categories.

5.	Validate vehicle records.

6.	Validate accounting accounts and journals.

7.	Validate approver assignments.

8.	Validate document folders.

9.	Validate user access.

10.	Correct upload errors.
Deliverables
1.	Uploaded master data

2.	Data validation checklist

3.	Data correction log

4.	Approved data validation report
Output
Validated system data ready for UAT.
Acceptance Criteria
1.	Master data uploaded successfully.

2.	Critical master records are complete.

3.	Data owners approve uploaded records.

4.	Users can perform UAT using actual data.
________________________________________
Phase 8: User Acceptance Testing
Timeline
Week 9 to Week 10
Objective
To allow department users to test the configured system and confirm readiness for go-live.
UAT Workstreams
Workstream	Test Coverage
Leasing	Inquiry, ocular, quotation, reservation, BIS, lease, move-in, renewal/move-out
PMO	Move-in inspection, meter reading, tenant signing, turnover, move-out inspection, acceptance
Job Order	Helpdesk ticket, job order form, payment verification, MST scheduling, completion
Procurement	PR, approval, sourcing, comparison, PO, supplier email, delivery
Inventory	Receiving, goods receipt, stock monitoring, stock release, asset tagging
Office Supplies	OSR, approval, stock check, issuance, PR if no stock
Fleet	Internal vehicle request, special client trip, billing, collection, trip record
Accounting	Reservation verification, move-in billing, monthly billing, supplier payment, vehicle collection, deposit refund
Approvals	Request approval, return, rejection, exception approval
Documents	Upload, tag, link, review, archive
Website	Inquiry submission and CRM lead creation
Reports	Dashboards, pivot views, list reports, KPI summary
UAT Procedure
1.	Provide UAT test scripts.

2.	Assign users per department.

3.	Conduct guided testing session.

4.	Users perform actual process scenarios.

5.	Users record issues or comments.

6.	Implementation team reviews issue log.

7.	Issues are categorized as:
o	Critical
o	Major
o	Minor
o	Enhancement
o	Change Request
8.	Critical issues are resolved before go-live.
9.	Major issues are resolved or accepted with workaround.
10.	Minor issues may be scheduled for post-go-live.
11.	Enhancements are evaluated separately.
12.	UAT sign-off is secured.
Deliverables
1.	UAT test scripts

2.	UAT attendance record

3.	UAT issue log

4.	UAT resolution log

5.	UAT sign-off document
Output
User-approved system ready for final training and go-live preparation.
Acceptance Criteria
1.	Users complete assigned test scripts.

2.	Critical issues are resolved.

3.	Major issues have resolution or accepted workaround.

4.	Process owners sign off UAT.
________________________________________
Phase 9: User Training and Process Walkthrough
Timeline
Week 10 to Week 11
Objective
To train users according to their department roles and ensure proper adoption of the Odoo process.
Training Schedule
Training Session	Audience	Duration
Odoo Navigation and Basic Usage	All users	Half day
CRM and Leasing Process	Leasing / Sales	1 day
Lease Package and Tenant Management	Leasing, Billing, PMO, Accounting	1 day
PMO Move-In and Move-Out	PMO/Admin, Leasing, Security, Billing	1 day
Helpdesk and Job Order	PMO/Admin, Helpdesk, Maintenance, MST	1 day
Procurement Process	Procurement, Department Heads, GM Approvers	1 day
Inventory and Office Supplies	Warehouse, Admin, Procurement	1 day
Accounting and Invoicing	Accounting, Billing, Finance	1 to 2 days
Fleet and Vehicle Request	Admin, Fleet, GSD, Accounting	Half day to 1 day
Approvals	Department Heads, Managers, GM, Finance	Half day
Documents Management	All departments / Document Controller	Half day
Website Inquiry and CRM Routing	Marketing, Leasing	Half day
Reports and Dashboards	Management and Department Heads	Half day
System Administration	IT / System Administrator	1 day
Training Topics
1.	Login and dashboard navigation

2.	User roles and access

3.	Creating and updating records

4.	Searching and filtering records

5.	Uploading documents

6.	Submitting approvals

7.	Approving or rejecting requests

8.	Using CRM stages

9.	Processing lease records

10.	Processing PMO inspections

11.	Creating Helpdesk tickets

12.	Processing job orders

13.	Creating PRs and POs

14.	Receiving inventory

15.	Processing invoices and payments

16.	Monitoring vehicle requests

17.	Reviewing dashboards

18.	Common errors and corrections

19.	User responsibilities after go-live

20.	Escalation and support process
Deliverables
1.	Training plan

2.	Training attendance sheet

3.	User quick guide

4.	Department process guide

5.	Training completion report
Output
Users trained and ready for go-live.
Acceptance Criteria
1.	Users attended assigned training.

2.	Users understand assigned workflows.

3.	Process owners confirm training completion.

4.	Support escalation process is explained.
________________________________________
Phase 10: Go-Live Preparation and Cutover
Timeline
Week 11 to Week 12
Objective
To prepare the production environment, finalize data, confirm open issues, and prepare the organization for live system use.
Go-Live Readiness Activities
Activity	Description
Final Configuration Review	Confirm all required modules, fields, workflows, approvals, and reports
Final User Access Review	Confirm users, roles, permissions, and approver assignments
Final Master Data Review	Confirm tenant, unit, supplier, product, vehicle, and accounting data
Open Issue Review	Categorize and resolve critical issues
Cutover Plan	Define last manual transaction date and first Odoo transaction date
Document Template Review	Confirm availability of forms and document folders
Approval Route Review	Confirm all approvers and backup approvers
Accounting Readiness	Confirm journals, accounts, billing items, and payment process
Website Readiness	Confirm inquiry form and CRM lead routing
User Support Readiness	Confirm support team and escalation channels
Management Sign-Off	Secure approval to proceed to go-live
Cutover Checklist
Checklist Item	Status
Production database ready	Pending / Done
Modules configured	Pending / Done
Users created	Pending / Done
Access rights assigned	Pending / Done
Master data uploaded	Pending / Done
Approval workflows tested	Pending / Done
Documents folders ready	Pending / Done
CRM pipeline tested	Pending / Done
Lease records ready	Pending / Done
Accounting setup validated	Pending / Done
Purchase workflow tested	Pending / Done
Inventory receiving tested	Pending / Done
Helpdesk and job order tested	Pending / Done
Fleet workflow tested	Pending / Done
Website inquiry tested	Pending / Done
Reports and dashboards tested	Pending / Done
UAT signed off	Pending / Done
Training completed	Pending / Done
Go-live approval secured	Pending / Done
Data Cutover
1.	Freeze master data changes before final upload.

2.	Confirm last manual records.

3.	Upload final master data changes.

4.	Validate critical records.

5.	Set beginning transaction date in Odoo.

6.	Communicate cutover instructions to all users.
Deliverables
1.	Go-live readiness checklist

2.	Cutover plan

3.	Final user access list

4.	Open issue list

5.	Go-live sign-off
Output
System approved for live operation.
Acceptance Criteria
1.	Critical issues are resolved.

2.	Master data is validated.

3.	Users are trained.

4.	Management signs off go-live.
________________________________________
Phase 11: Go-Live
Timeline
Week 12
Objective
To officially start using Odoo as the live operational system for Phase 1 processes.
Go-Live Activities
Activity	Description
System Opening	Activate live operations in Odoo
User Access Confirmation	Confirm all users can log in
First Live Transactions	Support first CRM, lease, PR, inventory, accounting, helpdesk, fleet, and approval transactions
Issue Monitoring	Track issues in go-live support log
Department Support	Provide real-time assistance to key users
Daily Go-Live Review	Review issues, blockers, and urgent fixes
Management Update	Provide daily progress update during go-live week
First Live Transaction Checklist
1.	Create CRM Lead

2.	Create Reservation

3.	Verify Reservation Payment

4.	Create or update Lease Record

5.	Process Move-In Clearance

6.	Create Monthly Billing Reference

7.	Create Helpdesk Ticket

8.	Create Job Order

9.	Verify Job Order Payment

10.	Create Purchase Requisition

11.	Create Purchase Order

12.	Receive Goods

13.	Create Goods Receipt

14.	Create Payment Request

15.	Create Office Supplies Request

16.	Process Stock Release

17.	Create Vehicle Request

18.	Record Vehicle Trip

19.	Verify Collection

20.	Upload Documents

21.	Approve Requests

22.	Review Dashboard
Deliverables
1.	Live Odoo system

2.	Go-live issue log

3.	Daily go-live support update

4.	First transaction validation report
Output
Odoo Phase 1 is operational.
Acceptance Criteria
1.	Users can log in.

2.	Core processes can be performed live.

3.	Critical live blockers are resolved immediately.

4.	Management receives go-live status update.
________________________________________
Phase 12: Post-Go-Live Stabilization
Timeline
Week 13 to Week 14
Objective
To stabilize live operations, support users, correct minor issues, validate reports, and ensure adoption.
Stabilization Activities
Activity	Description
Daily Issue Monitoring	Review support tickets and user-reported issues
User Assistance	Guide users in live transactions
Minor Configuration Adjustment	Adjust fields, views, filters, and access as needed
Report Validation	Validate dashboard numbers with process owners
Approval Route Correction	Correct approver assignments if needed
Document Filing Review	Confirm users are uploading and linking files properly
Data Quality Review	Identify wrong entries, duplicates, or missing fields
Process Compliance Review	Check if users are following the agreed process
Management Review	Present stabilization status
Handover	Turn over system admin notes and support procedures
Post-Go-Live Support Coverage
1.	User guidance

2.	Minor configuration correction

3.	Access rights correction

4.	Field or view adjustment

5.	Workflow clarification

6.	Report validation

7.	Issue logging and tracking

8.	Process compliance monitoring

9.	Data correction assistance

10.	Stabilization review
Excluded from Stabilization Unless Covered by Change Request
1.	New modules

2.	Major workflow redesign

3.	Custom development

4.	Third-party integration

5.	Major data migration

6.	New complex reports

7.	New approval structure

8.	New department rollout

9.	New website pages outside approved scope

10.	Advanced accounting customization outside approved scope
Deliverables
1.	Post-go-live issue log

2.	Stabilization report

3.	Resolved issue summary

4.	Pending enhancement list

5.	System admin handover notes

6.	Final project closure recommendation
Output
Odoo system stabilized and ready for regular operation.
Acceptance Criteria
1.	No unresolved critical live issues.

2.	Users can complete daily transactions.

3.	Reports are reviewed and validated.

4.	Department heads confirm operational readiness.

5.	Pending items are categorized as support, enhancement, or change request.
________________________________________
5. Detailed Weekly Implementation Schedule
Week 1: Kickoff and Scope Confirmation
Day	Activity	Output
Day 1	Kickoff meeting	Kickoff completed
Day 2	Confirm modules and process owners	Confirmed team
Day 3	Confirm project governance	Governance matrix
Day 4	Issue data and document request list	Data request list
Day 5	Initial process review planning	Workshop schedule
Week 2: Process Validation
Day	Activity	Output
Day 1	Leasing and CRM workshop	Validated leasing flow
Day 2	PMO and Job Order workshop	Validated PMO flow
Day 3	Procurement and Inventory workshop	Validated procurement flow
Day 4	Accounting, Fleet, Office Supplies workshop	Validated admin/accounting flow
Day 5	Approval, Documents, Website, Reporting workshop	Validated support workflows
Week 3: Data Preparation and Core Setup
Day	Activity	Output
Day 1	Data template review	Approved templates
Day 2	Company, departments, users setup	Initial system structure
Day 3	Lease package and CRM setup	Initial leasing setup
Day 4	Sales, Subscriptions, Accounting setup	Initial billing setup
Day 5	Purchase and Inventory setup	Initial procurement setup
Week 4: Core Module Configuration
Day	Activity	Output
Day 1	Accounting and Invoicing configuration	Billing structure
Day 2	Purchase configuration	RFQ/PO workflow
Day 3	Inventory configuration	Receiving/stock setup
Day 4	Documents and Approvals configuration	Filing and approval setup
Day 5	Helpdesk, Maintenance, Fleet, Website configuration	Service and admin setup
Week 5: Configuration Review and Start Studio Setup
Day	Activity	Output
Day 1	Core module review	Configuration corrections
Day 2	Leasing Studio fields	Leasing custom fields
Day 3	PMO Studio fields	PMO custom fields
Day 4	Procurement and Inventory Studio fields	Procurement custom fields
Day 5	Accounting, Fleet, Website Studio fields	Admin/accounting fields
Week 6: Studio Workflow Configuration
Day	Activity	Output
Day 1	Leasing workflows and statuses	Leasing workflow ready
Day 2	PMO move-in/move-out workflow	PMO workflow ready
Day 3	Job order and maintenance workflow	Job order workflow ready
Day 4	Procurement and payment workflow	Procurement workflow ready
Day 5	Fleet, OSR, documents, approvals workflow	Admin workflow ready
Week 7: Dashboards and Internal Testing
Day	Activity	Output
Day 1	Dashboard configuration	Initial dashboards
Day 2	Report and saved filter setup	Initial reports
Day 3	Internal leasing test	Leasing issues logged
Day 4	Internal procurement/accounting test	Procurement issues logged
Day 5	Internal PMO/fleet/helpdesk test	Admin issues logged
Week 8: Issue Correction and Data Upload
Day	Activity	Output
Day 1	Resolve internal test issues	Corrected configuration
Day 2	Upload master data batch 1	Initial uploaded data
Day 3	Upload master data batch 2	Completed data upload
Day 4	Validate data	Data validation report
Day 5	Prepare UAT scripts	UAT pack ready
Week 9: User Acceptance Testing
Day	Activity	Output
Day 1	Leasing UAT	Leasing UAT results
Day 2	PMO, Helpdesk, Maintenance UAT	PMO UAT results
Day 3	Procurement, Inventory, Office Supplies UAT	Procurement UAT results
Day 4	Accounting, Fleet, Vehicle Collection UAT	Accounting/Fleet UAT results
Day 5	Approval, Documents, Website, Dashboards UAT	Support UAT results
Week 10: UAT Resolution and Training Start
Day	Activity	Output
Day 1	Resolve UAT critical issues	Corrected system
Day 2	Resolve remaining UAT issues	Updated issue log
Day 3	Conduct basic user training	Trained users
Day 4	Conduct leasing and PMO training	Trained process users
Day 5	Conduct procurement, inventory, accounting training	Trained process users
Week 11: Final Training and Go-Live Preparation
Day	Activity	Output
Day 1	Fleet, helpdesk, maintenance, documents training	Trained users
Day 2	Approver and management dashboard training	Trained approvers
Day 3	Final data review	Data validation
Day 4	Go-live checklist review	Readiness checklist
Day 5	Go-live approval meeting	Go-live sign-off
Week 12: Go-Live
Day	Activity	Output
Day 1	Start live system use	Odoo live
Day 2	Support first transactions	Live transaction support
Day 3	Monitor issues	Go-live issue log
Day 4	Resolve urgent issues	Stabilized transactions
Day 5	Management go-live review	Go-live status report
Week 13: Post-Go-Live Stabilization Week 1
Day	Activity	Output
Day 1	Review live issues	Support log
Day 2	Correct minor configuration issues	Adjusted system
Day 3	Validate reports and dashboards	Report validation
Day 4	Review process compliance	Compliance notes
Day 5	Management stabilization update	Week 1 stabilization report
Week 14: Post-Go-Live Stabilization Week 2
Day	Activity	Output
Day 1	Final issue review	Updated support log
Day 2	Final user guidance	User support
Day 3	Final dashboard review	Dashboard confirmation
Day 4	Handover to system administrator	Handover notes
Day 5	Project closure meeting	Stabilization closure report
________________________________________
6. Implementation Workstream Schedule
6.1 Leasing Workstream
Week	Activity
Week 1	Confirm leasing process owner and requirements
Week 2	Validate CRM to deposit refund process
Week 3	Configure CRM and Lease Package
Week 5	Configure Studio fields
Week 6	Configure statuses and checklists
Week 7	Internal test
Week 9	UAT
Week 10	Training
Week 12	Go-live
Week 13-14	Stabilization
6.2 PMO and Job Order Workstream
Week	Activity
Week 1	Confirm PMO/Admin process owner
Week 2	Validate move-in, move-out, job order process
Week 4	Configure Helpdesk and Maintenance
Week 5-6	Configure PMO and Job Order Studio forms
Week 7	Internal test
Week 9	UAT
Week 10	Training
Week 12	Go-live
Week 13-14	Stabilization
6.3 Procurement and Inventory Workstream
Week	Activity
Week 1	Confirm procurement and warehouse owners
Week 2	Validate PR, RFQ, PO, receiving, payment process
Week 3-4	Configure Purchase and Inventory
Week 5-6	Configure Studio fields and approval controls
Week 7	Internal test
Week 9	UAT
Week 10	Training
Week 12	Go-live
Week 13-14	Stabilization
6.4 Accounting and Billing Workstream
Week	Activity
Week 1	Confirm accounting owner
Week 2	Validate billing, collection, deposit, refund, supplier payment
Week 3-4	Configure Accounting and Invoicing
Week 5-6	Configure accounting verification fields
Week 7	Internal test
Week 9	UAT
Week 10	Training
Week 12	Go-live
Week 13-14	Stabilization
6.5 Fleet and Admin Workstream
Week	Activity
Week 1	Confirm fleet/admin owner
Week 2	Validate internal errand and special trip process
Week 4	Configure Fleet
Week 5-6	Configure vehicle request, billing, collection fields
Week 7	Internal test
Week 9	UAT
Week 10	Training
Week 12	Go-live
Week 13-14	Stabilization
6.6 Website and CRM Inquiry Workstream
Week	Activity
Week 1	Confirm website and inquiry requirements
Week 2	Validate inquiry form fields
Week 4	Configure website page and form
Week 5	Configure CRM routing
Week 7	Internal test
Week 9	UAT
Week 10	Training
Week 12	Go-live
Week 13-14	Stabilization
________________________________________
7. Key Milestones
Milestone	Target Week	Required Sign-Off
Project Kickoff Completed	Week 1	Project Sponsor
Process Validation Completed	Week 2	Process Owners
Master Data Templates Completed	Week 3	Data Owners
Core Module Configuration Completed	Week 5	Project Manager
Studio Configuration Completed	Week 7	Process Owners
Internal Testing Completed	Week 8	Implementation Team
Data Upload Completed	Week 9	Data Owners
UAT Completed	Week 10	Process Owners
User Training Completed	Week 11	Department Heads
Go-Live Readiness Approved	Week 11	Management
Go-Live Completed	Week 12	Project Sponsor
Stabilization Completed	Week 14	Management
________________________________________
8. Critical Dependencies
Dependency	Required By	Impact if Delayed
Approved scope	Week 1	Delays process validation
Assigned process owners	Week 1	Delays workshops
Approved process flows	Week 2	Delays configuration
Master data templates	Week 3	Delays data upload
Clean master data	Week 8	Delays UAT and go-live
Approval matrix	Week 4	Delays Approvals setup
Accounting setup decisions	Week 4	Delays billing and payment testing
Lease package readiness	Week 3	Delays leasing setup
Website content and inquiry fields	Week 4	Delays website form setup
User availability for UAT	Week 9	Delays UAT sign-off
User attendance in training	Week 10-11	Affects adoption
Management go-live approval	Week 11	Delays go-live
________________________________________
9. Risk Management Plan
Risk	Impact	Mitigation
Delayed master data submission	Delayed testing and go-live	Issue templates early and assign data owners
Unclear approval matrix	Incorrect approval routing	Confirm approvers during Week 2
Process owner unavailability	Delayed validation	Schedule workshops in advance
Scope expansion	Timeline extension	Use change request process
Users not attending UAT	Missed issues before go-live	Require department UAT participation
Users not attending training	Low adoption	Require training attendance sign-off
Accounting setup incomplete	Billing and payment issues	Prioritize accounting configuration early
Lease package gaps	Leasing process delay	Identify gaps during Week 2
Too many manual exceptions	Weak controls	Configure exception approval categories
Incomplete document filing	Weak audit trail	Require attachments in key workflows
Poor post-go-live adoption	Operational disruption	Provide stabilization and daily support
________________________________________
10. Go-Live Success Criteria
The project shall be considered ready for go-live when:
1.	Phase 1 modules are installed and configured.

2.	Users and access rights are completed.

3.	Master data is uploaded and validated.

4.	Approval workflows are configured and tested.

5.	Documents folders are ready.

6.	CRM inquiry process is tested.

7.	Leasing process is tested.

8.	PMO move-in and move-out process is tested.

9.	Job order process is tested.

10.	Procurement PR-to-PO process is tested.

11.	Inventory receiving process is tested.

12.	Office supplies request process is tested.

13.	Vehicle request and billing process is tested.

14.	Accounting verification process is tested.

15.	Website inquiry to CRM lead creation is tested.

16.	Reports and dashboards are available.

17.	UAT is signed off.

18.	Users are trained.

19.	Management approves go-live.
________________________________________
11. Post-Go-Live Success Criteria
Post-go-live stabilization shall be considered successful when:
1.	No unresolved critical issue remains.

2.	Users can complete their daily transactions.

3.	Department heads confirm operational readiness.

4.	Reports and dashboards are validated.

5.	Approval workflow issues are corrected.

6.	Access rights issues are corrected.

7.	Documents are properly uploaded and filed.

8.	Live transactions are being processed correctly.

9.	Pending items are classified as support, enhancement, or change request.

10.	System administrator receives handover notes.
________________________________________
12. Final Recommended Implementation Timeline Summary
Week	Phase	Main Output
Week 1	Kickoff and Mobilization	Project started, scope confirmed
Week 2	Process Validation	Approved process design
Week 3	Data Preparation / Initial Setup	Data templates and initial setup
Week 4	Core Configuration	Core modules configured
Week 5	Core Configuration / Studio Start	Main settings and initial Studio fields
Week 6	Studio Workflow Configuration	Custom workflows and fields completed
Week 7	Dashboards and Internal Testing	Reports and internal tests
Week 8	Issue Resolution and Data Upload	UAT-ready system
Week 9	UAT	User testing completed
Week 10	UAT Resolution and Training	Issues resolved and training started
Week 11	Final Training and Go-Live Preparation	Go-live checklist and sign-off
Week 12	Go-Live	Odoo live operation
Week 13	Stabilization Week 1	Live support and correction
Week 14	Stabilization Week 2	Handover and closure
________________________________________
13. Final Implementation Recommendation
The recommended approach is to implement Phase 1 in controlled stages, beginning with process confirmation and master data preparation, followed by module configuration, Studio workflow setup, internal testing, UAT, training, go-live, and post-go-live stabilization.
The most important priority is to ensure that all go-live critical processes are working before launch:
1.	CRM Inquiry

2.	Reservation

3.	Lease Contract

4.	Move-In

5.	Monthly Billing

6.	Move-Out

7.	PMO Inspection

8.	Job Order

9.	Purchase Requisition

10.	Purchase Order

11.	Inventory Receiving

12.	Payment Request

13.	Office Supplies Request

14.	Vehicle Request

15.	Accounting Verification

16.	Document Filing

17.	Approval Workflow

18.	Website Inquiry
Once these are stable, the implementation can proceed to deeper operational controls, dashboard refinement, and continuous process improvement after go-live.
