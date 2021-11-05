pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo $BUILD_NUMBER'
        script {
          dockerImage = docker.build(REGISTRY_ACCOUNT + "/" + REGISTRY_REPOSITORY + ":$BUILD_NUMBER", "./scripts/weather")
        }
      }
    }
    stage('Push') {
      steps {
        script {
          docker.withRegistry('', REGISTRY_CREDS) {
            dockerImage.push()
          }
        }

      }
    }
    stage('Cleaning up') {
      steps {
        sh "docker rmi $REGISTRY_ACCOUNT/$REGISTRY_REPOSITORY:$BUILD_NUMBER"
      }
    }
  }
  environment {
    REGISTRY_ACCOUNT = 'itaybs'
    REGISTRY_REPOSITORY = 'weather-fetcher'
    REGISTRY_CREDS = 'itaybs-dockerhub'
    dockerImage = ''
  }
}