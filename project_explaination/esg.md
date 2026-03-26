Project: ESG Reporting Platform
Tech Stack: Django REST Framework | PostgreSQL | JWT Authentication | Docker | Role-Based Access Control | Email Service

Overview:

The ESG Reporting Platform is a full-fledged backend system designed to help medium to large enterprises — including Banks, NBFCs, Manufacturing units, and IT/Service companies — conduct structured self-assessments around Environmental, Social, and Governance (ESG) factors. The platform enables organizations to assess their ESG contributions and generate formal, auditable ESG reports for internal tracking and regulatory/compliance purposes.

Key Features and Functionality:

Role-Based Workflow and Hierarchy:

The system supports multiple internal roles such as Developer, HR, Manager, Operations, and Senior Leadership.

The assessment flow is hierarchical:

Individual employees fill out ESG-related questionnaires.

Their responses are reviewed by managers, who can edit or update them based on department-level context.

The updated responses are passed on to upper management, who can further refine the inputs before final submission.

Once submitted, the system generates a comprehensive ESG report, which is also sent via email to relevant stakeholders.

Assessment Logic:

This is not a right-or-wrong type questionnaire.

Each question is scenario-based, and every option carries a relative score between 0 and 1, depending on how well it aligns with ESG goals.

Final scores are calculated using weighted logic based on department and role to provide a balanced ESG outlook for the organization.

Report Generation and Delivery:

Upon final submission, the system automatically generates an ESG report summarizing all contributions.

Reports are formatted in a structured and auditable format and are delivered via email notifications.

This report can be used for compliance, investor transparency, and internal tracking.

Why ESG Reporting is Important Today:

In today's global business environment, ESG reporting is becoming increasingly critical. Investors, regulators, and consumers are demanding greater transparency and accountability from companies—not just in financial terms but also in how they manage their impact on society and the environment.

ESG data helps companies evaluate and reduce risks related to environmental damage, poor labor practices, and unethical governance.

It enables sustainable investment and decision-making by banks and financial institutions.

With global ESG standards being adopted in many regions, especially in Europe and North America, having a system that supports accurate ESG reporting has become a competitive necessity.

My Contribution:

Developed and secured RESTful APIs for user roles, assessment submissions, and report generation.

Implemented JWT-based authentication and role-based access control for secure data flow.

Designed and normalized the PostgreSQL schema to support modular assessments and scoring.

Integrated email delivery for automated ESG report dispatch.

Containerized the application using Docker for consistent deployments.