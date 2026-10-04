# DevOps CI/CD Pipeline

A complete CI/CD pipeline demonstration using GitHub Actions, Docker, and FastAPI. This project showcases modern DevOps practices including automated testing, security scanning, containerization, and deployment automation.

![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-blue)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [CI/CD Pipeline](#cicd-pipeline)
- [GitHub Actions Workflows](#github-actions-workflows)
- [Security](#security)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)

## 🎯 Overview

This project demonstrates a complete CI/CD pipeline for a FastAPI application, showcasing:

- **Continuous Integration**: Automated linting, testing, and security scanning
- **Continuous Deployment**: Automated building, pushing, and deployment of Docker images
- **Best Practices**: Containerization, health checks, multi-environment support
- **Security**: Vulnerability scanning with Trivy
- **Monitoring**: Code coverage reporting with Codecov

## ✨ Features

### CI Pipeline Features
- ✅ Automated linting with flake8
- ✅ Unit testing with pytest
- ✅ Code coverage reporting
- ✅ Docker image building
- ✅ Security vulnerability scanning
- ✅ Multi-stage pipeline execution

### CD Pipeline Features
- ✅ Automated Docker image building and pushing
- ✅ Multi-environment deployment (staging → production)
- ✅ Environment-specific configurations
- ✅ Health checks after deployment
- ✅ Deployment notifications

### Application Features
- ✅ RESTful API with FastAPI
- ✅ CRUD operations
- ✅ Pydantic data validation
- ✅ Automatic API documentation
- ✅ Health check endpoints

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      GitHub Repository                        │
│                                                               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  Push/PR     │───>│  CI Pipeline │───>│  CD Pipeline │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│                            │                   │             │
│                            ▼                   ▼             │
│                    ┌──────────────┐    ┌──────────────┐   │
│                    │  Docker Hub  │    │  Staging     │   │
│                    └──────────────┘    └──────────────┘   │
│                                                  │           │
│                                                  ▼           │
│                                          ┌──────────────┐  │
│                                          │ Production   │  │
│                                          └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Application
- **Python 3.11**: Runtime environment
- **FastAPI 0.104**: Modern web framework
- **Pydantic 2.5**: Data validation
- **Uvicorn**: ASGI server

### CI/CD
- **GitHub Actions**: CI/CD automation
- **Docker**: Containerization
- **Docker Compose**: Local development
- **Trivy**: Security scanning
- **Codecov**: Code coverage

### Testing
- **pytest**: Testing framework
- **httpx**: HTTP client for testing
- **flake8**: Code linting

## 📦 Prerequisites

### Local Development
- **Python 3.11+**
- **Docker 20.10+**
- **Docker Compose 2.0+**
- **Git**

### For CI/CD Deployment
- **GitHub account**
- **Docker Hub account**
- **GitHub Secrets configured**:
  - `DOCKER_USERNAME`
  - `DOCKER_PASSWORD`

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/qqqqqwwerty/ci-cd-pipeline.git
cd ci-cd-pipeline
```

### 2. Local Development with Docker Compose

```bash
# Start the application
docker-compose up api

# Run tests
docker-compose up api-test
```

### 3. Local Development with Python

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload

# Run tests
pytest tests/ -v
```

### 4. Access the API

- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🔄 CI/CD Pipeline

### CI Pipeline (`.github/workflows/ci.yml`)

Triggers on:
- Push to `main` or `develop` branches
- Pull requests to `main`

Stages:
1. **Lint**: Code quality checks with flake8
2. **Test**: Unit tests with pytest and coverage reporting
3. **Build**: Docker image building and testing
4. **Security**: Vulnerability scanning with Trivy

### CD Pipeline (`.github/workflows/cd.yml`)

Triggers on:
- Push to `main` branch
- Manual workflow dispatch

Stages:
1. **Build & Push**: Build and push Docker image to Docker Hub
2. **Deploy Staging**: Deploy to staging environment
3. **Deploy Production**: Deploy to production environment

## 🔧 GitHub Actions Workflows

### CI Workflow

```yaml
Jobs:
  - lint: Code quality checks
  - test: Unit tests and coverage
  - build: Docker image building
  - security: Vulnerability scanning
```

### CD Workflow

```yaml
Jobs:
  - build-and-push: Build and push to Docker Hub
  - deploy-staging: Deploy to staging
  - deploy-production: Deploy to production
```

## 🔒 Security

### Security Features

- **Vulnerability Scanning**: Trivy scans for security vulnerabilities
- **Non-root User**: Docker container runs as non-root user
- **Health Checks**: Application health monitoring
- **Secrets Management**: GitHub Secrets for sensitive data
- **Code Quality**: Automated linting to catch issues early

### Security Best Practices

- Minimal Docker base image (python:3.11-slim)
- Dependency pinning in requirements.txt
- Security scanning before deployment
- Environment separation (staging/production)

## 🧪 Testing

### Running Tests Locally

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test
pytest tests/test_main.py::test_read_root
```

### Test Coverage

- Unit tests for all API endpoints
- Integration tests for CRUD operations
- Error handling tests
- Health check tests

## 🚀 Deployment

### Manual Deployment

```bash
# Build Docker image
docker build -t devops-api:latest .

# Run container
docker run -d -p 8000:8000 devops-api:latest
```

### Automated Deployment

The CD pipeline automatically:
1. Builds Docker image on push to main
2. Pushes image to Docker Hub
3. Deploys to staging environment
4. Runs health checks
5. Deploys to production (if staging passes)

### Configuration

Add these secrets to your GitHub repository:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password/access token

## 📊 Monitoring

### Health Check Endpoint

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy"
}
```

### API Documentation

Automatic interactive API documentation available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**qqqqqwwerty** - Junior DevOps Engineer

---

**Note**: This is a demonstration project for educational purposes. Always review and customize the pipeline for your specific requirements before deploying to production.
