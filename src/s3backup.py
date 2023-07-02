import boto3
from os import getenv


def upload_objects(objects: list[str]) -> None:
    session = boto3.Session(
        aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    )
    s3 = session.resource(
        service_name="s3", endpoint_url=getenv("S3_ENDPOINT_URL")
    )
    bucket = s3.Bucket(getenv("S3_BUCKET_NAME"))
    for obj in objects:
        bucket.upload_file(obj, obj)
