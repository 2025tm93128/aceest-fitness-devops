pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Validate Python Syntax') {
            steps {
                sh '.venv/bin/python -m py_compile app.py'
            }
        }

        stage('Run Pytest Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness-app:latest .'
            }
        }
    }

    post {
        success {
            echo 'ACEest Fitness pipeline completed successfully.'
        }
        failure {
            echo 'ACEest Fitness pipeline failed. Review the stage logs.'
        }
        always {
            cleanWs()
        }
    }
}
