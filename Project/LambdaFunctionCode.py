import json
import boto3
from urllib.parse import unquote_plus

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('S3FileMetadata')

def lambda_handler(event, context):
    try:
        # Get S3 bucket and object key from the event
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            object_key = unquote_plus(record['s3']['object']['key'])

            # Get metadata about the file
            s3_response = s3.head_object(Bucket=bucket_name, Key=object_key)
            file_size = s3_response['ContentLength']
            content_type = s3_response['ContentType']
            last_modified = s3_response['LastModified'].isoformat()
            e_tag = s3_response['ETag']
            storage_class = s3_response.get('StorageClass', 'STANDARD')
            owner = s3_response.get('Owner', {}).get('DisplayName', 'Unknown')
            
            # Prepare the item to be stored in DynamoDB
            item = {
                'fileName': object_key,
                'bucketName': bucket_name,
                'fileSize': file_size,
                'contentType': content_type,
                'lastModified': last_modified,
                'eTag': e_tag,
                'storageClass': storage_class,
                'owner': owner
            }

            # Store the item in DynamoDB
            table.put_item(Item=item)
            print(f'Successfully stored metadata for {object_key} in DynamoDB')

    except Exception as e:
        print(f'Error processing {object_key} from bucket {bucket_name}: {e}')
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
