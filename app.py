python -m ensurepip --default-pip
import boto3
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('public-resources.sandbox.vizuri.com')
for object in my_bucket.objects.all():
    print(object)
