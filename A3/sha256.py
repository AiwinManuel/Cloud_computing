import json
import hashlib

def lambda_handler(event, context):
    # Extracting values from the JSON input
    body = event.get('body', {})
    value_to_hash = body.get('value', '')
    # Performing SHA-256 hashing
    hashed_value = hashlib.sha256(value_to_hash.encode()).hexdigest()

    return {
        "banner": "B00947641",  
        "result": hashed_value,
        "arn": context.invoked_function_arn,  
        "action": "sha256",
        "value": value_to_hash
    }

