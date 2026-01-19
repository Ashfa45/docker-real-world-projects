stage('Deploy Application') {
    steps {
        sh '''
        docker-compose down || true
        docker-compose up -d
        '''
    }
}
