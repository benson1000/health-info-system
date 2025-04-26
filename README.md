# health-info-system
This Health Information System is a secure and scalable Django-based application designed to enable medical professionals (e.g., doctors) to manage health programs and client enrollments



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Deployment](#deployment)

## Introduction
This project simulates a **basic health information system** aimed at managing clients and healthcare programs. The primary goal is to allow a healthcare professional (such as a doctor) to efficiently manage client records and enroll them in relevant health programs like **TB**, **HIV**, and **Malaria**.

The solution provides **RESTful API endpoints** to handle key operations, such as:
- **Creating Health Programs** (e.g., TB, HIV, Malaria)
- **Registering Clients** into the system
- **Enrolling Clients** in one or more health programs
- **Viewing Client Profiles** which include personal details and enrolled programs
- **Exposing Client Data via APIs** for external systems to access and interact with

## Features
- **Create a Health Program**: Doctors can create health programs such as TB, HIV, and Malaria, and manage the services under each program.
- Endpoint: 
    ```http
    POST /api/programs/
    ```
  - Authentication: Required  
- **Client Registration**: Register clients with basic details (name, age, etc.) to keep track of their health information.
- Endpoint: 
    ```http
    POST /api/clients/
    ```
  - Authentication: Required
- **Client Enrollment**: Enroll clients in one or more health programs based on their medical needs.
- Endpoint: 
    ```http
    POST /api/clients/{id}/enroll/
    ```
  - Example Request Body:
    ```json
    {
      "program_ids": [1, 2]
    }
    ```
  - Authentication: Required
- **Search Clients by Name**:
  - Quickly find clients using partial or full names.
  - Endpoint:
    ```http
    GET /api/clients/search/?name=John
    ```
  - Authentication: Required
- **Client Profile Viewing**: View detailed client profiles, including personal information and the programs they are enrolled in.
- Endpoint:
    ```http
    GET /api/clients/{id}/
    ```
  - Authentication: Required
- **REST API Exposure**:
  - All features are accessible via a RESTful API secured with JWT tokens.

- **JWT-Based Authentication**:
  - Secure login and token-based session handling for doctors/admins.
  
  Obtain Token:
  ```http
  POST /api/token/
  ```


Body:
```json
{
  "username": "benso",
  "password": "@Benso7130"
}
```
Use Bearer Token:  
Include the token in request headers:
```makefile
Authorization: Bearer <access_token>
```

## Technologies
- **Python**: The programming language used to build the backend application.
- **Django**: The backend framework used for implementing the core application logic and handling requests.
- **Django REST Framework (DRF)**: Enables the creation of RESTful APIs, making the system accessible to external applications.
- **PostgreSQL**: A relational database used to store client and program data.
- **python-dotenv**: Used for managing environment variables securely across different development environments.

## Setup and Installation

### Prerequisites
- Python 3.12
- PostgreSQL


| Layer | Tech |
| :--- | :--- |
| Backend | Django (v4+) |
| API Framework | Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Database | PostgreSQL |
| Docs/Test | Postman + DRF Browsable UI |

---

📁 Project Structure
```graphql
health_system/
├── core/
│   ├── models.py         # Client & Program models
│   ├── serializers.py    # API serializers
│   ├── views.py          # API views with permissions
│   ├── urls.py           # App URL routes
├── health_system/
│   ├── settings.py       # Project settings
│   ├── urls.py           # Global URL routes
```

---

🧪 API Testing Instructions

Start Server:
```bash
python manage.py runserver
```

Authenticate with JWT:
```http
POST /api/token/
```

Add Token in Postman Headers:
```makefile
Authorization: Bearer <access_token>
```

Use the following endpoints to:
```http
GET/POST /api/clients/
GET/POST /api/programs/
POST /api/clients/{id}/enroll/
GET /api/clients/search/?name=...
GET /api/clients/{id}/
```

---

🔐 Security Considerations
- JWT ensures only authenticated users can access or modify records.
- No sensitive data is exposed in public APIs.
- Future enhancements could include audit logs and field-level encryption.

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/benson1000/health-info-system.git
    cd health-info-system
    ```

2. Activate Virtual environment:
    ```bash
    source venv/bin/activate or if not installed  
    python3 -m venv venv then activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start The Django-Project:
    ```bash
    django-admin startproject cema_health_system
    ```


