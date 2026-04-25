#Runtime: Python 3.13
#Upgraded from Python 3.10 to Python 3.13 on April 26 
#Tested via Postman and verified in DynamoDb
import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("FeedbackTable")

def lambda_handler(event, context):
    try:
        # 🔹 Detect HTTP method (for API Gateway HTTP API)
        http_method = event.get("requestContext", {}) \
            .get("http", {}) \
            .get("method")

        # =========================
        # ✅ HANDLE GET /feedback
        # =========================
        if http_method == "GET":
            response = table.scan()

            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(response.get("Items", []))
            }

        # =========================
        # ✅ HANDLE POST /feedback
        # =========================
        body = json.loads(event.get("body", "{}"))

        feedback_text = body.get("feedback")
        user_name = body.get("user", "anonymous")

        if not feedback_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Feedback is required"})
            }

        item = {
            "feedbackId": str(uuid.uuid4()),
            "feedback": feedback_text,
            "user": user_name,
            "createdAt": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Feedback submitted successfully",
                "feedbackId": item["feedbackId"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
