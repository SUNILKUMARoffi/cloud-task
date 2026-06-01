\# Cloud Task Manager



A containerized task management REST API built with FastAPI, PostgreSQL, SQLAlchemy, Docker, and Docker Compose.



\## Overview



Cloud Task Manager is a backend application that allows users to create, retrieve, and delete tasks through REST API endpoints. The application follows a multi-container architecture where FastAPI and PostgreSQL run in separate Docker containers and communicate through a Docker network.



\## Features



\* Create tasks

\* Retrieve all tasks

\* Delete tasks

\* PostgreSQL database persistence

\* SQLAlchemy ORM integration

\* Dockerized deployment

\* Docker Compose orchestration

\* Persistent storage using Docker Volumes

\* Environment variable configuration



\## Tech Stack



\### Backend



\* FastAPI

\* Python

\* SQLAlchemy

\* Pydantic



\### Database



\* PostgreSQL 18



\### DevOps \& Infrastructure



\* Docker

\* Docker Compose

\* Docker Networks

\* Docker Volumes



\### Version Control



\* Git

\* GitHub



\## Project Structure



```text

cloud-task/

│

├── app/

│   ├── main.py          # FastAPI application and API endpoints

│   ├── database.py      # Database connection and session management

│   ├── models.py        # SQLAlchemy models

│   └── schemas.py       # Pydantic request/response schemas

│

├── Dockerfile           # FastAPI container build instructions

├── docker-compose.yml   # Multi-container orchestration

├── requirements.txt     # Python dependencies

├── .env                 # Environment variables

├── .gitignore

└── README.md

```



\## Architecture



```text

Browser / API Client

&#x20;         │

&#x20;         ▼

&#x20;  FastAPI Container

&#x20;         │

&#x20;         ▼

&#x20;    SQLAlchemy ORM

&#x20;         │

&#x20;         ▼

&#x20;PostgreSQL Container

&#x20;         │

&#x20;         ▼

&#x20;Docker Volume

&#x20;(Persistent Storage)

```



\## Quick Start



\### Prerequisites



\* Docker Desktop

\* Git



\### Clone Repository



```bash

git clone https://github.com/SUNILKUMARoffi/cloud-task.git

cd cloud-task

```



\### Configure Environment Variables



Create a `.env` file:



```env

DATABASE\_URL=postgresql://postgres:admin123@postgres:5432/cloud\_task

```



\### Start the Application



```bash

docker compose up -d --build

```



\### Access the API



API Documentation:



```text

http://localhost:8000/docs

```



\## API Endpoints



| Method | Endpoint         | Description   |

| ------ | ---------------- | ------------- |

| GET    | /                | Health Check  |

| GET    | /tasks           | Get All Tasks |

| POST   | /tasks           | Create Task   |

| DELETE | /tasks/{task\_id} | Delete Task   |



\### Example Request



```json

{

&#x20; "title": "Learn Docker Compose"

}

```



\## Environment Variables



| Variable     | Description                  |

| ------------ | ---------------------------- |

| DATABASE\_URL | PostgreSQL connection string |



Example:



```env

DATABASE\_URL=postgresql://postgres:admin123@postgres:5432/cloud\_task

```



\## Learning Outcomes



This project demonstrates:



\* FastAPI CRUD API development

\* PostgreSQL database integration

\* SQLAlchemy ORM usage

\* Pydantic data validation

\* Docker image creation

\* Docker container management

\* Docker networking concepts

\* Docker Compose orchestration

\* Persistent storage using Docker Volumes

\* Environment variable management

\* Git and GitHub workflows



\## Future Enhancements



\* APIRouter-based project structure

\* Database migrations with Alembic

\* JWT Authentication \& Authorization

\* Update Task endpoint

\* Automated testing with Pytest

\* CI/CD Pipeline

\* Kubernetes deployment



```

```



