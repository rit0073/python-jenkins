pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh "virtualenv -p /usr/bin/python3 venv"
        sh """
        . venv/bin/activate
        pip install -r requirements.txt
        """
      }
    }

    stage("run-test") {
      steps {
        sh "venv/bin/python -m pytest tests/test_main_prog.py"
      }
    }
  }
}
