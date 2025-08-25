pipeline {
  agent any
  stages {
    stage('Checkout'){ steps{ checkout scm } }
    stage('Setup Python'){ steps{ sh "python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt" } }
    stage('Unit Tests'){ steps{ sh ". .venv/bin/activate && pytest -q" } }
  }
}
