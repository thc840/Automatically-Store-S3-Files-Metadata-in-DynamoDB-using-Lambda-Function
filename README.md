# Automatically-Store-S3-Files-Metadata-in-DynamoDB-using-Lambda-Function

This project automates capturing and storing metadata from files uploaded to Amazon S3 into an Amazon DynamoDB table using an event-driven AWS Lambda function in Python (boto3). It extracts object attributes—such as file name, bucket, size, content type, timestamp, ETag, storage class, and owner—via IAM-secured access, logs execution in CloudWatch, and provides real-time, serverless scalability while trading off cold starts, service limits, and vendor lock-in. 

