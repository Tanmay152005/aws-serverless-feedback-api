# AWS Serverless Feedback API 

A production-ready serverless backend built using AWS Lambda, API Gateway(HTTP API), DynamoDB.

## Features
- Submits Feedback using POST API 
- Retrieves stored Feedback using GET API
- Fully Serverless and Scalable 
- Tested using browser and command line(curl)

## Tech Stack 
- AWS Lambda (Python)
- API Gateway (HTTP API)
- DynamoDB
- AWS IAM 

## API Endpoints

### POST /feedback

Example:
```bash 
curl -X POST http://<api-id>.execute-api.<region>.amazonaws.com/prod/feedback \
-H "Content-Type: application/json" \
-d '{"user":"tanmay","feedback":"Great service"}'
```

### GET /feedback
Retrieves all stored feedback
```bash
curl https://<api-id>.execute-api.<region>.amazonaws.com/prod/feedback
```
## ARCHITECTURE
Client -> API Gateway -> AWS Lambda -> DynamoDB

## Future Improvements 
- Authentication (JWT/IAM)
- Pagination for GET API
- Filtering and sorting feedback
