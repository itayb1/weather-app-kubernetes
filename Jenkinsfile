pipeline {
  agent any
  stages {
    stage('Build Dockerfile') {
      steps {
        sh 'hostname'
        echo 'Building ${APP_NAME}'
        sh 'docker build ./scripts/weather --tag "${APP_NAME}:latest"'
      }
    }

    stage('Tag & Push') {
      steps {
        sh '''REMOTE_IMAGE="itaybs/${APP_NAME}:latest"
docker image tag "${APP_NAME}:latest" $REMOTE_IMAGE && docker image push $REMOTE_IMAGE'''
      }
    }

  }
  environment {
    APP_NAME = 'weather-fetcher'
  }
}