#!/usr/bin/python3

import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an existing S3 bucket

    :param file_name: File to upload
    :param bucket: Existing bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded successfully, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        logging.info(f"File '{file_name}' uploaded to bucket '{bucket}' as '{object_name}'")
        return True
    except ClientError as e:
        logging.error(f"Error uploading file: {e}")
        return False

# Example usage
file_to_upload = 'file.txt'
existing_bucket_name = 'unique-bucket-09082023'

if upload_file(file_to_upload, existing_bucket_name):
    print(f"File '{file_to_upload}' uploaded successfully to '{existing_bucket_name}'.")
else:
    print(f"Failed to upload '{file_to_upload}' to '{existing_bucket_name}'.")
