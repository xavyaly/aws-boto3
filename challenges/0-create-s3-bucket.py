#!/usr/bin/python3

import logging
import boto3
from botocore.exceptions import ClientError
import time

def create_bucket(bucket_name, region=None):
    # Constants
    DEFAULT_REGION = 'us-east-1'
    LOCATION_CONSTRAINT = region if region else DEFAULT_REGION
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Create bucket
    try:
        s3_client = boto3.client('s3', region_name=DEFAULT_REGION)
        
        location = {'LocationConstraint': LOCATION_CONSTRAINT}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        logging.info(f"Bucket '{bucket_name}' created in region '{LOCATION_CONSTRAINT}'")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            logging.info(f"Bucket '{bucket_name}' already exists.")
            return False
        else:
            logging.error(f"Error creating bucket: {e}")
            return False

# Example usage
bucket_name = 'unique-bucket-09082023'
region = 'us-east-2'
max_retries = 3
for attempt in range(max_retries):
    if create_bucket(bucket_name, region):
        print(f"Bucket '{bucket_name}' created successfully.")
        break
    else:
        print(f"Failed to create bucket '{bucket_name}'. Retrying...")
        time.sleep(2)  # Wait for 2 seconds before retrying
else:
    print(f"Max retries reached. Could not create bucket '{bucket_name}'.")


