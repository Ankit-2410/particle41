import json
from datetime import datetime

def handler(event, context):
    ip_address = event.get("requestContext", {}).get("http", {}).get("sourceIp", "Unknown")
    timestamp = datetime.utcnow().isoformat() + "Z"

    body = json.dumps({
        "timestamp": timestamp,
        "ip": ip_address
    })

    return {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": body
    }


