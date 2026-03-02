# Drive Management API

A RESTful backend service to create and fetch volunteer drives for specific cities.

Built using **FastAPI, SQLAlchemy, Docker**, and deployed on **AWS EC2**.

---

## 🚀 Live Deployment

Swagger UI:

http://15.206.212.47:8000/docs

---

## 🛠 Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite (Local Development)
- Docker & Docker Compose
- AWS EC2 Deployment

---

## 📌 Features

- Create a new drive
- Fetch drives by city
- Input validation using Pydantic
- Proper RESTful API design
- Dockerized application
- Deployed on AWS EC2

---

## 📂 Project Structure

drive-management-api/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routers/
│ └── drives.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
## Running Locally (Without Docker)
1. Create virtual environment:
python -m venv venv
venv\Scripts\activate
2. Install dependencies:
pip install -r requirements.txt
3. Start server:
uvicorn app.main:app --reload
4. Open Swagger:
http://127.0.0.1:8000/docs
## Running with Docker
Build and start container:
docker compose up --build
Access Swagger at:
http://localhost:8000/docs
## API Endpoints
POST /drives/  → Create a new drive
GET /drives?city=Indore  → Fetch drives by city
## Design Decisions
• Clean separation of concerns (models, schemas, routers)
• Proper validation using Pydantic
• Dockerized for portability
• Cloud deployment on AWS EC2
• Production-ready project structure
## Future Improvements
• PostgreSQL integration for production
• Authentication & role-based access control
• Pagination support
• CI/CD using GitHub Actions
• Nginx reverse proxy with SSL
## Author
Prasann Nareliya
B.Tech CSE | DevOps & Backend Enthusiast
