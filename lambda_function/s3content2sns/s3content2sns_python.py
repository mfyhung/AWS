import json
import boto3
import gzip
import base64
import urllib.parse
import os
import io

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name'] #Get the bucket info from the event
    print(bucket)
    key = event['Records'][0]['s3']['object']['key']
    log = s3_client.get_object(Bucket=bucket, Key=key)
    content = log['Body'].read()
    body = gzip.decompress(content) #Get the content from the gzip file
    json_body = body.decode('utf8').replace("'", '"') #Transfer the content to json format
    print(json_body)
    send_message(json_body)
    
def send_message(body):
    sns = sns_client.publish(
        TopicArn = 'arn:aws:sns:ap-east-1:244857349068:hpo-codebuild-notifications',
        Message = body,
        Subject = "Hpoanalysis-test"
    )
