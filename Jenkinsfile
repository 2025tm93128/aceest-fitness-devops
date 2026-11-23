pipeline {
    agent any
    environment {
        IMAGE_NAME = 'aceest-fitness'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Set Up Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Validate and Test') {
            steps {
                sh '.venv/bin/python -m py_compile app.py'
                sh '.venv/bin/python -m pytest -q --cov=app --cov-report=term --cov-report=xml'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage('Build and Test Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} python -m pytest -q'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
            cleanWs()
        }
        success { echo 'ACEest Assignment 2 pipeline completed successfully.' }
        failure { echo 'Pipeline failed. Review the failed stage.' }
    }
}
