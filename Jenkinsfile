pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Code checked out'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage (Python project)'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment successful'
            }
        }
    }
}
