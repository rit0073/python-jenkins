pipeline {
  agent any
  stages {
    stage("run-test") {
      steps {
        sh "python -m pytest tests/test_main_prog.py"
      }
    }
  }
}
