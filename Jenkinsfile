pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t my-flask-app .'
        sh 'docker tag my-flask-app $DOCKER_BFLASK_IMAGE'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run my-flask-app python -m pytest app/tests/'
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
          sh 'docker push $DOCKER_BFLASK_IMAGE'
        }
      }
    }
    stage('Stop Container') {
      steps {
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          sh 'docker stop python-poc || true'
          sh 'docker rm python-poc || true'
        }
      }
    }
    stage('Run') {
      steps {
        sh 'docker run -d --name python-poc -p 5000:5000 feitordaniel97/ci_cd_python'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}