pipeline {
    agent any  // Runs on any available Jenkins agent 

    environment {
        VENV = "${WORKSPACE}/venv"  // Define virtual environment path
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/PasupathiG03/taskapi-backend.git'
            }
        }

        stage('Setup Python') {
            steps {
                echo "Setting up virtual environment..."
                sh 'python3 -m venv $VENV'
                sh '. $VENV/bin/activate && pip install --upgrade pip'
                sh '. $VENV/bin/activate && pip install -r backend/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running Django tests..."
                sh '. $VENV/bin/activate && python backend/manage.py test tasks'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "All tests passed ✅"
        }
        failure {
            echo "Some tests failed ❌"
        }
    }
}
