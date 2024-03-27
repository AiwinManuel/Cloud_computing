import json
import requests

def lambda_handler(event, context):
    json_response = event
    

    post_url = "http://129.173.67.184:6000/end"

    try:
        post_response = requests.post(post_url, json=json_response)
        return post_response.text  
    except requests.RequestException as e:
        return json.dumps({"message": "Error in sending POST request", "error": str(e)})
