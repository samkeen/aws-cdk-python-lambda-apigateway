from aws_cdk import cdk, aws_apigateway
from aws_cdk.aws_iam import PolicyStatement
from aws_cdk.aws_sqs import Queue
from aws_cdk.aws_lambda import Function, InlineCode, Runtime


class QueueViewerConstruct(cdk.Construct):

    def __init__(self, app: cdk.App, id: str, queue: Queue) -> None:
        super().__init__(app, id)

        # Create our Lambda function
        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()
        lambda_fn = Function(
            self,
            "QueueViewer",
            code=InlineCode(handler_code),
            handler="index.main",
            timeout=300,
            runtime=Runtime.PYTHON37,
            environment={'QUEUE_URL': queue.queue_url},
        )
        lambda_fn.add_to_role_policy(PolicyStatement().add_action('sqs:*').add_resource(queue.queue_arn))
        # Now create our API for the Lambda function
        self.api = aws_apigateway.LambdaRestApi(
            self,
            'QueueViewerApi',
            handler=lambda_fn,
            proxy=False
        )
        queue_status = self.api.root.add_resource('attributes')
        queue_status.add_method('GET')

    def endpoint_url(self):
        return self.api.url_for_path('/attributes')
