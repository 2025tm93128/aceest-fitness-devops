# ACEest Fitness & Gym - DevOps Assignment 2

This repository implements a complete CI/CD workflow for the ACEest Fitness & Gym Flask API.
It continues the Assignment 1 codebase and preserves the professor-supplied application versions under `versions/supplied-originals/`.

## Application

Version `2.0.0` provides health, readiness, version, programs, clients, calorie estimation, progress, workouts, and body-metric endpoints.

## Validation

- 20 automated Pytest tests
- 86% application code coverage
- Python syntax validation
- GitHub Actions test and Docker build workflow
- Jenkins pipeline with SonarQube, Docker build/test/push, and Kubernetes deployment stages

## Git workflow

- Baseline tag: `assignment-1-final`
- Assignment 2 feature branch: `feature/assignment-2-cicd`
- Release tag: `assignment-2-v2.0.0`
- Assignment 2 changes merged to `main` through Pull Request #1

## Container registry

Public Docker Hub repository:

`2025tm93128/aceest-fitness-devops`

Planned image tags:

- `v1.0.0`
- `v2.0.0`
- `latest`

## Local testing

```bash
python -m pip install -r requirements.txt
python -m py_compile app.py
python -m pytest -q --cov=app --cov-report=term
```

## Docker

```bash
docker build -t 2025tm93128/aceest-fitness-devops:v2.0.0 .
docker run --rm 2025tm93128/aceest-fitness-devops:v2.0.0 python -m pytest -q
docker run -d --name aceest-fitness -p 5000:5000 2025tm93128/aceest-fitness-devops:v2.0.0
```

Health endpoints:

- `GET /health`
- `GET /ready`
- `GET /version`

## CI/CD flow

1. GitHub Actions validates syntax, runs Pytest with coverage, builds the Docker image, and runs tests inside the image.
2. Jenkins checks out the repository, creates a Python environment, runs tests and coverage, performs SonarQube analysis and quality-gate validation, builds and tests the Docker image, pushes versioned images to Docker Hub, and deploys to Kubernetes.
3. SonarQube configuration is stored in `sonar-project.properties`.

## Kubernetes deployment strategies

The `kubernetes/` folder contains manifests for:

- Rolling update and rollback: `base.yaml`
- Blue-Green: `blue-green.yaml`
- Canary: `canary.yaml`
- Shadow: `shadow.yaml`
- A/B testing: `ab-testing.yaml`

Runtime evidence for Docker, Jenkins, SonarQube, Kubernetes, rollout, rollback, and deployment strategies is captured in Prayogshala.
