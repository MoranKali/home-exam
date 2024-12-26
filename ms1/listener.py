from flask import Flask, request, jsonify
import json
from marshmallow import Schema, fields, ValidationError, validate
import os
import logging
import boto3
# import new_producer
from botocore.exceptions import ClientError
#from flask_restful import Resource, Api

env_token = os.environ["secret_token"]
aws_access_key_id = os.environ["aws_access_key"]
aws_secret_access_key = os.environ["secret_access_key"]

logger = logging.getLogger(__name__)
sqs = boto3.resource("sqs", region_name="eu-north-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
queue = sqs.get_queue_by_name(QueueName="myQueue.fifo")
AWS_REGION = 'eu-north-1'
QUEUE_URL = 'https://sqs.eu-north-1.amazonaws.com/248189902862/myQueue.fifo'

sqs_client = boto3.client("sqs", region_name=AWS_REGION)

def send_queue_message(queue, message_body, message_attributes=None):
    """
    Send a message to an Amazon SQS queue.

    :param queue: The queue that receives the message.
    :param message_body: The body text of the message.
    :param message_attributes: Custom attributes of the message. These are key-value
                               pairs that can be whatever you want.
    :return: The response from SQS that contains the assigned message ID.
    """
    if not message_attributes:
        message_attributes = {}

    try:
        response = queue.send_message(
            MessageBody=message_body, MessageAttributes=message_attributes
        )
    except ClientError as error:
        logger.exception("Send message failed: %s", message_body)
        raise error
    else:
        return response



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
        # send to sqs
        try:
            schema.load(data)
        except ValidationError as err:
            return jsonify({"status": "error", "message": err.messages}), 400
        sqs_response=send_queue_message(queue,data_str=json.dumps(data), message_attributes=None)
        print(f"SQS Response: {sqs_response}")
        return jsonify({"status": "success", "data": data}), 200
    else:
        return jsonify({"status": "error", "message": "No payload received"}), 400

if __name__ == '__main__':
    payload=app.run(host='0.0.0.0', port=8080)
