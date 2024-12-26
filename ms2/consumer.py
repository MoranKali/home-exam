import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
aws_access_key_id = os.environ["aws_access_key"]
aws_secret_access_key = os.environ["secret_access_key"]
sqs = boto3.resource("sqs", region_name="eu-north-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
queue = sqs.get_queue_by_name(QueueName="StandardQueue")

s3 = boto3.resource('s3', region_name='eu-north-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
s3_client = boto3.client('s3', region_name='eu-north-1')
bucket_name = "248189902862-messages"

def receive_messages(queue, max_number, wait_time):
    """
    Receive a batch of messages in a single request from an SQS queue.

    :param queue: The queue from which to receive messages.
    :param max_number: The maximum number of messages to receive. The actual number
                       of messages received might be less.
    :param wait_time: The maximum time to wait (in seconds) before returning. When
                      this number is greater than zero, long polling is used. This
                      can result in reduced costs and fewer false empty responses.
    :return: The list of Message objects received. These each contain the body
             of the message and metadata and custom attributes.
    """
    try:
        messages = queue.receive_messages(
            MessageAttributeNames=["All"],
            MaxNumberOfMessages=max_number,
            WaitTimeSeconds=wait_time,
        )
        for msg in messages:
            logger.info("Received message: %s: %s", msg.message_id, msg.body)
    except ClientError as error:
        logger.exception("Couldn't receive messages from queue: %s", queue)
        raise error
    else:
        return messages

def delete_message(message):
    """
    Delete a message from a queue. Clients must delete messages after they
    are received and processed to remove them from the queue.

    :param message: The message to delete. The message's queue URL is contained in
                    the message's metadata.
    :return: None
    """
    try:
        message.delete()
        logger.info("Deleted message: %s", message.message_id)
    except ClientError as error:
        logger.exception("Couldn't delete message: %s", message.message_id)
        raise error

if __name__ == '__main__':
    messages = receive_messages(queue, 10, 20)
    for msg in messages:
        s3.Object(bucket_name, msg.message_id).put(Body=msg.body)
        delete_message(msg)
