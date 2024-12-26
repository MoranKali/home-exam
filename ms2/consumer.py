import boto3
import os

aws_access_key_id = os.environ["aws_access_key"]
aws_secret_access_key = os.environ["secret_access_key"]
sqs = boto3.resource("sqs", region_name="eu-north-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

queue = sqs.get_queue_by_name(QueueName="your-queue-name")

def process_message(message_body):
    print(f"processing message: {sqs_message}")
    # do what you want with the message here
    pass

if __name__ == "__main__":
    while True:
        messages = sqs_queue.receive_messages()
        for message in messages:
            process_message(message.body)
            message.delete()