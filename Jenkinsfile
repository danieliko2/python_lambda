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
                sh 'cd package && ls -la && echo did ls! && zip -r ../my-deployment-package.zip .'
                sh 'zip ./my-deployment-package.zip ./lambda_function.py'
                sh 'aws lambda update-function-code --function-name ex4 --zip-file fileb://my-deployment-package.zip'
                sh 'ls -la'

            }
        }
    }
}