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
                sh 'docker-compose up -d'
            }
        }
        stage('Docker Push') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                sh "docker tag calculator2_app thugrock/calculator"
                sh 'docker push thugrock/calculator'
                }
            }
        }
    }
}
