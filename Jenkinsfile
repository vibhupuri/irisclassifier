pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vibhupuri/iris-classifier:latest'
    }

    stages {
        stage('Print Current User') {
            steps {
                script {
                    def currentUser = sh(script: 'whoami', returnStdout: true).trim()
                    echo "Running as user: ${currentUser}"
                }
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${env.IMAGE_NAME} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                def currentUser = sh(script: 'whoami', returnStdout: true).trim()
                iris-classifier:latest
                    sh "docker push ${currentUser}/iris-classifier:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${env.IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}
