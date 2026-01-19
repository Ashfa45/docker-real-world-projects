pipeline {
    agent any

    stages {
        stage('Build Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker-compose down || true
                docker-compose up -d
                '''
            }
        }
    }
}
