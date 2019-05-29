import json
import boto3
import os

def main(event, context):
    queue_url = os.environ.get('QUEUE_URL')
    # const sqs = new SQS();
    # const response = await sqs.getQueueAttributes({
    #     QueueUrl: process.env.QUEUE_URL,
    #     AttributeNames: ['All']
    # }).promise();
    #
    # return {
    #     statusCode: 200,
    #     body: JSON.stringify(response.Attributes, undefined, 2),
    #     headers: {
    #         'content-type': 'application/json'
    #     }
    # };
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
