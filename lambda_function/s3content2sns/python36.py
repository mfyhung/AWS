import json
import boto3
import gzip
import base64
import os
import io

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    response = s3_client.list_objects(Bucket="codepipeline-ap-east-1-286823830082", Prefix="hpoanalysis-dev/")
    latest = (len(response['Contents']))
    key = str(response['Contents'][latest - 1]['Key'])
    print(key)
    log = s3_client.get_object(Bucket="codepipeline-ap-east-1-286823830082", Key=key)
    content = log['Body'].read()
    body = gzip.decompress(content)
    json_body = body.decode('utf8').replace("'", '"')
    print(json_body)
    #json_data = json.loads(json_body)
    #print(json_data)
    send_message(json_body)
    
def send_message(body):
    sns = sns_client.publish(
        TopicArn = 'arn:aws:sns:ap-east-1:244857349068:hpo-codebuild-notifications',
        Message = body,
        Subject = "Hpoanalysis-dev"
    )

