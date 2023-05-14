pipeline {
    agent any

    stages {
        stage('test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('update jenkinsfile') {
            steps {
                sh 'echo "Package the dependencies"'
                sh 'pip install --target ./package -r requirements.txt'
                sh 'zip -r ./scripts/my-deployment-package.zip ./scripts/package'
                sh 'ls -la'
                // sh 'zip ./scripts/my-deployment-package.zip ./scripts/lambda_function.py'
            }
        }
    }
}