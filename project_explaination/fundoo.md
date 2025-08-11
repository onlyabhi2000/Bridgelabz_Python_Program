📌 Project Overview:
This project is a Notes Management System built with FastAPI, PostgreSQL, and SQLAlchemy, designed for users to securely create, edit, and organize notes, with the added ability to collaborate with other verified users. It also supports user authentication, labels for categorization, and role-based access control using JWT.

It simulates a production-grade microservice architecture and follows clean separation of concerns using models, schemas, routers, and utility helpers.

🚀 Key Features and Functionality:
User Authentication and Authorization:

JWT-based login and token validation.

Email and password registration system.

is_verified flag to control access for collaboration.

Note Management:

Users can create, read, update, and delete personal notes.

Notes have title, content, timestamps, and can be labeled.

Labeling System:

Users can assign multiple labels to a note.

Many-to-many relationship between notes and labels.

Collaborator System (Core Feature):

Owners can add other verified users as collaborators on a note.

Collaborators can read and update shared notes.

Only the note owner can delete a note or manage collaborators.

Fully secure with access checks on all endpoints.

Structured Response Format:

All APIs return a standardized response: {"message", "payload", "status"} using a utility wrapper.

Consistent developer and frontend experience.

Modular Design:

Organized under app/api/, app/models/, app/schemas/, and app/utils/.

Clean dependency injection using FastAPI’s Depends.

👨‍💻 My Contribution:
Designed the schema for Notes, Users, Labels, and the Collaborator feature using SQLAlchemy and Alembic migrations.

Implemented JWT authentication with FastAPI dependency injection for secure endpoints.

Created all APIs for:

Notes CRUD operations.

Label assignment and filtering.

Collaborator management with proper authorization.

Built custom response wrappers to return uniform JSON responses across all endpoints.

Used Pydantic v2 with from_attributes for clean data serialization.

Tested user flows by creating and switching between multiple users via curl and Swagger UI.

Collaborated closely on schema integrity, ensuring ownership and permission checks are strictly enforced.

Handled issues like model migration updates, UUID key management, and circular relationships.


