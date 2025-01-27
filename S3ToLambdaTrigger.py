#https://github.com/manishkrishnvimal/notes/blob/master/S3ToLambda- link for guide

#Create one Lambda function and give AWS provided policy template with read access to S3.
#Create S3 bucket and in properties create event notification with Lambda function role which one was created in step1
#In S3 bucket, select event type of put and create object
#In Lambda use the below code, It will be triggered whenever a file will be uploaded to your S3 bucket

import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client("s3")
    bucketname = event["Records"][0]["s3"]["bucket"]["name"]
    bucketobject = event["Records"][0]["s3"]["object"]["key"]
    print('Hello from S3 ')
    print(bucketname)
    print(bucketobject)

    response = s3.get_object(Bucket=bucketname, Key=bucketobject)
    print(response)
    data = response["Body"].read()
    print(data)
    print(event)

    # By monitering cloudLogWatch we can see the information.
    # import json
    # import boto3
    #import json: For handling JSON data.
    #import boto3: AWS SDK for Python, used here to interact with Amazon S3.