pipeline {
    agent any

    stages {
        stage('test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest'
            }
        }
        stage('update jenkinsfile') {
            steps {
                sh 'echo "Package the dependencies"'
                sh 'pip install --target ./package -r requirements.txt'
                sh 'zip -r ./my-deployment-package.zip ./package/*'
                sh 'zip ./my-deployment-package.zip ./lambda_function.py'
                sh 'ls -la'
                // sh 'zip ./scripts/my-deployment-package.zip ./scripts/lambda_function.py'
            }
        }
    }
}