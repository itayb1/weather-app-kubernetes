pipeline {
  agent any
  environment {
    REGISTRY_ACCOUNT = "itaybs"
    REGISTRY_REPOSITORY = "weather-fetcher"
    dockerImage = ''
  }
  stages {
    stage('Build') {
      steps {
        sh 'echo $BUILD_NUMBER'
        script {
          dockerImage = docker.build REGISTRY_ACCOUNT + "/" + REGISTRY_REPOSITORY + ":$BUILD_NUMBER"
        }
    }
    stage('Push') {
      steps {
        script {
          docker.withRegistry('', itaybs-dockerhub) {
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
}