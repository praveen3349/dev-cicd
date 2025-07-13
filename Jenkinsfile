pipeline {
    agent any

    stages {
        // Stage 1: Clone Code
        stage('Clone Repository') {
            steps {
                git 'https://github.com/praveen3349/dev-cicd'
            }
        }

        // Stage 2: Run Tests
        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        // Stage 3: Build Docker Image
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        // Stage 4: Deploy (On Same EC2)
        stage('Deploy') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d --name flask-app -p 5000:5000 flask-app
                '''
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed! Check logs."
        }
    }
}
