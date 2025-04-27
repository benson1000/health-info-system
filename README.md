# health-info-system
This Health Information System is a secure and scalable Django-based application designed to enable medical professionals (e.g., doctors) to manage health programs and client enrollments



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Deployment](#deployment)
- [Supporting Documents](#supporting documents)

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
| Backend | Django (v5+) |
| API Framework | Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Database | PostgreSQL |
| Docs/Test | Postman + DRF Browsable UI + Django REST Framework's APITestCase module|

---

📁 Project Structure
```graphql
health-info-system/
├── core/
    ├──tests/
    ├── test_models.py      # test Client and Program creation
│   ├── test_serializers.py # for ClientSerializer and ProgramSerializer validation
│   ├── test_views.py       # test for Register a client, Enroll a client into Malaria program, Search client, View client profile
│   ├── test_authentication.py           # for Block unauthenticated users from accessing endpoints
│   ├── models.py         # Client & Program models
│   ├── serializers.py    # API serializers
│   ├── views.py          # API views with permissions
│   ├── urls.py           # App URL routes
├── cema_health_system/
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
## Setup and Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/benson1000/health-info-system.git
    cd health-info-system
    ```

2. **Activate Virtual Environment**:
    ```bash
    source venv/bin/activate
    ```
    or if not installed:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start The Django Project**:
    ```bash
    django-admin startproject cema_health_system
    ```

5. **Connect to the Database**:
    - Change directory:
      ```bash
      cd cema_health_system
      ```
    - Install `psycopg2-binary`:
      ```bash
      pip install psycopg2-binary==2.9.10
      ```
    - Then connect to your PostgreSQL database by updating your `settings.py`:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'your_db_name',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```

6. **Run Migrations and Apply Migrations**:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

7. **Run the Server**:
    ```bash
    python3 manage.py runserver
    ```
    - Then open your browser and go to:
      ```text
      http://127.0.0.1:8000/
      ```

    ![Alt text](screenshots/running-code.png)

8. **Run Tests**:
    ```bash
    python3 manage.py test
    ```
    ![Alt text](screenshots/test-results.png)

---

✅ Now your project should be running successfully!

## Deployment

The application has been successfully deployed to Render, and users can interact with the API through the Swagger interface.

To interact with the application and explore the API endpoints, visit the following URL:

[https://health-info-system-ncfp.onrender.com/api/swagger/](https://health-info-system-ncfp.onrender.com/api/swagger/)

This URL provides a user-friendly interface for making requests to the API and understanding the available endpoints.

### Database

For this project, I have used **PostgreSQL** as the database for storing application data. Render provides a fully managed PostgreSQL database, ensuring reliability and scalability.

Feel free to explore the deployed application and interact with the endpoints via the Swagger documentation.


## Supporting Documents

### Prototype Demonstration Video
This video demonstrates the prototype of the Health Info System. You can view the video by clicking the link below:

- [Prototype Demonstration Video](documents/official.mp4)


### PowerPoint Slide
You can also view the PowerPoint slide for the presentation of the Health Info System:

- [Health Info System Presentation (PPT)](documents/Health-Information-System.pptx)