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

    }
}
