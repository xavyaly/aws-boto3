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



# Code Explanation

# Certainly! Let's go through the modified code step by step to understand how it works:

# 1. **Import Required Modules**:
#    ```python
#    import logging
#    import boto3
#    from botocore.exceptions import ClientError
#    import time
#    ```
#    The code starts by importing necessary modules: `logging` for logging messages, `boto3` for AWS interaction, `ClientError` from `botocore.exceptions` to handle specific AWS errors, and `time` for adding a delay between retries.

# 2. **Define the `create_bucket` Function**:
#    ```python
#    def create_bucket(bucket_name, region=None):
#    ```
#    This function is used to create an S3 bucket. It takes two parameters: `bucket_name` (the name of the bucket to be created) and `region` (the region where the bucket should be created).

# 3. **Set Constants and Logging Configuration**:
#    ```python
#    DEFAULT_REGION = 'us-east-1'
#    LOCATION_CONSTRAINT = region if region else DEFAULT_REGION
#    ```
#    These constants define the default region and location constraint. If a specific region is provided, it's used; otherwise, the default region is used.

#    ```python
#    logging.basicConfig(level=logging.INFO)
#    ```
#    This configures the logging system to display messages at the `INFO` level and above.

# 4. **Attempt to Create the Bucket**:
#    ```python
#    try:
#        s3_client = boto3.client('s3', region_name=DEFAULT_REGION)
#        location = {'LocationConstraint': LOCATION_CONSTRAINT}
#        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
#        logging.info(f"Bucket '{bucket_name}' created in region '{LOCATION_CONSTRAINT}'")
#        return True
#    except ClientError as e:
#        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
#            logging.info(f"Bucket '{bucket_name}' already exists.")
#            return False
#        else:
#            logging.error(f"Error creating bucket: {e}")
#            return False
#    ```
#    Inside the `try` block, the function creates an S3 client and attempts to create the bucket using `s3_client.create_bucket()`. If successful, it logs a success message and returns `True`.

#    If the `create_bucket` operation raises a `ClientError`, the code checks if the error code is `'BucketAlreadyOwnedByYou'`, which indicates that the bucket already exists and is owned by you. In this case, the function logs a message and returns `False`.

#    If any other error occurs during the bucket creation attempt, the function logs an error message and returns `False`.

# 5. **Example Usage and Retries**:
#    ```python
#    bucket_name = 'unique-bucket-09082023'
#    region = 'us-west-2'
#    max_retries = 3
#    for attempt in range(max_retries):
#        if create_bucket(bucket_name, region):
#            print(f"Bucket '{bucket_name}' created successfully.")
#            break
#        else:
#            print(f"Failed to create bucket '{bucket_name}'. Retrying...")
#            time.sleep(2)  # Wait for 2 seconds before retrying
#    else:
#        print(f"Max retries reached. Could not create bucket '{bucket_name}'.")
#    ```
#    This part of the code demonstrates the example usage of the `create_bucket` function. It attempts to create the bucket with retries. If the bucket creation is successful (`create_bucket` returns `True`), it prints a success message and exits the loop using `break`.

#    If the bucket creation fails, it prints a retry message, waits for 2 seconds using `time.sleep(2)`, and then retries the operation. If the maximum number of retries (`max_retries`) is reached without success, it prints a message indicating that the maximum retries were reached.

# Overall, this code combines error handling, logging, and retry mechanisms to create an S3 bucket, considering scenarios where the bucket might already exist or the operation might fail temporarily.
