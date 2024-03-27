import json
import boto3
from datetime import datetime

def default_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def lambda_handler(event, context):
    state_machine_arn = "arn:aws:states:us-east-1:339713063445:stateMachine:A3"
    step_function_input = event.get("input", {})

    if not state_machine_arn or not step_function_input:
        return {
            'statusCode': 400,
            'body': json.dumps({"message": "Missing state machine ARN or input"})
        }

    sfn_client = boto3.client('stepfunctions')

    try:
        response = sfn_client.start_execution(
            stateMachineArn=state_machine_arn,
            input=json.dumps(step_function_input)
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response, default=default_serializer)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "Error in starting Step Function", "error": str(e)}, default=default_serializer)
        }
