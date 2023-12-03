import boto3
import os

s3 = boto3.resource(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
    endpoint_url=os.getenv("S3_ENDPOINT_URL", ""),
)

def get_list_objects(bucket_name):
    bucket = s3.Bucket(bucket_name)
    return [obj.key for obj in bucket.objects.all()]


def get_list_buckets_with_prefix(prefix):
    array = []
    for bucket in s3.buckets.all():
        if bucket.name.startswith(prefix):
            array.append(bucket.name)
    return array


def get_object_by_key(bucket_name, key):
    obj = s3.Object(bucket_name, key)
    return obj.get()["Body"].read().decode("utf-8")