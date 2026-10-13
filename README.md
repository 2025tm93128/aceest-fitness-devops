# ACEest Fitness & Gym DevOps Project
## Project Overview
ACEest Fitness & Gym is a Flask-based REST API created for the Introduction to DevOps assignment. The project demonstrates source-code management, automated testing, containerization, continuous integration with GitHub Actions, and build automation through Jenkins.

## Features
- Application health check
- View available fitness programs
- View registered clients
- Register a client for a fitness program
- Estimate calories burned based on weight, workout duration, and intensity
- Automated testing with Pytest
- Docker containerization
- GitHub Actions continuous integration
- Jenkins build pipeline

## Project Structure
```text
aceest-fitness-devops/
├── .github/
│   └── workflows/
│       └── main.yml
├── tests/
│   └── test_app.py
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── Jenkinsfile
├── README.md
└── requirements.txt
```

## Prerequisites
- Python 3.12 or later
- Git
- Docker
- Jenkins with Git, Pipeline, and Workspace Cleanup plugins

## Local Setup
Clone the repository and enter the project directory:

git clone <repository-url>
cd aceest-fitness-devops

Create and activate a virtual environment.

## Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

## Linux
python3 -m venv .venv
source .venv/bin/activate

Install the project dependencies:

python -m pip install -r requirements.txt

## Run the Flask Application
python app.py

Open the application in a browser at:
http://127.0.0.1:5000

## API Endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Display application information |
| GET | `/health` | Return application health status |
| GET | `/programs` | List available fitness programs |
| GET | `/clients` | List registered clients |
| POST | `/clients` | Register a client |
| POST | `/calories` | Estimate calories burned |

## Automated Testing
Run all tests with:

python -m pytest -v

The project contains eight tests covering application endpoints, successful requests, and validation failures.

## Docker
Build the Docker image:

docker build -t aceest-fitness-app:latest .

Run the Docker container:

docker run --rm -p 5000:5000 aceest-fitness-app:latest

## GitHub Actions
The workflow is defined in .github/workflows/main.yml. It runs automatically for pushes and pull requests targeting the main branch.

The workflow performs:

1. Source-code checkout
2. Python setup
3. Dependency installation
4. Python syntax validation
5. Pytest execution
6. Docker-image build

## Jenkins Pipeline
The Jenkins pipeline is defined in Jenkinsfile. It performs:

1. Source-code checkout
2. Python virtual-environment setup
3. Dependency installation
4. Python syntax validation
5. Pytest execution
6. Docker-image build
7. Workspace cleanup

## Author
**Nisha Ray**  
Introduction to DevOps Assignment, 2026