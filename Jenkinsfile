pipeline {
    agent{
        dockerfile
        {
            filename 'Dockerfile'
            dir '.'
            additionalBuildArgs '--tag ef1120/temperatures'
            args '-p 9191:80'
        }
        
    }

    stages {
        stage('Build') {
            steps {                
                    echo 'Building de Docker image..'
                    // Here, Jenkins will build the image using the specified Dockerfile                
            }
        }

        stage('Execute APP')
        {
            steps{
                sh 'python /app/temperature.py'
            }
        }
       
    }

   post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline executed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
