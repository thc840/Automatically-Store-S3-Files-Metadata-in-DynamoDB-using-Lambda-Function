# Automatically-Store-S3-Files-Metadata-in-DynamoDB-using-Lambda-Function

This project automates capturing and storing metadata from files uploaded to Amazon S3 into an Amazon DynamoDB table using an event-driven AWS Lambda function in Python (boto3). It extracts object attributes—such as file name, bucket, size, content type, timestamp, ETag, storage class, and owner—via IAM-secured access, logs execution in CloudWatch, and provides real-time, serverless scalability while trading off cold starts, service limits, and vendor lock-in. 

## Workflow

1. A user uploads a file to an Amazon S3 bucket.
2. The S3 object-created event triggers the AWS Lambda function.
3. Lambda reads the uploaded file's metadata and stores it in Amazon DynamoDB.

The project uses Amazon S3, AWS Lambda, Amazon DynamoDB, and IAM. The Lambda function is written in Python with boto3.

## Setup

1. Create an S3 bucket.
2. Create a DynamoDB table with a String partition key named `fileName`.
3. Create an IAM role for Lambda and attach `AmazonS3ReadOnlyAccess` and `AmazonDynamoDBFullAccess`. `AmazonCloudWatchFullAccess` is listed as optional.
4. Create a Lambda function using Python 3.9 and assign the IAM role.
5. Add the S3 bucket as a Lambda trigger and select **All object create events**.
6. Add the Python function from [`Project/LambdaFunctionCode.py`](Project/LambdaFunctionCode.py) to Lambda.

The function writes to a DynamoDB table named `S3FileMetadata`. Use that name for the table referenced by the function.

## Metadata stored

The function writes the object key (`fileName`), bucket name, file size, content type, last-modified time, ETag, storage class, and owner to DynamoDB.

## Test

Upload a file to the S3 bucket. Check the Lambda execution and log messages in CloudWatch, then open the DynamoDB table and verify that the file metadata was stored.

