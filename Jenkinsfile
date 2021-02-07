pipeline {
  agent any
  stages {
    stage("run-test") {
      steps {
        python -m pytest tests/test_main_prog.py
      }
    }
  }
}
