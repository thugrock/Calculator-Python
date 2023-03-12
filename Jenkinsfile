pipeline {
    agent any

    stages {
        stage('Clone git') {
            steps {
                git "https://github.com/thugrock/Calculator-Python.git"
            }
        }
        stage('Build Code') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build docker image'){
            agent any
            steps{
                sh 'apt-get install docker-compose'
                sh 'apt-get install docker.io'
                sh 'docker-compose up -d'
            }
        }
    }
}
