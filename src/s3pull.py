import boto3
from os import getenv
from dotenv import load_dotenv
import logging


def pull_objects(objects: list[str]) -> None:
    logging.info("Pulling objects from S3...")
    session = boto3.Session(
        aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    )
    s3 = session.resource(
        service_name="s3", endpoint_url=getenv("S3_ENDPOINT_URL")
    )
    bucket = s3.Bucket(getenv("S3_BUCKET_NAME"))
    for obj in objects:
        bucket.download_file("latest/" + obj, "data/" + obj)
    logging.info("Objects pulled from S3!")


if __name__ == "__main__":
    load_dotenv()
    pull_objects(["config.json", "database.db"])
