pipeline{
    agent any
    stages{
        stage('checkout code'){
            steps{
                echo 'Checking out source code'
            }
        }
        stage('install dependencies'){
            steps{
                echo 'Installing dependencies'
            }
        }
        stage('run python script'){
            steps{
                echo 'Running Python script'
            }
        }
        stage('generate report'){
            steps{
                echo 'Generating report'
            }
        }
    }

    // Post actions to be executed after pipeline finishes
    post{
        success{
            echo 'Pipeline executed successfully!'
        }
        failure{
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}