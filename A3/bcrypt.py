import json
import bcrypt

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    value_to_hash = body.get('value', '')

    # Hashing with bcrypt
    salt = bcrypt.gensalt()  
    hashed_value = bcrypt.hashpw(value_to_hash.encode(), salt).decode()

    response = {
        "banner": "B00947641",
        "result": hashed_value,
        "arn": context.invoked_function_arn,  
        "action": "bcrypt",
        "value": value_to_hash
    }

    return response