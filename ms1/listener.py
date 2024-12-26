from flask import Flask, request, jsonify
#from json import dumps, loads
from marshmallow import Schema, fields, ValidationError, validate
import os
import boto3
import producer
#from flask_restful import Resource, Api

AWS_REGION = 'eu-north-1'
QUEUE_URL = 'https://sqs.eu-north-1.amazonaws.com/248189902862/myQueue.fifo'

sqs_client = boto3.client("sqs", region_name=AWS_REGION)

env_token = os.environ["secret_token"]

class DataSchema(Schema):
    email_subject = fields.String(required=True)
    email_sender = fields.String(required=True)
    email_timestream = fields.String(required=True)
    email_content = fields.String(required=True)

class PayloadSchema(Schema):
    data = fields.Nested(DataSchema, required=True)
    token = fields.String(validate=validate.Equal(env_token,error='Incorrect Token'), required=True)
    
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/payload', methods=['POST'])
def get_payload():
    data = request.get_json()
    schema=PayloadSchema()
    if data:
        # add tests and send to sqs
        try:
            schema.load(QUEUE_URL,data)
        except ValidationError as err:
            return jsonify({"status": "error", "message": err.messages}), 400
        producer.send_queue_message(data)
        return jsonify({"status": "success", "data": data}), 200
    else:
        return jsonify({"status": "error", "message": "No payload received"}), 400

if __name__ == '__main__':
    payload=app.run(host='0.0.0.0', port=8080)
