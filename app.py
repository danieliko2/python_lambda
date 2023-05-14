from flask import Flask, render_template, request
import boto3, json

lambda_client = boto3.client('lambda')

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('base.html')

@app.route('/ex', methods=['POST'])
def ex():
    test_event = {"key1": request.form['my_input']}
    try:
        response = lambda_client.invoke(
            FunctionName='ex4',
            Payload=json.dumps(test_event),
        )
        print(response['Payload'])
        return_value=response['Payload'].read().decode("utf-8")
        return_value=json.loads(return_value)

        print(return_value['body'])
        return return_value["body"]
    except:
        print("Failiure")
        return "Failure"

if __name__ == "__main__":
    app.run()