import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket name and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    # Define the destination bucket and folder
    destination_bucket = source_bucket
    destination_key = "uppercase-folder/" + source_key.split('/')[-1]
    
    # Read the file from the source bucket
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    content = response['Body'].read().decode('utf-8')
    
    # Convert content to uppercase
    uppercase_content = content.upper()
    
    # Upload the modified file to the destination folder
    s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=uppercase_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'File {source_key} processed and uploaded to {destination_key}')
    }
