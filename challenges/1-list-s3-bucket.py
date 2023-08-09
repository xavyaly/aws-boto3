#!/us/bin/python3

#!/usr/bin/python3

import logging
import boto3
from botocore.exceptions import NoCredentialsError

def list_buckets():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Create an S3 client
    try:
        s3_client = boto3.client('s3')
        
        response = s3_client.list_buckets()
        buckets = response['Buckets']
        
        if buckets:
            logging.info("List of S3 buckets:")
            for bucket in buckets:
                logging.info(f"Bucket: {bucket['Name']}")
        else:
            logging.info("No S3 buckets found in the account.")
    except NoCredentialsError:
        logging.error("AWS credentials not found. Please configure your credentials.")
        return

# Call the list_buckets function to list all S3 buckets
list_buckets()
