pipeline {
    agent any

    environment {
        API_TOKEN = credentials('api_token')
    }

    stages {

        stage('Checkout code') {
            steps {
                echo 'Checking out source code'
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing dependencies'
            }
        }

        stage('Run Python script') {
            steps {
                bat '''
                    echo Running Python script with secure token
                    python api_caller.py
                '''
            }
        }

        stage('Generate report') {
            steps {
                bat '''
                    echo Generating report
                    python report_generator.py
                '''
            }
        }

        stage('Verify credentials usage') {
            steps {
                bat '''
                    echo Using API token securely (masked in logs)
                    echo %API_TOKEN%
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}