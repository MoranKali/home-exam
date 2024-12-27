import boto3
import os
import logging
import string
import random
import time

aws_access_key_id = os.environ["aws_access_key"]
aws_secret_access_key = os.environ["secret_access_key"]
sqs = boto3.resource("sqs", region_name="eu-north-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

s3 = boto3.resource('s3', region_name='eu-north-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
s3_client = boto3.client('s3', region_name='eu-north-1')
bucket_name = "248189902862-messages"

sqs_queue = sqs.get_queue_by_name(QueueName="StandardQueue")

logger = logging.getLogger(__name__)

# generate a random id for the message
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def process_message(message_body):
    print(f"processing message: {message_body}")
    # do what you want with the message here
    s3.Object(bucket_name, id_generator(6)).put(Body=message_body)
    logger.warning("Message processed: %s", message_body)

if __name__ == "__main__":
    while True:
        time.sleep(5)
        messages = sqs_queue.receive_messages()
        for message in messages:
            process_message(message.body)
            message.delete()