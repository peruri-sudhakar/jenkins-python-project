pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Code checked out'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-jenkins-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm python-jenkins-app'
            }
        }
    }
}
