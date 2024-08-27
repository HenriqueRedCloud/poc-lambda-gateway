# AWS Lambda with API Gateway - PoC

This Proof of Concept (PoC) demonstrates how to set up an AWS Lambda function triggered by an API Gateway. The Lambda function processes HTTP GET requests and returns a personalized greeting message.

## Folder Structure

- **src/**: Contains the Lambda function code.
- **infrastructure/**: Contains the CloudFormation templates to deploy the AWS resources.
- **README.md**: Instructions on how to deploy and use the PoC.

## Prerequisites

1. **AWS CLI**: Ensure the AWS CLI is installed and configured with your credentials.
2. **AWS Account**: You need an AWS account with permissions to create Lambda, API Gateway, and S3 resources.

## Steps to Deploy

1. **Upload Lambda Code to S3**:
   - Zip the contents of the `src/` folder.
   - Upload the zip file to an S3 bucket.

   - ```zip -r lambda.zip src/```
   - ```aws s3 cp lambda.zip s3://your-s3-bucket/lambda.zip```

2. **Deploy CloudFormation Templates**:
    - Deploy API Gateway
    - ```aws cloudformation create-stack --stack-name apigateway-poc --template-body file://infrastructure/api_gateway.yml --capabilities CAPABILITY_IAM```

    - Deploy Lambda
    - ```aws cloudformation create-stack --stack-name lambda-poc --template-body file://infrastructure/lambda.yml --capabilities CAPABILITY_IAM```


2. **Test the Setup**:
    - ```curl https://<API-GATEWAY-ENDPOINT>/dev/hello?name=John```

## How It Works
1. Lambda Function: The Lambda function is triggered by an API Gateway GET request. It processes the request, logs the event, and returns a personalized greeting message.
2. API Gateway: The API Gateway acts as the entry point for HTTP requests and triggers the Lambda function.
3. CloudWatch: Logs the events and outputs from the Lambda function for monitoring and debugging.