pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh "pip install -r requirements.txt"
      }
    }

    stage("run-test") {
      steps {
        sh "python -m pytest tests/test_main_prog.py"
      }
    }
  }
}
