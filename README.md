# 🚀 Cloud & DevOps Portfolio Website

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Pytest](https://img.shields.io/badge/Tests-Pytest-success)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)

A production-ready portfolio application built with **Flask**, showcasing modern backend engineering, containerization, automated testing, and cloud deployment practices.

This project demonstrates clean software architecture, DevOps best practices, and production-ready deployment techniques while serving as my personal portfolio website.

---

## 🎯 Objective

The goal of this project is to demonstrate modern backend engineering and cloud deployment practices through a production-ready Flask portfolio application. It showcases how a simple web application can be structured, tested, containerized, and prepared for cloud deployment using industry-standard tools.

---

## ✨ Features

- ✅ Flask Application Factory Pattern
- ✅ Modular routing using Blueprints
- ✅ Environment-based configuration with `.env`
- ✅ Structured application logging
- ✅ Health check endpoint (`/health`)
- ✅ Custom 404 and 500 error pages
- ✅ Automated testing with Pytest
- ✅ GitHub Actions Continuous Integration
- ✅ Docker containerization
- ✅ Gunicorn production server
- ✅ Responsive portfolio website

---

## 🏗️ Architecture

```
                   Browser
                      │
                      ▼
               Gunicorn Server
                      │
                      ▼
              Flask Application
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
   Blueprints                 Configuration
        │                           │
        └─────────────┬─────────────┘
                      ▼
        Templates + Static Assets
```

---

## 📂 Project Structure

```
gcp-flask-portfolio/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── routes.py
│   ├── static/
│   └── templates/
│
├── tests/
│   └── test_routes.py
│
├── logs/
│
├── .github/
│   └── workflows/
│       ├── docker.yml
│       └── python-ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── run.py
├── requirements.txt
├── cloudbuild.yaml
├── app.yaml
└── README.md
```

---

## 💡 Key Engineering Practices

- Clean project architecture using the Flask Application Factory Pattern
- Modular routing using Blueprints
- Environment-based configuration
- Structured application logging
- Health monitoring endpoint
- Automated testing with Pytest
- Continuous Integration using GitHub Actions
- Production deployment using Gunicorn
- Docker containerization

---

## 🛠️ Tech Stack

### Backend

- Python 3.13
- Flask
- Gunicorn

### Cloud & DevOps

- Docker
- GitHub Actions
- Google Cloud Platform
- Google Cloud Build

### Testing

- Pytest

### Frontend

- HTML5
- CSS3

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone git@github.com:sharmadivyam216-dot/gcp-flask-portfolio.git
cd gcp-flask-portfolio
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python run.py
```

Visit:

```
http://localhost:8080
```

---

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t flask-portfolio .
```

Run the container:

```bash
docker run -p 8080:8080 flask-portfolio
```

Open your browser:

```
http://localhost:8080
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## ❤️ Health Check

The application exposes a health endpoint:

```
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

---

## 🔄 Continuous Integration

GitHub Actions automatically performs the following tasks whenever code is pushed to the configured branches:

- Install project dependencies
- Run automated tests
- Validate the application

This helps ensure that new changes do not break existing functionality.

---

## ☁️ Deployment

This project is prepared for deployment using:

- Google Cloud App Engine
- Google Cloud Build
- Docker

> A live deployment link will be added after the portfolio UI redesign is completed.

---

## 📈 Future Improvements

- Modern portfolio UI redesign
- Dark mode support
- Contact form with backend integration
- Terraform infrastructure provisioning
- Kubernetes deployment
- Monitoring and observability
- HTTPS custom domain
- Production analytics dashboard

---

## 👨‍💻 Author

**Divyam Sharma**

GitHub: https://github.com/sharmadivyam216-dot

---

## 📄 License

This project is intended for learning, portfolio, and demonstration purposes.

---

## ⭐ Project Status

- ✅ Production-ready backend architecture
- ✅ Automated testing with Pytest
- ✅ GitHub Actions Continuous Integration
- ✅ Dockerized application
- ✅ Gunicorn production deployment
- 🚧 Frontend modernization in progress
- 🚀 Cloud deployment coming soon