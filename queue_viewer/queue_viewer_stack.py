from aws_cdk import aws_lambda as lambda_, cdk, aws_apigateway, aws_sqs, aws_iam
from aws_cdk.aws_iam import PolicyStatement


class QueueViewerStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        # Create the SQS queue
        queue = aws_sqs.Queue(self, 'SimpleQueue')

        # Create our Lambda function
        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()
        lambda_fn = lambda_.Function(
            self,
            "QueueViewer",
            code=lambda_.InlineCode(handler_code),
            handler="index.main",
            timeout=300,
            runtime=lambda_.Runtime.PYTHON37,
            environment={'QUEUE_URL': queue.queue_url},
        )
        lambda_fn.add_to_role_policy(PolicyStatement().add_action('sqs:*').add_resource(queue.queue_arn))
        # Now create our API for the Lambda function
        api = aws_apigateway.LambdaRestApi(
            self,
            'QueueViewerApi',
            handler=lambda_fn,
            proxy=False
        )
        queue_status = api.root.add_resource('status')
        queue_status.add_method('GET')



