import json
import hashlib

def lambda_handler(event, context):
    body = event.get('body', '{}')
    value_to_hash = body.get('value', '')

    # Performing MD5 hashing
    hashed_value = hashlib.md5(value_to_hash.encode()).hexdigest()
    response = {
        "banner": "B00947641",
        "result": hashed_value,
        "arn": context.invoked_function_arn,  
        "action": "md5",
        "value": value_to_hash
    }
    return {
        "banner": "B00947641",
        "result": hashed_value,
        "arn": context.invoked_function_arn,  
        "action": "md5",
        "value": value_to_hash
    }
