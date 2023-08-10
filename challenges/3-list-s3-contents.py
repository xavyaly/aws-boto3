#!/usr/bin/python3

import boto3

def list_bucket_contents(bucket):
    """List the objects in an existing S3 bucket

    :param bucket: Existing bucket to list contents from
    """
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            print(f"Objects in bucket '{bucket}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"No objects found in bucket '{bucket}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
existing_bucket_name = 'unique-bucket-09082023'
list_bucket_contents(existing_bucket_name)


# Execution Output

# $ python3 3-list-s3-contents.py 
# Objects in bucket 'unique-bucket-09082023':
#  - file1.txt
#  - file2.jpg
#  - file2.png
#  - file3.pdf