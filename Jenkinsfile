pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master',
                url: 'https://github.com/Ashfa45/docker-real-world-projects.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
