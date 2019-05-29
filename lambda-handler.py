import json
import os

import boto3


def main(event, context):
    queue_url = os.environ.get('QUEUE_URL')

    sqs = boto3.client('sqs')
    queue_resp = sqs.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['All']
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(queue_resp['Attributes'])
    }
    return response
