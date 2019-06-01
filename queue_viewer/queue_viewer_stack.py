from aws_cdk import cdk, aws_sqs

from queue_viewer.queue_viewer_construct import QueueViewerConstruct


class QueueViewerStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)
        # Create the SQS queue
        queue_one = aws_sqs.Queue(self, 'SimpleQueueOne')
        queue_two = aws_sqs.Queue(self, 'SimpleQueueTwo')
        # QueueViewerConstruct will wrap the queue in an ApiGateway/Lambda.  The APIGateway
        # exposes an endpoint that returns the queue attributes
        queue_one_viewer = QueueViewerConstruct(self, 'QueueViewerOne', queue_one)
        queue_two_viewer = QueueViewerConstruct(self, 'QueueViewerTwo', queue_two)
        cdk.CfnOutput(
            self, "QueueOneEndpointUrl",
            value=queue_one_viewer.endpoint_url()
        )
        cdk.CfnOutput(
            self, "QueueTwoEndpointUrl",
            value=queue_two_viewer.endpoint_url()
        )
