pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh './venv/Scripts/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/Scripts/pytest --html=reports/report.html --self-contained-html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
            }
        }
    }
}
