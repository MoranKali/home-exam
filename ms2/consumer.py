import boto3
import os
import logging

aws_access_key_id = os.environ["aws_access_key"]
aws_secret_access_key = os.environ["secret_access_key"]
sqs = boto3.resource("sqs", region_name="eu-north-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

sqs_queue = sqs.get_queue_by_name(QueueName="StandardQueue")

logger = logging.getLogger(__name__)

def process_message(message_body):
    print(f"processing message: {message_body}")
    # do what you want with the message here
    logger.info("Message processed: %s", message_body)
    pass

if __name__ == "__main__":
    while True:
        messages = sqs_queue.receive_messages()
        for message in messages:
            process_message(message.body)
            # message.delete()