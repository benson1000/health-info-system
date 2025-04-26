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
- **Health Program Management**: Doctors can create health programs such as TB, HIV, and Malaria, and manage the services under each program.
- **Client Registration**: Register clients with basic details (name, age, etc.) to keep track of their health information.
- **Client Enrollment**: Enroll clients in one or more health programs based on their medical needs.
- **Client Profile Viewing**: View detailed client profiles, including personal information and the programs they are enrolled in.
- **API Endpoints for Integration**: Expose client information via RESTful APIs for easy integration with other systems or front-end applications.

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


