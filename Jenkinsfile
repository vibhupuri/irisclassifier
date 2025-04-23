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
stage('Login to Docker Hub') {
            steps {
                script {
     withCredentials([usernamePassword(credentialsId: '064e341d-3edf-4d73-8ab4-c98f7efa7a1e', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                }
              }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                def currentUser = sh(script: 'whoami', returnStdout: true).trim()
                    sh "docker push vibhupuri/iris-classifier:latest"
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
