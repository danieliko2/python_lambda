from flask import Flask, render_template, request
import boto3, json


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")