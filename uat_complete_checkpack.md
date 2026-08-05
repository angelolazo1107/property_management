ODOO PHASE 1 IMPLEMENTATION
Complete User Acceptance Testing (UAT) Document Pack
For All Identified Assessed Phase 1 Processes


Field	Details
Client / Organization	[Client Company Name]
Service Provider / Implementer	[Service Provider Name]
Project	Odoo Phase 1 Implementation
Document Type	UAT Plan, UAT Scripts, Issue Logs, Sign-Off Forms, UAT Summary, and Go/No-Go Templates
Version	v1.0
Prepared Date	August 4, 2026
Prepared By	[Name / Project Manager]
Status	Draft for Review / UAT Use

This document is intended as the master UAT pack for Phase 1 and may be edited during project execution.
 
1. Document Control
Version	Date	Author	Description	Approved By
v1.0	2026-08-04	[Project Manager]	Initial complete UAT document pack	[Project Sponsor]
				
				

Document	Purpose
UAT Plan	Defines UAT scope, objectives, responsibilities, entry/exit criteria, schedule, and acceptance rules.
UAT Scenario Matrix	Maps each identified business process to its test case, modules, owner, and expected evidence.
UAT Test Scripts	Detailed step-by-step scripts for users to execute during UAT.
UAT Issue Log Template	Tracks defects, questions, enhancements, owners, target dates, and status.
UAT Daily Status Report	Provides daily visibility on testing progress, pass/fail status, issues, and blockers.
Department Sign-Off Forms	Confirms formal acceptance by process owners and departments.
Final UAT Summary Report	Summarizes test coverage, results, unresolved issues, and readiness.
Go / No-Go Recommendation	Provides final UAT-based recommendation for go-live decision.

2. Static Table of Contents
Section	Title
1	Document Control
2	Static Table of Contents
3	UAT Plan
4	UAT Scope and Coverage
5	UAT Roles and Responsibilities
6	UAT Entry and Exit Criteria
7	UAT Schedule and Workstreams
8	UAT Data Requirements
9	Defect Management Procedure
10	UAT Scenario Coverage Matrix
11	Detailed UAT Test Scripts
12	UAT Issue Log Template
13	UAT Daily Status Report Template
14	Department UAT Sign-Off Forms
15	Final UAT Summary Report Template
16	Go / No-Go Recommendation Form

3. UAT Plan
The purpose of User Acceptance Testing is to allow the Client process owners, key users, and approvers to validate that the configured Odoo Phase 1 system supports the assessed procedures, required controls, and end-to-end workflows before production go-live.
3.1 UAT Objectives
•	Confirm that all identified Phase 1 processes can be executed in Odoo from start to finish.
•	Confirm that the Lease Module Package, CRM, Accounting, Sales, Subscriptions, Purchase, Inventory, Approvals, Documents, Studio, Maintenance, Helpdesk, Fleet, and Website modules are configured for the agreed scope.
•	Validate payment verification controls before reservation, move-in, chargeable job orders, supplier payment, deposit refund, and vehicle collection closure.
•	Validate approval routing, document filing, access rights, statuses, dashboards, and reports.
•	Identify defects, gaps, enhancements, and change requests before go-live.
•	Obtain formal sign-off from process owners and management.
3.2 UAT Approach
1.	Prepare UAT environment, users, master data, and test records.
2.	Execute test scripts by department and process area.
3.	Record actual results, evidence, pass/fail status, and remarks.
4.	Log issues using the UAT Issue Log.
5.	Classify issues as Critical, Major, Minor, Enhancement, or Change Request.
6.	Resolve, retest, or formally defer issues before sign-off.
7.	Secure process owner and management sign-off.
4. UAT Scope and Coverage
4.1 Modules Covered
No.	Odoo Module	UAT Coverage
1	Lease Module Package	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
2	CRM	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
3	Accounting	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
4	Sales	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
5	Subscriptions	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
6	Purchase	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
7	Inventory	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
8	Approvals	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
9	Documents	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
10	Studio	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
11	Maintenance	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
12	Helpdesk	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
13	Fleet	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.
14	Website	Configuration, process execution, access rights, records, documents, approvals, and reporting as applicable.

4.2 Business Process Areas Covered
No.	Process Area	Coverage
1	Sales / Leasing Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
2	Tenant Management Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
3	PMO Move-In Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
4	PMO Move-Out Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
5	PMO Job Order Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
6	Maintenance Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
7	Tenant Helpdesk / Support Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
8	Procurement Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
9	Warehouse / Inventory Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
10	Office Supplies Request Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
11	Vehicle Request Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
12	Vehicle Billing and Collection Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
13	Accounting and Billing Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
14	Approval Management Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
15	Document Management Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
16	Website Inquiry Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.
17	Reporting and Dashboard Process	End-to-end transaction flow, document requirements, approvals, controls, and reports.

5. UAT Roles and Responsibilities
Role / Department	UAT Responsibility
Project Sponsor / Management	Approve UAT scope, resolve escalations, approve go-live recommendation.
Project Manager	Coordinate UAT schedule, issue log, test status, and sign-off collection.
Leasing / Sales	Test CRM, reservation, BIS, lease contract, move-in, renewal, move-out, and tenant coordination workflows.
PMO / Admin	Test move-in/out inspection, utility readings, unit turnover, unit acceptance, and office supplies workflows.
Maintenance / MST	Test job order assignment, scheduling, work completion, and maintenance closure.
Procurement	Test PR, sourcing, canvass, RFQ, PO, supplier email, and payment request flow.
Warehouse / Inventory	Test receiving, goods receipt, stock release, asset tagging, and replenishment.
Accounting / Finance / Billing	Test reservation verification, invoicing, payment posting, 3-way match, collections, refunds, and settlement.
Fleet / GSD	Test internal errand, special client trip, billing assessment, collection, AR, trip record, and accounting endorsement.
Marketing / Website	Test website inquiry form and CRM lead routing.
System Administrator / IT	Validate access rights, security, documents, and configuration support.

6. UAT Entry and Exit Criteria
6.1 Entry Criteria
Entry Criteria	Required Status
Core modules installed and configured	Completed before UAT start
Studio fields, forms, views, statuses, and dashboards configured	Completed or ready for UAT validation
Users and access rights created	Completed and validated
Master data uploaded	Completed for UAT-relevant records
Approval workflows configured	Completed for all UAT categories
Document folders and tags configured	Completed
UAT scripts distributed	Completed
UAT participants identified and scheduled	Completed
Known configuration blockers resolved	Completed or formally accepted

6.2 Exit Criteria
Exit Criteria	Required Status
All critical Phase 1 process flows can be executed end-to-end in Odoo.	Required before go-live recommendation
All required approvals route to the correct approvers and generate an audit trail.	Required before go-live recommendation
All key transaction records can store required documents and attachments.	Required before go-live recommendation
Payment verification controls are working for reservation, move-in, job order, vehicle collection, supplier payment, and refund processes.	Required before go-live recommendation
UAT defects are logged, classified, assigned, resolved, retested, or formally accepted as post-go-live items.	Required before go-live recommendation
Process owners approve the UAT results for their department.	Required before go-live recommendation
Management signs the Go / No-Go recommendation after UAT completion.	Required before go-live recommendation

7. UAT Schedule and Workstreams
Day / Session	Workstream	Participants	Test Coverage
Day 1	Leasing and CRM	Leasing, Billing, Legal, Management	Website inquiry, CRM, ocular, quotation, reservation, BIS, contract, move-in, monthly billing, renewal/move-out, deposit refund
Day 2	PMO, Helpdesk, Maintenance	PMO/Admin, Maintenance/MST, Helpdesk, Leasing, Accounting	Move-in, inspections, utility readings, move-out, access return, job order, MST scheduling, work completion
Day 3	Procurement, Inventory, Office Supplies	Procurement, Warehouse, Admin, Accounting, Department Heads, GM Approver	PR, sourcing, canvass, PO, delivery, receiving, goods receipt, stock release, assets, OSR
Day 4	Accounting, Billing, Fleet, Vehicle Collection	Accounting, Finance, Billing, Admin, Fleet, GSD	Reservation, move-in clearance, monthly billing, supplier payment, move-out settlement, refunds, vehicle billing/collection
Day 5	Approvals, Documents, Website, Reports, Management Dashboards	All process owners, System Admin, Management	Approval routing, document filing, access rights, dashboards, KPI validation, UAT sign-off

8. UAT Data Requirements
Data Set	Required Sample Records
Users and Approvers	At least one user for each department role and approver level.
Tenants and Prospects	Sample prospects, reserved tenants, active tenants, expiring tenants, and move-out tenants.
Units	Available, reserved, occupied, for move-out, vacated, for repair, and available-again units.
Products / Services	Rental, deposit, parking, access card, Wi-Fi, pet fee, job order services, vehicle trip services, office supplies, assets, consumables.
Suppliers	At least three suppliers for canvassing and one repeat-order supplier.
Inventory	Stockable items, consumables, office supplies, assets, low stock samples.
Vehicles and Drivers	Available vehicle, unavailable vehicle, driver records, internal and chargeable trip sample.
Accounting	Journals, payment terms, COA accounts, AR/AP records, security deposit and refund samples.
Documents	Sample IDs, proof of payment, contracts, PR, quotation, PO, GR, job order, vehicle AR, trip record.

9. Defect Management Procedure
Severity	Definition	Target Handling
Critical	Blocks an end-to-end go-live critical process or causes incorrect financial, approval, or access control result.	Must be resolved before go-live or formally escalated for go/no-go decision.
Major	Process can continue only with workaround or has significant usability/control impact.	Resolve before go-live or obtain process owner acceptance with workaround.
Minor	Does not block process but requires correction, formatting, or minor configuration adjustment.	May be resolved before or after go-live during stabilization.
Enhancement	Nice-to-have improvement beyond agreed acceptance criteria.	Log separately for post-go-live enhancement review.
Change Request	Request outside approved scope, major redesign, new module, integration, or additional report.	Requires formal Change Request approval.

8.	Tester records actual result and evidence for each test step.
9.	Failed steps are logged in the UAT Issue Log with severity, owner, and target date.
10.	Implementation team resolves or explains the issue.
11.	Tester retests the corrected scenario.
12.	Process owner signs off after pass or accepted workaround.
10. UAT Scenario Coverage Matrix
Test Case ID	Group	Process	Modules	Primary Users	Status	Remarks
UAT-WEB-001	Website and CRM	Website Inquiry to CRM Lead	Website, CRM, Studio	Marketing, Leasing Agent, System Admin	Pending	
UAT-LS-001	Sales / Leasing	Client Acquisition and Inquiry Handling	CRM, Website, Lease Module Package, Studio	Leasing Agent	Pending	
UAT-LS-002	Sales / Leasing	Ocular Visit Coordination	CRM, Calendar, Documents, Studio	Leasing Agent, Security Coordinator	Pending	
UAT-LS-003	Sales / Leasing	Quotation Preparation and Follow-Up	CRM, Sales, Invoicing, Lease Module Package, Documents	Leasing Agent, Billing	Pending	
UAT-LS-004	Sales / Leasing	Reservation Fee Verification and Unit Blocking	Lease Module Package, Accounting, Invoicing, Documents, Approvals, Studio	Leasing, Accounting/Billing, Finance	Pending	
UAT-LS-005	Sales / Leasing	Tenant Application / BIS	Lease Module Package, Documents, Studio	Leasing, Billing, Legal	Pending	
UAT-LS-006	Sales / Leasing	Lease Package Contract and Legal Processing	Lease Module Package, Documents, Studio	Legal, Leasing, Billing	Pending	
UAT-LS-007	Sales / Leasing	Unit Assessment Request and Unit Readiness	Lease Module Package, Helpdesk, Maintenance, Documents, Studio	Leasing, PMO/Admin, Housekeeping, Maintenance	Pending	
UAT-LS-008	Sales / Leasing	Access Card / Biometrics Request	Lease Module Package, Invoicing, Accounting, Documents, Studio	Leasing, Admin, Security, Cashier/Billing	Pending	
UAT-LS-009	Sales / Leasing	Wi-Fi Application	Helpdesk, Maintenance, Accounting, Invoicing, Documents, Studio	Leasing, Billing, IT/Support	Pending	
UAT-LS-010	Sales / Leasing	Parking Application	Lease Module Package, Invoicing, Accounting, Documents, Studio	Leasing, Admin, Billing, Security	Pending	
UAT-LS-011	Sales / Leasing	Move-In Financial Clearance	Accounting, Invoicing, Lease Module Package, Sales, Subscriptions, Studio	Leasing, Billing, Accounting	Pending	
UAT-LS-012	Sales / Leasing	Contract Signing, Notarization, and Filing	Lease Module Package, Documents, Studio	Leasing, Legal, Billing	Pending	
UAT-LS-013	Sales / Leasing	Move-In Processing and Rental Registration	Lease Module Package, Documents, Studio	Leasing, PMO/Admin, Billing	Pending	
UAT-LS-014	Sales / Leasing	Pet Registration	Lease Module Package, Invoicing, Accounting, Documents, Studio	Leasing, Billing/Cashier	Pending	
UAT-LS-015	Sales / Leasing	Agent Commission Accounting	Lease Module Package, Accounting, Documents, Approvals, Studio	Leasing, Finance/Accounting	Pending	
UAT-LS-016	Sales / Leasing	Monthly Rental Billing	Subscriptions, Accounting, Invoicing, Lease Module Package, Studio	Billing, Accounting, Leasing	Pending	
UAT-LS-017	Sales / Leasing	Tenant Support from Active Lease	Helpdesk, Maintenance, Lease Module Package, Documents, Studio	Tenant Support, Leasing, PMO/Admin	Pending	
UAT-LS-018	Sales / Leasing	Lease Expiration, Renewal, or Move-Out Decision	Lease Module Package, CRM, Calendar, Studio	Leasing	Pending	
UAT-LS-019	Sales / Leasing	Security Deposit Refund	Accounting, Invoicing, Lease Module Package, Documents, Approvals, Studio	Accounting, Finance, Leasing, PMO/Admin	Pending	
UAT-PMO-001	PMO / Admin	PMO Move-In Flow	Lease Module Package, Maintenance, Helpdesk, Documents, Studio	Leasing, Information Desk, Security, PMO/Admin, MST	Pending	
UAT-PMO-002	PMO / Admin	Move-In Assessment	Maintenance, Documents, Studio	PMO/Admin, MST, Tenant	Pending	
UAT-PMO-003	PMO / Admin	Initial Utility Meter Reading	Lease Module Package, Documents, Accounting, Studio	PMO/Admin, MST, Tenant	Pending	
UAT-PMO-004	PMO / Admin	Unit Turnover and PMO Filing	Lease Module Package, Documents, Studio	Leasing, PMO/Admin, Security	Pending	
UAT-PMO-005	PMO / Admin	PMO Move-Out Flow	Lease Module Package, Maintenance, Accounting, Documents, Studio	Leasing, Information Desk, Security, PMO/Admin, Billing, Accounting	Pending	
UAT-PMO-006	PMO / Admin	Move-Out Assessment and Chargeable Findings	Maintenance, Accounting, Documents, Studio	PMO/Admin, Billing, Tenant	Pending	
UAT-PMO-007	PMO / Admin	Final Utility Meter Reading	Lease Module Package, Accounting, Documents, Studio	PMO/Admin, Tenant, Billing	Pending	
UAT-PMO-008	PMO / Admin	Billing Settlement and Unit Acceptance	Lease Module Package, Accounting, Documents, Studio	PMO/Admin, Billing, Accounting	Pending	
UAT-PMO-009	PMO / Admin	Access Item Return	Documents, Accounting, Lease Module Package, Studio	PMO/Admin, Security, Billing	Pending	
UAT-JO-001	Job Order and Maintenance	Tenant Request to Helpdesk Ticket	Helpdesk, Lease Module Package, Documents, Studio	Tenant Support, PMO/Admin	Pending	
UAT-JO-002	Job Order and Maintenance	Job Order Form, Tenant Approval, and Payment	Helpdesk, Maintenance, Accounting, Invoicing, Documents, Studio	PMO/Admin, Accounting, Tenant	Pending	
UAT-JO-003	Job Order and Maintenance	Payment Control Rule for Chargeable Job Order	Accounting, Helpdesk, Maintenance, Studio, Approvals	PMO/Admin, Accounting, Management	Pending	
UAT-JO-004	Job Order and Maintenance	MST Scheduling	Maintenance, Helpdesk, Calendar, Studio	PMO/Admin, MST	Pending	
UAT-JO-005	Job Order and Maintenance	Work Completion and Job Order Closure	Maintenance, Helpdesk, Documents, Studio	MST, PMO/Admin	Pending	
UAT-JO-006	Job Order and Maintenance	Job Order Rate Management	Maintenance, Helpdesk, Accounting, Studio	PMO/Admin, Accounting, Management	Pending	
UAT-PRC-001	Procurement	Purchase Requisition	Approvals, Purchase, Documents, Studio	Department Requestor, Department Head, GM, Procurement	Pending	
UAT-PRC-002	Procurement	Strategic Sourcing and Supplier Canvass	Purchase, Approvals, Documents, Studio	Procurement Assistant, Procurement Manager, GM	Pending	
UAT-PRC-003	Procurement	Repeat Order	Purchase, Documents, Studio	Procurement	Pending	
UAT-PRC-004	Procurement	RFQ / PO Creation and GM PO Approval	Purchase, Approvals, Documents, Accounting, Studio	Procurement Assistant, Procurement Manager, GM	Pending	
UAT-PRC-005	Procurement	PO Email to Supplier	Purchase, Documents, Studio	Procurement	Pending	
UAT-PRC-006	Procurement / Inventory	Delivery, Warehouse Receiving, and Goods Receipt	Inventory, Purchase, Documents, Accounting, Studio	Warehouse, Procurement, Accounting	Pending	
UAT-PRC-007	Procurement / Accounting	3-Way Match	Purchase, Inventory, Accounting, Documents, Studio	Accounting, Procurement, Warehouse	Pending	
UAT-PRC-008	Procurement / Accounting	Payment Request and Supplier Payment	Accounting, Purchase, Inventory, Documents, Approvals, Studio	Procurement, Accounting, Finance	Pending	
UAT-INV-001	Inventory / Warehouse	Product Master Setup	Inventory, Purchase, Studio	Warehouse, Procurement, Admin	Pending	
UAT-INV-002	Inventory / Warehouse	Stock Monitoring and Low Stock Review	Inventory, Purchase, Studio	Warehouse, Admin, Procurement	Pending	
UAT-INV-003	Inventory / Warehouse	Stock Release	Inventory, Approvals, Documents, Studio	Warehouse, Admin, Requestor	Pending	
UAT-INV-004	Inventory / Warehouse	Asset Tagging, Monitoring, Transfer, and Deployment	Inventory, Accounting, Documents, Studio	Warehouse, PMO/Admin, Accounting	Pending	
UAT-INV-005	Inventory / Warehouse	Consumable Flow	Inventory, Purchase, Approvals, Documents, Studio	Requestor, Warehouse, Procurement	Pending	
UAT-OSR-001	Office Supplies	Office Supplies Request and Approval	Approvals, Inventory, Purchase, Accounting, Documents, Studio	Requesting Department, Department Head, Admin	Pending	
UAT-OSR-002	Office Supplies	Stock Check and Issue Available Items	Approvals, Inventory, Documents, Studio	Admin, Warehouse, Requestor	Pending	
UAT-OSR-003	Office Supplies	No Stock to PR and Procurement	Approvals, Purchase, Inventory, Documents, Studio	Admin, Procurement, Accounting	Pending	
UAT-OSR-004	Office Supplies	Office Supplies Distribution and Acknowledgement	Inventory, Documents, Studio	Admin, Warehouse, Requesting Department	Pending	
UAT-FLT-001	Fleet / Vehicle	Internal Vehicle Errand	Fleet, Approvals, Documents, Studio	Employee, Admin, Driver	Pending	
UAT-FLT-002	Fleet / Vehicle	Special Client Trip Request	Fleet, Invoicing, Accounting, Documents, Approvals, Studio	Client/GSD, Admin, Driver, Accounting	Pending	
UAT-FLT-003	Fleet / Vehicle	Vehicle Billing Assessment and Client Approval	Fleet, Invoicing, Accounting, Studio	Admin, GSD, Client	Pending	
UAT-FLT-004	Fleet / Vehicle	GSD Collection and AR Issuance	Accounting, Invoicing, Fleet, Documents, Studio	GSD, Accounting, Admin	Pending	
UAT-FLT-005	Fleet / Vehicle	Driver Trip Record	Fleet, Documents, Studio	Driver, Admin	Pending	
UAT-FLT-006	Fleet / Vehicle	Accounting Collection Verification	Accounting, Invoicing, Fleet, Documents, Studio	Accounting, GSD, Admin	Pending	
UAT-ACC-001	Accounting and Billing	Move-In Billing and Payment Clearance	Accounting, Invoicing, Lease Module Package, Sales, Subscriptions, Studio	Billing, Accounting, Leasing	Pending	
UAT-ACC-002	Accounting and Billing	Monthly Rental Billing and Outstanding Balance Monitoring	Subscriptions, Accounting, Invoicing, Lease Module Package	Billing, Accounting	Pending	
UAT-ACC-003	Accounting and Billing	PMO Job Order Payment Verification	Accounting, Invoicing, Helpdesk, Maintenance, Studio	Accounting, Admin, PMO	Pending	
UAT-ACC-004	Accounting and Billing	Move-Out Billing and Settlement	Accounting, Invoicing, Lease Module Package, Documents, Studio	Billing, Accounting, PMO	Pending	
UAT-ACC-005	Accounting and Billing	Damage and Missing Item Charges	Accounting, Invoicing, Lease Module Package, Documents, Studio	PMO, Billing, Accounting	Pending	
UAT-ACC-006	Accounting and Billing	Security Deposit Deduction and Refund	Accounting, Approvals, Documents, Lease Module Package, Studio	Accounting, Finance, Management	Pending	
UAT-ACC-007	Accounting and Billing	Vendor Bill and Supplier Payment	Accounting, Purchase, Inventory, Documents, Approvals, Studio	Accounting, Procurement	Pending	
UAT-ACC-008	Accounting and Billing	Vehicle Collection Verification	Accounting, Invoicing, Fleet, Documents, Studio	Accounting, GSD	Pending	
UAT-CTRL-001	Approval Management	General Approval Process	Approvals, Studio	Requestor, Reviewer, Approver	Pending	
UAT-CTRL-002	Approval Management	Return and Rejection Handling	Approvals, Studio	Requestor, Approver	Pending	
UAT-DOC-001	Document Management	Document Filing	Documents, Studio	All Departments, Document Controller	Pending	
UAT-DOC-002	Document Management	Document Access, Folder, and Sensitive Record Control	Documents, Studio	Document Controller, System Admin, Department Users	Pending	
UAT-RPT-001	Reporting and Dashboard	Leasing Dashboard	CRM, Lease Module Package, Accounting, Studio	Leasing Manager, Management	Pending	
UAT-RPT-002	Reporting and Dashboard	PMO Dashboard	Maintenance, Helpdesk, Lease Module Package, Studio	PMO/Admin Manager, Management	Pending	
UAT-RPT-003	Reporting and Dashboard	Procurement Dashboard	Purchase, Approvals, Inventory, Studio	Procurement Manager, Management	Pending	
UAT-RPT-004	Reporting and Dashboard	Inventory Dashboard	Inventory, Purchase, Studio	Warehouse, Admin, Management	Pending	
UAT-RPT-005	Reporting and Dashboard	Accounting Dashboard	Accounting, Invoicing, Purchase, Inventory, Fleet, Studio	Accounting Manager, Finance, Management	Pending	
UAT-RPT-006	Reporting and Dashboard	Fleet Dashboard	Fleet, Accounting, Studio	Fleet/Admin, GSD, Management	Pending	
UAT-RPT-007	Reporting and Dashboard	Management KPI Dashboard	All Phase 1 Modules, Studio	Management, Department Heads	Pending	

 
11. Detailed UAT Test Scripts
Instructions: Each tester should execute the script using actual or approved UAT data. Record Actual Result, Status, Remarks, and attach evidence such as screenshots, documents, logs, or exported records.
Website and CRM
UAT-WEB-001 - Website Inquiry to CRM Lead
Field	Details
Objective	Confirm website inquiry creates a CRM lead and routes to Leasing.
Odoo Modules	Website, CRM, Studio
Primary Roles / Testers	Marketing, Leasing Agent, System Admin
Preconditions	Website form and CRM pipeline configured.
Required Test Data	Sample client inquiry with name, phone, email, preferred unit, budget, move-in date, parking requirement.
Required Evidence	Screenshot of website submission, CRM lead, and activity log.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open the website inquiry form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Submit a complete leasing inquiry.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify the created CRM lead.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Check assigned Leasing Agent and lead source.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Create follow-up activity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	CRM lead is created, assigned, tagged with source, and follow-up is scheduled.		Pass / Fail	

Sales / Leasing
UAT-LS-001 - Client Acquisition and Inquiry Handling
Field	Details
Objective	Validate inquiry capture, qualification, unit availability check, and lead status update.
Odoo Modules	CRM, Website, Lease Module Package, Studio
Primary Roles / Testers	Leasing Agent
Preconditions	CRM pipeline and unit records configured.
Required Test Data	Prospect inquiry and available unit. 
Required Evidence	CRM lead record with notes, source, next activity, and status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create CRM lead from walk-in/Facebook/referral source.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Enter client requirements and unit preferences.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Check unit availability in Lease Module.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record discussion notes and next activity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Move lead to Ocular Visit Scheduled or mark lost with reason.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Lead contains complete qualification details and correct status. Lost leads require lost reason.		Pass / Fail	

UAT-LS-002 - Ocular Visit Coordination
Field	Details
Objective	Validate scheduling of ocular visit and Security coordination details.
Odoo Modules	CRM, Calendar, Documents, Studio
Primary Roles / Testers	Leasing Agent, Security Coordinator
Preconditions	Lead exists and unit is available for viewing.
Required Test Data	Visitor name, entry time, contact person, floor/unit, purpose, vehicle information.
Required Evidence	Ocular visit record, security details, feedback, CRM stage history.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open interested CRM lead.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Create ocular visit schedule.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Encode visitor/security details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach or record unit list for viewing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Complete visit and record client feedback.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	If no-show, tag No Show and create reschedule activity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Ocular visit details are recorded, Security information is complete, and CRM stage is updated.		Pass / Fail	

UAT-LS-003 - Quotation Preparation and Follow-Up
Field	Details
Objective	Validate preparation and recording of rental quotation after ocular visit.
Odoo Modules	CRM, Sales, Invoicing, Lease Module Package, Documents
Primary Roles / Testers	Leasing Agent, Billing
Preconditions	Ocular visit completed. Products/services and unit rates configured.
Required Test Data	Unit rate, furniture rate if applicable, deposit, parking, Wi-Fi, access, lease term.
Required Evidence	Quotation copy/record, lead stage, follow-up activity.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open lead after ocular visit.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Prepare quotation or quotation record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Include rental amount, deposit, furniture, parking, Wi-Fi, access fees, and lease term.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Send or record quotation sent date.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Create follow-up activity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Move to Reservation or Lost based on client decision.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Quotation is recorded with correct pricing details, sent date, and follow-up status.		Pass / Fail	

UAT-LS-004 - Reservation Fee Verification and Unit Blocking
Field	Details
Objective	Validate reservation fee payment verification, receipt issuance, and unit blocking.
Odoo Modules	Lease Module Package, Accounting, Invoicing, Documents, Approvals, Studio
Primary Roles / Testers	Leasing, Accounting/Billing, Finance
Preconditions	Client accepted quotation and unit is available. Accounting journals configured.
Required Test Data	Reservation fee proof, tenant name, unit number, fee amount.
Required Evidence	Proof of payment, receipt number, reserved unit status, chatter/audit log.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create reservation record from qualified lead.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Upload proof of reservation payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Accounting verifies payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record official receipt/acknowledgement receipt number.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Update unit status to Reserved / Hold.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Notify Leasing and endorse to lease processing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Unit is not blocked until payment is verified. Reservation is confirmed after receipt issuance.		Pass / Fail	

UAT-LS-005 - Tenant Application / BIS
Field	Details
Objective	Validate BIS creation, required tenant details, and document submission to Billing/Legal.
Odoo Modules	Lease Module Package, Documents, Studio
Primary Roles / Testers	Leasing, Billing, Legal
Preconditions	Reservation verified and unit reserved.
Required Test Data	Tenant information, valid ID, proof of income, rental price, deposit, move-in date, lease terms, agent/discount tags.
Required Evidence	BIS record, attached ID/proof, submission status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create Tenant Application / BIS record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Encode tenant, unit, rental, deposit, move-in date, and lease term.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Tag agent involvement and discount if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach valid ID and proof of income.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit to Billing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Submit to Legal for contract preparation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	BIS is complete, required documents attached, and status shows submitted to Billing/Legal.		Pass / Fail	

 
UAT-LS-006 - Lease Package Contract and Legal Processing
Field	Details
Objective	Validate lease contract creation from BIS and legal review workflow.
Odoo Modules	Lease Module Package, Documents, Studio
Primary Roles / Testers	Legal, Leasing, Billing
Preconditions	BIS and tenant documents are complete.
Required Test Data	Lease terms, rental amount, deposit, tenant/unit details.
Required Evidence	Lease record, legal status, draft contract attachment.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create Lease Contract record from BIS.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify tenant, unit, lease term, rental, deposit, and move-in date.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Set legal processing status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record corrections if any.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Mark contract ready for signing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Attach draft contract.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Lease contract details match BIS. Contract status and attachment are properly recorded.		Pass / Fail	

UAT-LS-007 - Unit Assessment Request and Unit Readiness
Field	Details
Objective	Validate request for unit assessment and readiness confirmation before move-in.
Odoo Modules	Lease Module Package, Helpdesk, Maintenance, Documents, Studio
Primary Roles / Testers	Leasing, PMO/Admin, Housekeeping, Maintenance
Preconditions	Lease processing in progress and unit reserved.
Required Test Data	Unit number, move-in date, assessment request, findings.
Required Evidence	Assessment record, findings, maintenance task, ready status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create room/unit assessment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Assign PMO/Admin and Housekeeping/Maintenance if needed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Record inspection findings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Create cleaning or repair task if issue found.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Mark unit ready after pass/completion.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Link readiness status to lease/move-in record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Unit readiness cannot be marked complete without inspection result. Issues create action records.		Pass / Fail	

UAT-LS-008 - Access Card / Biometrics Request
Field	Details
Objective	Validate access request, fee processing, and release recording.
Odoo Modules	Lease Module Package, Invoicing, Accounting, Documents, Studio
Primary Roles / Testers	Leasing, Admin, Security, Cashier/Billing
Preconditions	Tenant has active/for move-in lease record.
Required Test Data	Access type, valid ID, access card fee, card number.
Required Evidence	Access request, proof of payment, card/biometrics details.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create access request linked to tenant/lease.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Select biometrics or access card.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Attach valid ID.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	For access card, create fee invoice/payment verification.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Record card number or biometric status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Mark access item released.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Biometrics can be marked free; access card requires payment verification before release.		Pass / Fail	

UAT-LS-009 - Wi-Fi Application
Field	Details
Objective	Validate Wi-Fi request, payment, installation scheduling, and completion.
Odoo Modules	Helpdesk, Maintenance, Accounting, Invoicing, Documents, Studio
Primary Roles / Testers	Leasing, Billing, IT/Support
Preconditions	Tenant has lease record and requests Wi-Fi.
Required Test Data	Internet subscription form, payment proof, installation details.
Required Evidence	Wi-Fi request, payment verification, installation completion evidence.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create Wi-Fi request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Attach subscription form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Record or create billing/payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Accounting verifies payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Assign IT/support installer.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Record installation schedule and completion details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Link Wi-Fi status to lease record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Wi-Fi installation request proceeds only after payment verification unless approved.		Pass / Fail	

UAT-LS-010 - Parking Application
Field	Details
Objective	Validate parking document submission, payment, and assignment.
Odoo Modules	Lease Module Package, Invoicing, Accounting, Documents, Studio
Primary Roles / Testers	Leasing, Admin, Billing, Security
Preconditions	Tenant has lease record and requests parking.
Required Test Data	Parking type, OR/CR, driver license, fee, slot/sticker.
Required Evidence	Parking record, attachments, payment, slot/sticker details.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create parking application.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Select parking type: Sapphire Parking, Sapphire Sticker, or Marina Sticker.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Attach OR/CR and driver license.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Create/verify parking fee payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Assign parking location/sticker number.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Notify tenant and link to lease.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Parking cannot be approved without required documents and payment.		Pass / Fail	

UAT-LS-011 - Move-In Financial Clearance
Field	Details
Objective	Validate complete move-in invoice, payment posting, and clearance.
Odoo Modules	Accounting, Invoicing, Lease Module Package, Sales, Subscriptions, Studio
Primary Roles / Testers	Leasing, Billing, Accounting
Preconditions	Contract ready, unit ready, billing products configured.
Required Test Data	Rental balance, security deposit, parking, access, Wi-Fi, pet/other fees, reservation payment.
Required Evidence	Move-in invoice, payment record, financial clearance status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Prepare move-in clearance from lease record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Create billing invoice with applicable charges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Apply reservation fee if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Accounting verifies charges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Record tenant payment and post payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Set Move-In Financially Cleared status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Move-in clearance is achieved only after payment is posted and verified.		Pass / Fail	

 
UAT-LS-012 - Contract Signing, Notarization, and Filing
Field	Details
Objective	Validate signed contract routing, notarization status, tenant copy release, and filing.
Odoo Modules	Lease Module Package, Documents, Studio
Primary Roles / Testers	Leasing, Legal, Billing
Preconditions	Contract ready for signing and tenant financially cleared.
Required Test Data	Signed lease contract, house rules, violation forms.
Required Evidence	Signed/notarized contract, tenant copy release record, filing status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Mark contract reviewed/explained to tenant.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Record tenant signature status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Submit signed contract to Billing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Forward to Legal for notarization.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Attach notarized contract.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Record tenant copy release.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	File in Documents folder.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Signed and notarized contract is attached, filed, and linked to lease.		Pass / Fail	

UAT-LS-013 - Move-In Processing and Rental Registration
Field	Details
Objective	Validate move-in form, final validation, rental registration, and activation.
Odoo Modules	Lease Module Package, Documents, Studio
Primary Roles / Testers	Leasing, PMO/Admin, Billing
Preconditions	Payment cleared, contract signed, unit ready, PMO inspection complete.
Required Test Data	Move-in form, tenant signature, agent signature if applicable, rental registration details.
Required Evidence	Move-in form, lease active status, unit occupied status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Prepare Move-In Form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Validate payment clearance, contract signing, and unit readiness.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Validate PMO inspection/turnover.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record tenant and agent signatures where applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Prepare rental registration details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Activate lease and mark unit Occupied.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Move-in cannot complete unless clearance, contract, readiness, and PMO turnover are complete.		Pass / Fail	

UAT-LS-014 - Pet Registration
Field	Details
Objective	Validate pet registration and fee collection.
Odoo Modules	Lease Module Package, Invoicing, Accounting, Documents, Studio
Primary Roles / Testers	Leasing, Billing/Cashier
Preconditions	Tenant has lease record and declares pet.
Required Test Data	Pet details, pet registration fee, proof of payment.
Required Evidence	Pet registration record and payment evidence.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create pet registration linked to tenant/lease.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Enter pet details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Generate or record pet registration fee.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Activate pet registration.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	File pet registration document.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Pet registration is active only after fee verification.		Pass / Fail	

UAT-LS-015 - Agent Commission Accounting
Field	Details
Objective	Validate agent commission after signed contract and completed requirements.
Odoo Modules	Lease Module Package, Accounting, Documents, Approvals, Studio
Primary Roles / Testers	Leasing, Finance/Accounting
Preconditions	Lease contract signed and agent tagged.
Required Test Data	Agent details, bank details, valid ID, commission amount.
Required Evidence	Commission request, vendor bill/payment, approval, proof of release.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open signed lease with agent.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Create agent commission request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Attach agent requirements and valid ID.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Validate commission amount.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Create vendor bill or payment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Finance approves and releases payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Record payment status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Commission is processed only after signed contract and complete agent requirements.		Pass / Fail	

UAT-LS-016 - Monthly Rental Billing
Field	Details
Objective	Validate recurring monthly billing for active leases and outstanding balance monitoring.
Odoo Modules	Subscriptions, Accounting, Invoicing, Lease Module Package, Studio
Primary Roles / Testers	Billing, Accounting, Leasing
Preconditions	Lease is active and monthly billing/subscription configured.
Required Test Data	Active lease contract with billing amount and cycle.
Required Evidence	Monthly invoice, payment record, outstanding balance report.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Confirm lease contract is Active.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Generate recurring monthly invoice.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify invoice amount and billing period.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Send billing to tenant.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Record tenant payment and post payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Review outstanding balance report.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Monthly invoice generated for active lease, sent to tenant, and payment/outstanding status tracked.		Pass / Fail	

UAT-LS-017 - Tenant Support from Active Lease
Field	Details
Objective	Validate tenant concern intake and link to tenant/lease/unit.
Odoo Modules	Helpdesk, Maintenance, Lease Module Package, Documents, Studio
Primary Roles / Testers	Tenant Support, Leasing, PMO/Admin
Preconditions	Active tenant/lease exists. Helpdesk team configured.
Required Test Data	Tenant concern details, category, unit, attachments.
Required Evidence	Helpdesk ticket, linked lease, resolution notes.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create support ticket for active tenant.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Link ticket to tenant, lease, and unit.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Assign concern category and responsible team.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach photo/document if needed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Update ticket stage until resolved.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Close ticket with resolution notes.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Tenant concern is traceable to tenant/unit and can be monitored until closure.		Pass / Fail	

 
UAT-LS-018 - Lease Expiration, Renewal, or Move-Out Decision
Field	Details
Objective	Validate lease expiry monitoring and renewal/move-out decision.
Odoo Modules	Lease Module Package, CRM, Calendar, Studio
Primary Roles / Testers	Leasing
Preconditions	Active lease with expiry date.
Required Test Data	Lease expiry date, tenant decision, renewal/move-out details.
Required Evidence	Expiring lease report, activity logs, renewal/move-out status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Run or view expiring lease list.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Confirm tenant notification at least 7 days before expiry.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Record tenant decision to renew or move out.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	If renew, create renewal activity/record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	If move out, initiate move-out process.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Update lease decision status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Lease nearing expiry appears in monitoring; renewal or move-out decision is recorded.		Pass / Fail	

UAT-LS-019 - Security Deposit Refund
Field	Details
Objective	Validate security deposit refund after move-out clearance and deduction computation.
Odoo Modules	Accounting, Invoicing, Lease Module Package, Documents, Approvals, Studio
Primary Roles / Testers	Accounting, Finance, Leasing, PMO/Admin
Preconditions	Move-out completed and final settlement cleared.
Required Test Data	Tenant bank details, deposit amount, deductions, approval.
Required Evidence	Refund computation, approval, proof of release, tenant closure status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open moved-out tenant account.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Confirm move-out clearance and PMO acceptance.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Enter tenant bank details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Compute refund and deductions.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit refund approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Finance approves refund.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Record refund release and proof.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
8	Close tenant account.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Refund cannot proceed without move-out clearance. Deductions and proof of refund are filed.		Pass / Fail	

PMO / Admin
UAT-PMO-001 - PMO Move-In Flow
Field	Details
Objective	Validate move-in form to PMO filing and unit occupied status.
Odoo Modules	Lease Module Package, Maintenance, Helpdesk, Documents, Studio
Primary Roles / Testers	Leasing, Information Desk, Security, PMO/Admin, MST
Preconditions	Move-in financially cleared and scheduled.
Required Test Data	Move-In Form, unit, tenant, schedule.
Required Evidence	Move-in assessment, utility readings, turnover and filing status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Leasing submits Move-In Form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Information Desk records the form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Security coordinates with PMO/Admin.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	PMO/Admin and MST inspect unit.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Initial utility readings are recorded.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Tenant signs assessment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Unit is turned over and PMO files records.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
8	Unit status becomes Occupied.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Move-in workflow completes with inspection, readings, tenant signing, filing, and occupied status.		Pass / Fail	

UAT-PMO-002 - Move-In Assessment
Field	Details
Objective	Validate unit condition documentation before occupancy.
Odoo Modules	Maintenance, Documents, Studio
Primary Roles / Testers	PMO/Admin, MST, Tenant
Preconditions	Move-in inspection scheduled.
Required Test Data	Fixture/equipment checklist, photos, observations.
Required Evidence	Signed move-in assessment and photos.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open PMO move-in assessment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Inspect unit condition with tenant.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Check fixtures and installed equipment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record damages, defects, or no findings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Attach photos if needed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Tenant reviews and signs/acknowledges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Move-in assessment captures unit condition and tenant acknowledgement.		Pass / Fail	

UAT-PMO-003 - Initial Utility Meter Reading
Field	Details
Objective	Validate baseline electric and water readings for billing reference.
Odoo Modules	Lease Module Package, Documents, Accounting, Studio
Primary Roles / Testers	PMO/Admin, MST, Tenant
Preconditions	Move-in inspection in progress.
Required Test Data	Electric reading, water reading, meter photos.
Required Evidence	Initial utility reading record and photos.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open initial utility reading form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Enter electric submeter reading.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Enter water submeter reading.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach meter photos.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Tenant verifies readings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Save as billing baseline.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Initial readings are recorded, acknowledged, and available for future billing.		Pass / Fail	

UAT-PMO-004 - Unit Turnover and PMO Filing
Field	Details
Objective	Validate release of keys, remote, access items, and completed filing.
Odoo Modules	Lease Module Package, Documents, Studio
Primary Roles / Testers	Leasing, PMO/Admin, Security
Preconditions	Inspection, initial reading, and payment clearance completed.
Required Test Data	Keys, AC remote, access card if applicable, turnover acknowledgement.
Required Evidence	Turnover record, issued item checklist, filing status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Confirm inspection passed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Confirm financial clearance and contract signed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Prepare keys, remote, and applicable access card.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Release items to tenant.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Record tenant acknowledgement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Mark PMO filing complete.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Unit turnover is recorded with issued items and documents filed.		Pass / Fail	

 
UAT-PMO-005 - PMO Move-Out Flow
Field	Details
Objective	Validate move-out request to unit status update.
Odoo Modules	Lease Module Package, Maintenance, Accounting, Documents, Studio
Primary Roles / Testers	Leasing, Information Desk, Security, PMO/Admin, Billing, Accounting
Preconditions	Tenant move-out notice/request exists.
Required Test Data	Move-Out Form, unit, tenant, schedule.
Required Evidence	Move-out assessment, settlement, access return, status update.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Leasing submits Move-Out Form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Information Desk records request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Security coordinates with PMO/Admin.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	PMO/Admin conducts final inspection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Final utility readings are recorded.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Billing settlement is completed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Tenant signs assessment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
8	Access items returned.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
9	PMO accepts unit and files records.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
10	Unit status becomes Vacated / Under Repair / Available.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Move-out process completes only after inspection, readings, settlement, signing, access return, and PMO acceptance.		Pass / Fail	

UAT-PMO-006 - Move-Out Assessment and Chargeable Findings
Field	Details
Objective	Validate final inspection findings and chargeable item identification.
Odoo Modules	Maintenance, Accounting, Documents, Studio
Primary Roles / Testers	PMO/Admin, Billing, Tenant
Preconditions	Move-out inspection scheduled.
Required Test Data	Damage findings, missing fixtures/equipment, photos.
Required Evidence	Move-out assessment, photos, chargeable item list.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open move-out assessment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Inspect unit condition, damages, alterations, and deficiencies.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Check completeness of fixtures/equipment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record findings and attach photos.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Flag chargeable findings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Submit chargeable items to Billing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Tenant reviews and signs.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Chargeable findings are documented, manager-confirmed, and endorsed to Billing.		Pass / Fail	

UAT-PMO-007 - Final Utility Meter Reading
Field	Details
Objective	Validate final electric/water readings for settlement.
Odoo Modules	Lease Module Package, Accounting, Documents, Studio
Primary Roles / Testers	PMO/Admin, Tenant, Billing
Preconditions	Move-out final inspection in progress.
Required Test Data	Final electric reading, final water reading, meter photos.
Required Evidence	Final utility reading record and billing handoff.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open final utility reading form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Enter final electric reading.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Enter final water reading.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach meter photos.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Tenant verifies readings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Submit readings to Billing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Final readings are recorded and available for final billing computation.		Pass / Fail	

UAT-PMO-008 - Billing Settlement and Unit Acceptance
Field	Details
Objective	Validate unit acceptance after settlement and access return.
Odoo Modules	Lease Module Package, Accounting, Documents, Studio
Primary Roles / Testers	PMO/Admin, Billing, Accounting
Preconditions	Final inspection, readings, and billing settlement completed.
Required Test Data	Settlement status, access item return, unit status.
Required Evidence	Unit acceptance record and final unit status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Confirm final inspection completed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Confirm final utility readings completed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Confirm tenant settlement or approved deposit deduction.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Confirm access items returned or charged.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	PMO/Admin accepts unit.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Update unit status to Vacated, For Cleaning, For Repair, or Available.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	File unit acceptance record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Unit acceptance cannot complete without inspection, readings, settlement, and access return/charge.		Pass / Fail	

UAT-PMO-009 - Access Item Return
Field	Details
Objective	Validate return of keys, access cards, remote, gate pass, sticker, and missing item charges.
Odoo Modules	Documents, Accounting, Lease Module Package, Studio
Primary Roles / Testers	PMO/Admin, Security, Billing
Preconditions	Move-out inspection completed.
Required Test Data	Access item checklist.
Required Evidence	Access item checklist, billing/deduction record if missing.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open access item return checklist.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Record returned keys, cards, remote, gate pass, sticker, and other items.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Identify missing items.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Endorse missing item charges to Billing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Mark access return cleared after return/payment/deduction.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	All access items are returned or charged before final clearance.		Pass / Fail	

Job Order and Maintenance
UAT-JO-001 - Tenant Request to Helpdesk Ticket
Field	Details
Objective	Validate request intake and Helpdesk ticket creation.
Odoo Modules	Helpdesk, Lease Module Package, Documents, Studio
Primary Roles / Testers	Tenant Support, PMO/Admin
Preconditions	Tenant or requestor exists. Helpdesk configured.
Required Test Data	Request description, category, unit, photos.
Required Evidence	Helpdesk ticket with attachments and assignment.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create tenant/requestor ticket.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Link ticket to tenant/unit if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Assign ticket category and team.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record request details and attachments.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Move ticket to Admin Review.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Request is logged as Helpdesk ticket with correct category and assignment.		Pass / Fail	

 
UAT-JO-002 - Job Order Form, Tenant Approval, and Payment
Field	Details
Objective	Validate formal job order creation, tenant sign-off, and payment verification.
Odoo Modules	Helpdesk, Maintenance, Accounting, Invoicing, Documents, Studio
Primary Roles / Testers	PMO/Admin, Accounting, Tenant
Preconditions	Helpdesk ticket reviewed by Admin.
Required Test Data	Job order scope, charges, tenant approval, payment proof.
Required Evidence	Signed job order and payment verification record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Admin reviews ticket and prepares Job Order Form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Define scope of work and corresponding charge.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Tenant reviews and signs job order.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Create invoice or payment record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Accounting verifies payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Update payment verified field.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Job order cannot proceed to scheduling until tenant approval and payment verification.		Pass / Fail	

UAT-JO-003 - Payment Control Rule for Chargeable Job Order
Field	Details
Objective	Validate system control that no chargeable job order starts without full payment except approved exception.
Odoo Modules	Accounting, Helpdesk, Maintenance, Studio, Approvals
Primary Roles / Testers	PMO/Admin, Accounting, Management
Preconditions	Chargeable job order exists but payment not verified.
Required Test Data	Job order amount and unpaid status.
Required Evidence	Blocked status or exception approval evidence.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create chargeable job order.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Leave payment status unverified.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Attempt to schedule MST work.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify scheduling is blocked or flagged.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit management exception approval if work must proceed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Approve exception and schedule work.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Chargeable job cannot be scheduled/started without payment unless approved by Management.		Pass / Fail	

UAT-JO-004 - MST Scheduling
Field	Details
Objective	Validate technician assignment based on availability and urgency.
Odoo Modules	Maintenance, Helpdesk, Calendar, Studio
Primary Roles / Testers	PMO/Admin, MST
Preconditions	Job order payment verified or approved exception exists.
Required Test Data	Technician list, tenant availability, work urgency.
Required Evidence	Scheduled work order and assignment notification.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open verified job order.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Check tenant and technician availability.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Set urgency and target schedule.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Assign MST/technician.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Notify technician or generate activity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Update status to Scheduled.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	MST schedule is recorded and assigned after clearance.		Pass / Fail	

UAT-JO-005 - Work Completion and Job Order Closure
Field	Details
Objective	Validate job completion, documentation, and closure.
Odoo Modules	Maintenance, Helpdesk, Documents, Studio
Primary Roles / Testers	MST, PMO/Admin
Preconditions	Scheduled job order exists.
Required Test Data	Completion notes, photos, technician remarks.
Required Evidence	Completion photos, notes, closed ticket/job order.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Technician starts work and updates status to In Progress.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Technician completes work.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Enter completion notes.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach completion photos.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Admin reviews completion.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Assign or confirm Job Order Number.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Close job order and related Helpdesk ticket.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Job order is closed only after completion evidence and Admin documentation.		Pass / Fail	

UAT-JO-006 - Job Order Rate Management
Field	Details
Objective	Validate standard job order rate catalog and rate approval.
Odoo Modules	Maintenance, Helpdesk, Accounting, Studio
Primary Roles / Testers	PMO/Admin, Accounting, Management
Preconditions	Job order rate categories configured.
Required Test Data	Service category and rates.
Required Evidence	Rate catalog entry and approval record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create or edit job order service rate.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Select category such as mechanical, plumbing, carpentry/masonry, electrical, or other.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Tag subject to assessment if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Tag materials separate if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit rate update approval if required.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Use approved rate in job order computation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Only approved active rates are used in job order charges.		Pass / Fail	

Procurement
UAT-PRC-001 - Purchase Requisition
Field	Details
Objective	Validate PR creation, department checking, GM approval, and endorsement to procurement.
Odoo Modules	Approvals, Purchase, Documents, Studio
Primary Roles / Testers	Department Requestor, Department Head, GM, Procurement
Preconditions	Approval categories configured.
Required Test Data	Item description, specs, quantity, purpose, attachments.
Required Evidence	Approved PR record and approval history.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create PR request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Enter complete item specifications, quantity, and purpose.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Submit to Department Head.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Department Head reviews.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit to GM for approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Procurement receives only approved PR.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Attempt changes after approval and verify reapproval/control if changed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	PR proceeds only after required approvals; approved details are controlled.		Pass / Fail	

 
UAT-PRC-002 - Strategic Sourcing and Supplier Canvass
Field	Details
Objective	Validate supplier sourcing, 3 quotations, comparison sheet, manager check, and GM approval.
Odoo Modules	Purchase, Approvals, Documents, Studio
Primary Roles / Testers	Procurement Assistant, Procurement Manager, GM
Preconditions	Approved PR exists.
Required Test Data	Three supplier quotations, price, availability, delivery, terms.
Required Evidence	Canvass sheet, quotations, approval history.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open approved PR.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Create sourcing/canvass record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Attach at least three quotations.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Encode comparison details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Procurement Manager reviews comparison.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	GM approves supplier selection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Move to PO preparation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Supplier comparison is documented and approved before PO preparation.		Pass / Fail	

UAT-PRC-003 - Repeat Order
Field	Details
Objective	Validate repeat order path using previous PO within six months and updated quotation.
Odoo Modules	Purchase, Documents, Studio
Primary Roles / Testers	Procurement
Preconditions	Repeat purchase request exists.
Required Test Data	Previous PO, updated quotation, price check.
Required Evidence	Previous PO reference, updated quotation, route decision.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create PR for repeat item.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Search previous PO within 6 months.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Attach updated quotation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Compare price to previous PO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	If same price, route to PO approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	If price increased or no previous PO, route to full sourcing with three suppliers.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Repeat order is streamlined only when previous PO and same price are validated.		Pass / Fail	

UAT-PRC-004 - RFQ / PO Creation and GM PO Approval
Field	Details
Objective	Validate official PO preparation and approval.
Odoo Modules	Purchase, Approvals, Documents, Accounting, Studio
Primary Roles / Testers	Procurement Assistant, Procurement Manager, GM
Preconditions	Approved PR and approved canvass/repeat order route exist.
Required Test Data	Supplier, item, quantity, price, terms, attachments.
Required Evidence	Approved PO with attachments and approval history.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create RFQ/PO from approved sourcing.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Attach PR, canvass if applicable, and quotation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Validate item, quantity, price, delivery and payment terms.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Procurement Manager checks PO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	GM approves PO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Set PO status to approved/ready for supplier.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	PO cannot be sent unless approved by GM. Attachments are complete.		Pass / Fail	

UAT-PRC-005 - PO Email to Supplier
Field	Details
Objective	Validate PO sending by email only and supplier acceptance tracking.
Odoo Modules	Purchase, Documents, Studio
Primary Roles / Testers	Procurement
Preconditions	PO approved by GM.
Required Test Data	Supplier email and approved PO.
Required Evidence	Email log, sent status, supplier acceptance record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open approved PO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Send PO to supplier by email.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Record email sent status/date.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record supplier acceptance or confirmation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Set status to waiting for delivery.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Only approved PO is sent to supplier and acceptance is tracked.		Pass / Fail	

Procurement / Inventory
UAT-PRC-006 - Delivery, Warehouse Receiving, and Goods Receipt
Field	Details
Objective	Validate supplier delivery, quantity/condition check, and goods receipt.
Odoo Modules	Inventory, Purchase, Documents, Accounting, Studio
Primary Roles / Testers	Warehouse, Procurement, Accounting
Preconditions	PO waiting for delivery.
Required Test Data	Delivery receipt/invoice, delivered items.
Required Evidence	Goods Receipt, delivery documents, discrepancy notes if any.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Receive supplier delivery.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Check item description, quantity, packaging, and condition.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Compare delivery against PO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record discrepancy if any.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Create Goods Receipt.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Update stock or receiving status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Endorse documents for payment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Goods receipt is recorded after warehouse checking and PO matching.		Pass / Fail	

Procurement / Accounting
UAT-PRC-007 - 3-Way Match
Field	Details
Objective	Validate matching of PO, Goods Receipt, and supplier invoice before payment.
Odoo Modules	Purchase, Inventory, Accounting, Documents, Studio
Primary Roles / Testers	Accounting, Procurement, Warehouse
Preconditions	PO, GR, and supplier invoice available.
Required Test Data	PO details, GR quantity, invoice amount.
Required Evidence	3-way match checklist and validation status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open supplier invoice/payment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Check PO details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Check Goods Receipt.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Check invoice amount and quantity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Validate PO-GR-Invoice consistency.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Record match result or discrepancy.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Payment processing only proceeds after 3-way match is cleared or exception approved.		Pass / Fail	

 
UAT-PRC-008 - Payment Request and Supplier Payment
Field	Details
Objective	Validate payment request preparation, approval, vendor bill, and payment.
Odoo Modules	Accounting, Purchase, Inventory, Documents, Approvals, Studio
Primary Roles / Testers	Procurement, Accounting, Finance
Preconditions	Goods Receipt and invoice complete.
Required Test Data	PR, PO, canvass, quotation, GR, invoice, payment terms.
Required Evidence	Payment request, vendor bill, payment record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create Payment Request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Attach PR, PO, canvass, quotation, GR, and invoice.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Procurement Manager approves payment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Accounting checks documents and due date.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Create or validate vendor bill.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Secure payment approval if required.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Post supplier payment and close request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Supplier payment has complete documentation, approval, vendor bill, and payment posting.		Pass / Fail	

Inventory / Warehouse
UAT-INV-001 - Product Master Setup
Field	Details
Objective	Validate product master creation for purchasing and inventory.
Odoo Modules	Inventory, Purchase, Studio
Primary Roles / Testers	Warehouse, Procurement, Admin
Preconditions	Product categories and UOMs configured.
Required Test Data	Product name, category, UOM, type, supplier, reorder level.
Required Evidence	Product master record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create product record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Assign category and UOM.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Set product type: stockable, consumable, service, or asset.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Assign supplier if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Set reorder/minimum stock level if required.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Activate product for purchase/inventory.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Product can be used in PR/PO/inventory transaction with correct category and tracking.		Pass / Fail	

UAT-INV-002 - Stock Monitoring and Low Stock Review
Field	Details
Objective	Validate monitoring of on-hand stock and replenishment trigger.
Odoo Modules	Inventory, Purchase, Studio
Primary Roles / Testers	Warehouse, Admin, Procurement
Preconditions	Products and stock quantities configured.
Required Test Data	Stock item with reorder point.
Required Evidence	Stock report and replenishment PR/reference.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open inventory stock report.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Review on-hand quantity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Compare quantity against reorder point.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Identify low stock item.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Prepare replenishment PR or alert Procurement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Verify stock report updates.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Low stock items are identified and can be routed to replenishment.		Pass / Fail	

UAT-INV-003 - Stock Release
Field	Details
Objective	Validate item release to requestor and stock deduction.
Odoo Modules	Inventory, Approvals, Documents, Studio
Primary Roles / Testers	Warehouse, Admin, Requestor
Preconditions	Approved stock or office supplies request.
Required Test Data	Item, approved quantity, requestor, acknowledgement.
Required Evidence	Stock release record and updated quantity.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open approved request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Check stock availability.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Release approved quantity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record requestor acknowledgement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Validate inventory deduction.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	File stock release record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Released quantity reduces inventory and has acknowledgement.		Pass / Fail	

UAT-INV-004 - Asset Tagging, Monitoring, Transfer, and Deployment
Field	Details
Objective	Validate asset tagging after delivery and deployment tracking.
Odoo Modules	Inventory, Accounting, Documents, Studio
Primary Roles / Testers	Warehouse, PMO/Admin, Accounting
Preconditions	Asset item received through Goods Receipt.
Required Test Data	Asset code, serial, location, accountable person.
Required Evidence	Asset record, tag number, transfer form, deployment status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Identify received item as asset.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Assign asset code/tag number.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Label or record asset tag.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Create/update asset monitoring record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Prepare transfer form.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Assign accountable person/location.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Deploy asset and update status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Asset is tagged before deployment and linked to PO/GR/accountable person.		Pass / Fail	

UAT-INV-005 - Consumable Flow
Field	Details
Objective	Validate consumable request, release, monitoring, and replenishment.
Odoo Modules	Inventory, Purchase, Approvals, Documents, Studio
Primary Roles / Testers	Requestor, Warehouse, Procurement
Preconditions	Consumable stock exists.
Required Test Data	Consumable item, requestor, stock threshold.
Required Evidence	Release record, stock report, replenishment PR if triggered.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Request consumable item.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Warehouse checks availability.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Release item if stock available.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Update stock quantity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Monitor on-hand quantity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	If low stock, raise replenishment PR.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Route replenishment to Procurement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Consumables are released from stock and replenished through PR when low.		Pass / Fail	

 
Office Supplies
UAT-OSR-001 - Office Supplies Request and Approval
Field	Details
Objective	Validate OSR filing, approval, and Admin review.
Odoo Modules	Approvals, Inventory, Purchase, Accounting, Documents, Studio
Primary Roles / Testers	Requesting Department, Department Head, Admin
Preconditions	OSR form and approval category configured.
Required Test Data	Office supplies request by department.
Required Evidence	Approved OSR record and approval history.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Requesting department fills up OSR.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Submit to Department Head.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Department Head approves.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Admin reviews request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Admin confirms request is valid and reasonable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Move to stock availability check.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	OSR proceeds only after department approval and Admin review.		Pass / Fail	

UAT-OSR-002 - Stock Check and Issue Available Items
Field	Details
Objective	Validate release of items when stock is available.
Odoo Modules	Approvals, Inventory, Documents, Studio
Primary Roles / Testers	Admin, Warehouse, Requestor
Preconditions	Approved OSR and available stock.
Required Test Data	Requested item and approved quantity.
Required Evidence	Issue record, acknowledgement, stock movement.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Admin checks stock availability.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Confirm sufficient stock.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Issue item to requesting department.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record item issuance.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Requestor acknowledges receipt.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Inventory quantity updates.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Available items are issued directly without PR and stock is updated.		Pass / Fail	

UAT-OSR-003 - No Stock to PR and Procurement
Field	Details
Objective	Validate no-stock branch from OSR to PR, procurement, payment, receipt, and return to Admin.
Odoo Modules	Approvals, Purchase, Inventory, Documents, Studio
Primary Roles / Testers	Admin, Procurement, Accounting
Preconditions	Approved OSR and no stock available.
Required Test Data	Requested item and PR details.
Required Evidence	PR, PO, receipt, payment reference, issuance record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Admin marks item as not available.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Admin creates PR to Procurement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	GM/procurement approval is completed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Procurement processes RFQ/canvass and PO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Accounting processes payment if required.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Warehouse receives item.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Item returns to Admin for issuance.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	No-stock OSR creates controlled procurement path before issuance.		Pass / Fail	

UAT-OSR-004 - Office Supplies Distribution and Acknowledgement
Field	Details
Objective	Validate distribution of received/available supplies and filing.
Odoo Modules	Inventory, Documents, Studio
Primary Roles / Testers	Admin, Warehouse, Requesting Department
Preconditions	Items are available for issuance.
Required Test Data	Department, item, quantity, acknowledgement.
Required Evidence	Distribution record and acknowledgement.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Prepare items for distribution.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify item and quantity.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Release to requesting department.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Obtain acknowledgement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Update stock.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	File distribution record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Distribution is documented and stock is updated.		Pass / Fail	

Fleet / Vehicle
UAT-FLT-001 - Internal Vehicle Errand
Field	Details
Objective	Validate internal vehicle request, review, consolidation, assignment, trip, and closure.
Odoo Modules	Fleet, Approvals, Documents, Studio
Primary Roles / Testers	Employee, Admin, Driver
Preconditions	Vehicle and driver records configured.
Required Test Data	Request purpose, destination, date/time, passengers.
Required Evidence	Vehicle request, assignment, trip record, closure status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Employee creates internal vehicle request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Admin reviews request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Admin consolidates trips by area if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Assign vehicle and driver.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Driver conducts trip.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Driver completes trip record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Admin files record and closes request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Internal vehicle errand is approved/scheduled, trip recorded, and closed.		Pass / Fail	

UAT-FLT-002 - Special Client Trip Request
Field	Details
Objective	Validate client trip request intake and evaluation.
Odoo Modules	Fleet, Invoicing, Accounting, Documents, Approvals, Studio
Primary Roles / Testers	Client/GSD, Admin, Driver, Accounting
Preconditions	Vehicle/GSD workflow configured.
Required Test Data	Client name, trip details, passengers, destination.
Required Evidence	Trip request, assessment status, client decision.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	GSD receives client trip request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	GSD logs trip details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Admin reviews availability and classification.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Admin determines whether chargeable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	If declined by client, close as declined with reason.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	If approved, proceed to billing/collection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Special client trip is logged, assessed, and routed based on client approval.		Pass / Fail	

 
UAT-FLT-003 - Vehicle Billing Assessment and Client Approval
Field	Details
Objective	Validate billing computation and client approval for chargeable trips.
Odoo Modules	Fleet, Invoicing, Accounting, Studio
Primary Roles / Testers	Admin, GSD, Client
Preconditions	Chargeable special trip request exists.
Required Test Data	Rates, route, charges, client approval.
Required Evidence	Billing computation and client approval record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Admin computes trip charges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Include base rate, distance, waiting time, toll/parking/fuel surcharge if applicable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Send computation to GSD/client.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Client approves or declines.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	If approved, move to collection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	If declined, mark request declined.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Billing assessment is documented and approved before collection/scheduling.		Pass / Fail	

UAT-FLT-004 - GSD Collection and AR Issuance
Field	Details
Objective	Validate GSD collection, acknowledgement receipt, and endorsement.
Odoo Modules	Accounting, Invoicing, Fleet, Documents, Studio
Primary Roles / Testers	GSD, Accounting, Admin
Preconditions	Chargeable client trip approved.
Required Test Data	Payment, AR number, collection log.
Required Evidence	AR, proof of payment, collection log, endorsement record.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	GSD collects payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Issue acknowledgement receipt.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Record collection in log.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Attach proof of payment/AR.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Endorse documents to Accounting next business day.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Admin schedules vehicle after payment confirmation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Collection is recorded with AR and endorsed to Accounting before closure.		Pass / Fail	

UAT-FLT-005 - Driver Trip Record
Field	Details
Objective	Validate actual trip record after vehicle trip.
Odoo Modules	Fleet, Documents, Studio
Primary Roles / Testers	Driver, Admin
Preconditions	Trip scheduled and executed.
Required Test Data	Mileage, fuel, remarks, date/time.
Required Evidence	Driver trip record and filing status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Driver completes trip.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Record actual trip details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Enter mileage and fuel information.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Add trip remarks.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit trip record to Admin.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Admin reviews and files.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Trip record is complete and filed for monitoring/accounting reference.		Pass / Fail	

UAT-FLT-006 - Accounting Collection Verification
Field	Details
Objective	Validate Accounting verification of GSD collections.
Odoo Modules	Accounting, Invoicing, Fleet, Documents, Studio
Primary Roles / Testers	Accounting, GSD, Admin
Preconditions	GSD endorsed AR/proof/trip record/summary.
Required Test Data	Billing computation, AR, proof, trip record, collection summary.
Required Evidence	Accounting verification record and updated monitoring.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Accounting receives collection documents.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify collected amount against billing computation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Validate AR issuance.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record collection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Update monitoring log.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Report discrepancy if any.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Mark collection verified and close trip.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Chargeable trip cannot close without Accounting verification.		Pass / Fail	

Accounting and Billing
UAT-ACC-001 - Move-In Billing and Payment Clearance
Field	Details
Objective	Validate invoice preparation, charge verification, tenant payment, and move-in clearance.
Odoo Modules	Accounting, Invoicing, Lease Module Package, Sales, Subscriptions, Studio
Primary Roles / Testers	Billing, Accounting, Leasing
Preconditions	Move-in clearance prepared.
Required Test Data	Move-in charges and payment proof.
Required Evidence	Move-in invoice, payment posting, clearance status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Billing prepares move-in invoice.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Accounting verifies charges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Tenant pays required amount.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Payment is posted.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Status becomes Move-In Financially Cleared.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Notify Leasing/PMO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Move-in cannot proceed until payment is posted and clearance status is updated.		Pass / Fail	

UAT-ACC-002 - Monthly Rental Billing and Outstanding Balance Monitoring
Field	Details
Objective	Validate monthly invoice generation and collection monitoring.
Odoo Modules	Subscriptions, Accounting, Invoicing, Lease Module Package
Primary Roles / Testers	Billing, Accounting
Preconditions	Active lease with recurring billing setup.
Required Test Data	Monthly rental amount and billing date.
Required Evidence	Monthly invoice, payment record, outstanding balance report.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Generate monthly invoice for active lease.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify billing period and amount.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Send invoice on required billing schedule.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record tenant payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Post payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Review outstanding balances.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Active leases generate invoices and outstanding balances are monitored.		Pass / Fail	

 
UAT-ACC-003 - PMO Job Order Payment Verification
Field	Details
Objective	Validate payment verification before MST scheduling.
Odoo Modules	Accounting, Invoicing, Helpdesk, Maintenance, Studio
Primary Roles / Testers	Accounting, Admin, PMO
Preconditions	Signed job order with amount due.
Required Test Data	Payment proof, receipt number.
Required Evidence	Payment verification status, receipt number, notification.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Receive job order amount from Admin.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Confirm tenant-signed job order.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Receive proof of payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify payment and receipt number.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Mark payment verified.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Notify Admin that MST scheduling is allowed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	MST scheduling is allowed only after payment verification or approved exception.		Pass / Fail	

UAT-ACC-004 - Move-Out Billing and Settlement
Field	Details
Objective	Validate computation of final move-out obligations and settlement.
Odoo Modules	Accounting, Invoicing, Lease Module Package, Documents, Studio
Primary Roles / Testers	Billing, Accounting, PMO
Preconditions	Final inspection and final utility readings completed.
Required Test Data	Utilities, unpaid rent, damage, cleaning, penalties, missing items.
Required Evidence	Final billing, payment/deduction, clearance status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Receive final inspection findings from PMO.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Receive final utility readings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Compute final utility charges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Compute unpaid rent, damage, cleaning, penalties, missing items, and other charges.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Prepare final invoice/settlement.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Record tenant payment or deposit deduction.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Mark financially cleared.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Final billing includes all applicable move-out charges and clearance is recorded.		Pass / Fail	

UAT-ACC-005 - Damage and Missing Item Charges
Field	Details
Objective	Validate chargeable findings through billing and payment/deposit deduction.
Odoo Modules	Accounting, Invoicing, Lease Module Package, Documents, Studio
Primary Roles / Testers	PMO, Billing, Accounting
Preconditions	Move-out finding recorded and confirmed chargeable.
Required Test Data	Finding, amount, invoice or deduction decision.
Required Evidence	Finding record, invoice/deduction, payment status.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	PMO records finding.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Manager confirms finding is chargeable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Billing computes amount.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Accounting validates invoice or deduction.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Tenant pays or amount is deducted from deposit.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Record final status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Chargeable findings are either paid or deducted from security deposit.		Pass / Fail	

UAT-ACC-006 - Security Deposit Deduction and Refund
Field	Details
Objective	Validate deposit deduction computation, approval, refund release, and documentation.
Odoo Modules	Accounting, Approvals, Documents, Lease Module Package, Studio
Primary Roles / Testers	Accounting, Finance, Management
Preconditions	Move-out settlement completed.
Required Test Data	Deposit amount, deductions, refund bank details.
Required Evidence	Refund approval, computation, proof of release.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open tenant deposit record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Apply approved deductions.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Compute net refund.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Obtain tenant bank details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Submit refund for Finance approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Release refund.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Attach proof of refund and close account.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Refund is released only after clearance and approval; deductions are documented.		Pass / Fail	

UAT-ACC-007 - Vendor Bill and Supplier Payment
Field	Details
Objective	Validate vendor bill and supplier payment after payment request.
Odoo Modules	Accounting, Purchase, Inventory, Documents, Approvals, Studio
Primary Roles / Testers	Accounting, Procurement
Preconditions	Payment request and 3-way match completed.
Required Test Data	Vendor bill, due date, payment terms.
Required Evidence	Vendor bill, payment record, closed request.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Receive approved payment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Check PR, canvass, quotation, PO, GR, and invoice.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Validate 3-way match.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Create/validate vendor bill.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Secure payment approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Post supplier payment.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Close payment request.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Supplier payment is processed with complete documents and valid vendor bill.		Pass / Fail	

UAT-ACC-008 - Vehicle Collection Verification
Field	Details
Objective	Validate accounting verification of vehicle trip collections.
Odoo Modules	Accounting, Invoicing, Fleet, Documents, Studio
Primary Roles / Testers	Accounting, GSD
Preconditions	Chargeable trip completed and GSD endorsed documents.
Required Test Data	AR, proof, trip record, collection summary.
Required Evidence	Verification record, collection posting, discrepancy log if any.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Receive AR copy, proof, trip record, and collection summary.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Compare amount with billing computation.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Validate receipt details.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Record collection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Flag discrepancy if any.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Mark trip collection verified.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Collection is verified, recorded, and discrepancies are reported.		Pass / Fail	

 
Approval Management
UAT-CTRL-001 - General Approval Process
Field	Details
Objective	Validate request submission, approval, and audit trail.
Odoo Modules	Approvals, Studio
Primary Roles / Testers	Requestor, Reviewer, Approver
Preconditions	Approval categories configured.
Required Test Data	Sample request with required documents.
Required Evidence	Approval record and audit history.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create request under defined approval category.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Complete required fields and attach required documents.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Submit for approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Approver reviews and approves.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify status and approval history.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Verify approved request proceeds to next process.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Approval status, approver, date/time, and comments are captured.		Pass / Fail	

UAT-CTRL-002 - Return and Rejection Handling
Field	Details
Objective	Validate returned and rejected requests with reasons.
Odoo Modules	Approvals, Studio
Primary Roles / Testers	Requestor, Approver
Preconditions	Approval category configured.
Required Test Data	Sample incomplete or invalid request.
Required Evidence	Return/rejection reason and status report.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Create request and submit for approval.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Approver returns request with reason.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Requestor revises and resubmits.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Approver rejects another sample request with reason.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify rejected request closes with reason.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Verify returned/rejected records are reportable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Returned request goes back to requestor; rejected request is closed with reason.		Pass / Fail	

Document Management
UAT-DOC-001 - Document Filing
Field	Details
Objective	Validate upload, tagging, linking, review, and archive of documents.
Odoo Modules	Documents, Studio
Primary Roles / Testers	All Departments, Document Controller
Preconditions	Documents folders and tags configured.
Required Test Data	Sample lease, PR, PO, GR, job order, payment proof.
Required Evidence	Document record, folder, tags, linked transaction.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Upload document to correct folder.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Apply document tag.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Link document to related record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Review completeness.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Mark document as filed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Archive document if process closed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Document is searchable, tagged, linked, and filed in correct folder.		Pass / Fail	

UAT-DOC-002 - Document Access, Folder, and Sensitive Record Control
Field	Details
Objective	Validate access rights for sensitive folders and department records.
Odoo Modules	Documents, Studio
Primary Roles / Testers	Document Controller, System Admin, Department Users
Preconditions	Document access matrix configured.
Required Test Data	Sensitive tenant/accounting/payroll-like sample document if applicable.
Required Evidence	Access test evidence and permission result.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Upload sample document to restricted folder.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Log in as authorized user and verify access.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Log in as unauthorized user and verify access is restricted.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Check document tags and linked record.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Confirm file can be found by authorized search only.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Sensitive documents are visible only to authorized users and correctly linked.		Pass / Fail	

Reporting and Dashboard
UAT-RPT-001 - Leasing Dashboard
Field	Details
Objective	Validate leasing KPIs and filters.
Odoo Modules	CRM, Lease Module Package, Accounting, Studio
Primary Roles / Testers	Leasing Manager, Management
Preconditions	Sample transactions exist.
Required Test Data	New inquiries, oculars, quotations, reservations, move-ins, move-outs, expiring leases, refunds.
Required Evidence	Dashboard screenshots and sample reconciliation.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open Leasing dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify new inquiries count.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify ocular visit/quotation/reservation data.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify move-in/move-out/expiry/refund data.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Filter by date/status/agent.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Export or view report if needed.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Leasing dashboard reflects transactions accurately and filters work.		Pass / Fail	

UAT-RPT-002 - PMO Dashboard
Field	Details
Objective	Validate PMO pending inspections, utility readings, job orders, and filings.
Odoo Modules	Maintenance, Helpdesk, Lease Module Package, Studio
Primary Roles / Testers	PMO/Admin Manager, Management
Preconditions	Sample PMO transactions exist.
Required Test Data	Move-in/out inspections, job orders, MST assignments.
Required Evidence	Dashboard screenshots and sample records.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open PMO dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify pending move-in inspection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify pending utility reading.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify move-out final inspection and damage findings.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify job order open/paid-not-scheduled/completed counts.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Filter by status/team/date.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	PMO dashboard accurately shows pending and completed PMO workload.		Pass / Fail	

 
UAT-RPT-003 - Procurement Dashboard
Field	Details
Objective	Validate PR, canvass, PO, delivery, and payment request reports.
Odoo Modules	Purchase, Approvals, Inventory, Studio
Primary Roles / Testers	Procurement Manager, Management
Preconditions	Sample procurement transactions exist.
Required Test Data	PRs, canvass records, POs, GRs, payment requests.
Required Evidence	Dashboard screenshots and sample transaction reconciliation.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open Procurement dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify PR monitoring.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify canvass and PO approval status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify waiting/partial delivery status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify payment request monitoring.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Filter by supplier/date/status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Procurement dashboard shows accurate transaction status and bottlenecks.		Pass / Fail	

UAT-RPT-004 - Inventory Dashboard
Field	Details
Objective	Validate stock on hand, low stock, stock release, goods receipt, asset tagging, replenishment.
Odoo Modules	Inventory, Purchase, Studio
Primary Roles / Testers	Warehouse, Admin, Management
Preconditions	Sample inventory transactions exist.
Required Test Data	Products, receipts, releases, assets, low stock items.
Required Evidence	Dashboard and stock report evidence.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open Inventory dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify stock on hand.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify low stock items.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify goods receipt report.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify stock release report.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Verify asset tagging pending and replenishment required.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Filter by product/location/category.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Inventory dashboard reflects stock and transaction status accurately.		Pass / Fail	

UAT-RPT-005 - Accounting Dashboard
Field	Details
Objective	Validate tenant billing, outstanding balances, deposits, vendor bills, job order revenue, vehicle collections.
Odoo Modules	Accounting, Invoicing, Purchase, Inventory, Fleet, Studio
Primary Roles / Testers	Accounting Manager, Finance, Management
Preconditions	Sample invoices/payments exist.
Required Test Data	Tenant invoices, vendor bills, refund records, vehicle collections.
Required Evidence	Dashboard screenshots and sample reconciliation.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open Accounting dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify tenant billing and outstanding balances.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify security deposit/refund monitoring.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify vendor bills payable.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify job order revenue and vehicle collection verification.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Check collection discrepancy report.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Filter by date/status/customer/supplier.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Accounting dashboard supports financial monitoring and exception review.		Pass / Fail	

UAT-RPT-006 - Fleet Dashboard
Field	Details
Objective	Validate vehicle requests, availability, driver assignments, trips, chargeable trips, collections.
Odoo Modules	Fleet, Accounting, Studio
Primary Roles / Testers	Fleet/Admin, GSD, Management
Preconditions	Sample fleet transactions exist.
Required Test Data	Vehicle requests, trip records, billing, collection verification.
Required Evidence	Fleet dashboard screenshots and sample records.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open Fleet dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify vehicle requests and availability.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify driver assignments and trip schedules.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify completed and chargeable trips.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify transportation revenue and outstanding collections.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Filter by date/vehicle/driver/status.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Fleet dashboard supports utilization and collection monitoring.		Pass / Fail	

UAT-RPT-007 - Management KPI Dashboard
Field	Details
Objective	Validate high-level KPI dashboard for all Phase 1 workstreams.
Odoo Modules	All Phase 1 Modules, Studio
Primary Roles / Testers	Management, Department Heads
Preconditions	Sample transactions exist across modules.
Required Test Data	Occupancy, move-ins, move-outs, approvals, payments, PRs, job orders, collections, documents.
Required Evidence	Dashboard screenshots and sample KPI validation.

Step	Test Action	Expected Result	Actual Result	Status	Remarks
1	Open management KPI dashboard.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
2	Verify occupancy, move-ins, and move-outs.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
3	Verify pending payment clearance and PMO inspection.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
4	Verify open PRs, PO approvals, and vendor payments.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
5	Verify outstanding tenant balances and refund requests.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
6	Verify vehicle collections and document compliance.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
7	Check pending approvals.	System accepts valid input, updates the record/status, and preserves audit trail as applicable.		Pass / Fail	
Final	Review overall process result and required evidence.	Management dashboard gives accurate overall operational visibility.		Pass / Fail	

 
12. UAT Issue Log Template
Issue ID	Date	Test Case ID	Module / Process	Issue Description	Severity	Owner	Target Date	Status	Resolution / Retest Result
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	
					Critical / Major / Minor / Enhancement / Change Request			Open / In Progress / Resolved / Deferred / Closed	

13. UAT Daily Status Report Template
Reporting Date	Prepared By	UAT Day / Session	Overall Status
			Green / Amber / Red

Workstream	Planned Test Cases	Executed	Passed	Failed	Blocked	Remarks
Leasing / CRM						
PMO / Job Order / Maintenance						
Procurement / Inventory / OSR						
Accounting / Fleet						
Approvals / Documents / Reports						

Key Accomplishments	Open Blockers	Required Decisions	Next-Day Plan
			
			
			
			

 
14. Department UAT Sign-Off Forms
Leasing / Sales UAT Sign-Off
Field	Details
Department	Leasing / Sales
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

PMO / Admin UAT Sign-Off
Field	Details
Department	PMO / Admin
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Maintenance / Helpdesk / MST UAT Sign-Off
Field	Details
Department	Maintenance / Helpdesk / MST
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Procurement UAT Sign-Off
Field	Details
Department	Procurement
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Warehouse / Inventory UAT Sign-Off
Field	Details
Department	Warehouse / Inventory
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Accounting / Finance / Billing UAT Sign-Off
Field	Details
Department	Accounting / Finance / Billing
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Admin Office Supplies UAT Sign-Off
Field	Details
Department	Admin Office Supplies
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Fleet / GSD UAT Sign-Off
Field	Details
Department	Fleet / GSD
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Website / Marketing UAT Sign-Off
Field	Details
Department	Website / Marketing
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

Approvals / Documents / Management Reporting UAT Sign-Off
Field	Details
Department	Approvals / Documents / Management Reporting
Process Owner	
UAT Date(s)	
Test Cases Executed	
Passed	
Failed / Deferred	
Open Critical Issues	None / List Issue IDs
Open Major Issues	None / List Issue IDs
Accepted Workarounds	
Department Ready for Go-Live?	Yes / No / Conditional
Remarks	

Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

 
15. Final UAT Summary Report Template
Field	Details
Project	Odoo Phase 1 Implementation
UAT Period	
Prepared By	
Reviewed By	
Overall UAT Result	Passed / Passed with Conditions / Failed

Metric	Count / Status
Total test cases planned	77
Total test cases executed	
Passed test cases	
Failed test cases	
Blocked test cases	
Open critical issues	
Open major issues	
Open minor issues	
Accepted workarounds	
Change requests raised	

Workstream	Result	Summary Remarks
Leasing / CRM		
PMO / Job Order / Maintenance		
Procurement / Inventory / OSR		
Accounting / Fleet / Collections		
Approvals / Documents / Website / Reports		

Open Item	Classification	Owner	Target Date	Go-Live Impact
	Support / Enhancement / Change Request			
	Support / Enhancement / Change Request			
	Support / Enhancement / Change Request			
	Support / Enhancement / Change Request			
	Support / Enhancement / Change Request			
	Support / Enhancement / Change Request			

16. Go / No-Go Recommendation Form
Readiness Area	Ready? Yes / No / Conditional	Remarks
UAT completed by required departments		
All critical issues resolved		
Major issues resolved or accepted with workaround		
Master data validated		
User access validated		
Approval routes validated		
Document filing validated		
Dashboards and reports validated		
Users trained		
Support team ready for go-live		

Field	Details
Recommendation	Go / No-Go / Go with Conditions
Recommended Go-Live Date	
Conditions Before Go-Live	
Approved Deferred Items	
Final Remarks	

Management Approval
Name	Role / Department	Signature	Date	Remarks
				
				
				
				

 
Appendix A: Phase 1 Critical Control Validation Checklist
No.	Critical Control	Validated? Yes / No	Test Case / Evidence	Remarks
1	No reservation without verified payment.			
2	No lease contract without complete BIS and tenant documents.			
3	No move-in without payment clearance, contract signing, and unit readiness.			
4	No access card release without payment.			
5	No parking assignment without required documents and payment.			
6	No Wi-Fi installation without payment unless approved.			
7	No chargeable job order scheduling without full payment unless approved by Management.			
8	No move-out closure without final inspection and settlement.			
9	No security deposit refund without move-out clearance.			
10	No PR processing without General Manager approval.			
11	No PO sending without General Manager approval.			
12	No vendor payment without complete documents and Goods Receipt.			
13	No chargeable vehicle trip scheduling without payment confirmation unless approved.			
14	No GSD collection closure without Accounting verification.			
15	No office supplies walk-in request unless justified and approved.			
16	No approved records should be changed without proper approval.			
17	All documents must be filed in Odoo Documents.			
18	All exceptions must be approved through Odoo Approvals.			
19	All closed records must be locked or controlled.			
20	All dashboards must be reviewed regularly by Management.			

Appendix B: UAT Evidence Checklist
Evidence Type	Required For	Examples
Screenshot	All pass/fail evidence	Record screen, status, approval trail, dashboard
Attached Document	Document-based workflows	Proof of payment, contract, PR, PO, GR, job order, trip record
Report Export	Dashboard/report validation	Leasing, PMO, Procurement, Inventory, Accounting, Fleet dashboards
Approval History	Controlled workflows	Approver name, approval date, comments
Payment Posting Record	Accounting controls	Receipt, invoice, payment, vendor bill, refund
Exception Approval	Waivers or overrides	Management exception approval, waiver reason

