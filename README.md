# Lambda with ApiGateway

This is a very simple example of using AWS CDK to define in Python 
([Python >= 3.7.1](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)) a Lambda function with APIGateway.
The function simply queries and SQS queue for its attributes when called.
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
Optionally you can view the resulting CloudFormation template with `cdk synth` and/or see what is going to be deployed by issuing `cdk diff`

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
