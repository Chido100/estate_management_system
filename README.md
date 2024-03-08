RESIDENT MANAGEMENT SYSTEM WEB APP (DJANGO)

Overview

Welcome to the Resident Management System Web App, a comprehensive solution developed using the Django framework. This project aims to streamline and enhance the management of residential estates by incorporating advanced features and technologies.

Features

User Authentication:

Robust authentication system with email verification and password reset functionalities.

Dynamic Dashboard:

A dynamic dashboard providing real-time updates on news and events within the resident estate.

Visitor Access Request System:

Noteworthy feature allowing residents to notify security in advance about expected visitors.

Real-time Notifications:

Implemented seamless real-time notifications throughout the application using Celery for task scheduling and Channels for handling WebSocket connections.

Technologies Used

Django Framework:

The project is built on the powerful and flexible Django web framework.

Celery:

Utilized Celery for efficient task scheduling and background processing.

Channels:

Implemented Channels to handle WebSocket connections, enabling real-time communication.

Getting Started

To run this project locally, follow these steps:

Clone the repository:
git clone https://github.com/Chido100/estate_management_system.git

Navigate to the project directory:
cd ems

Install dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Start the development server:

python manage.py runserver

Access the application at http://localhost:8000/.


