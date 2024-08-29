pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'  //Dockerfile name
            dir '.'  // The directory where the Dockerfile is located
            additionalBuildArgs '--tag apasoft/temperatures'  // If necessary, additional build arguments can be passed
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