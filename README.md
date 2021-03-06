# Lambda with ApiGateway via AWS CDK

This is a very simple example of using AWS CDK to define in Python 
([Python >= 3.7.1](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)) a Lambda function with APIGateway.
The function simply queries and SQS queue for the queue's attributes when called.

In this example we encapsulate the Lambda and APIGateway as a CDK [Construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html).  You simply instantiate the Construct, pass in an SQS que and it supplies an API Endpoint that returns the attributes of the queue when called.

```python
queue = aws_sqs.Queue(self, 'SimpleQueueOne')
queue_viewer = QueueViewerConstruct(self, 'QueueViewerOne', queue)
cdk.CfnOutput(
  self, "QueueOneEndpointUrl",
  value=queue_viewer.endpoint_url()
)
```

## Installing the CDK CLI

```bash
npm install -g aws-cdk

cdk --version
```
You will also need your AWS CLI configured (`~/.aws/config`)
See [docs](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) for details.

## Deploying this App Stack

Git clone then `cd` into the top directory of this project

Create your python virtual env
```bash
python -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt

```
Optionally you can view the resulting CloudFormation template with `cdk synth`.

When you are ready to deploy;
```bash
cdk deploy
```

If you then log into the console you will see a CloudFormation template comprising the build of your Lambda function, DynamoDb table
and associated resources.

# Cleaning up
```bash
cdk destroy
```