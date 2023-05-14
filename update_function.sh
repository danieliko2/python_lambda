#!/bin/bash


echo "Package the dependencies"
pip install --target ./package -r requirements.txt
zip -r ./scripts/my-deployment-package.zip ./scripts/package

zip ./scripts/my-deployment-package.zip ./scripts/lambda_function.py

echo "Deploy the lambda function"
aws lambda update-function-code --function-name ex4 --zip-file fileb://./my-deployment-package.zip