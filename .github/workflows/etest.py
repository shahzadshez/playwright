import boto3

s3 = boto3.client('s3',region='us-east-1')
s3.upload_file('test.txt', 'my-bucket', 'uploaded_file_name_test.txt')

dynamodb =s3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('my-table')

