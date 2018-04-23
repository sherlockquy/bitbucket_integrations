pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'if bash -c \'git log -1 --pretty=%B | grep "test fail"\'; then false; fi;'
      }
    }
  }
}