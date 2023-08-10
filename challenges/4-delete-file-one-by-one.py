#!/usr/bin/python3

import boto3

def delete_bucket_contents(bucket):
    """Delete all objects in an existing S3 bucket

    :param bucket: Existing bucket to delete contents from
    """
    s3_client = boto3.client('s3')

    try:
        response = s3_client.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            print(f"Deleting objects in bucket '{bucket}':")
            for obj in response['Contents']:
                object_key = obj['Key']
                s3_client.delete_object(Bucket=bucket, Key=object_key)
                print(f" - Deleted: {object_key}")
            print("All objects deleted.")
        else:
            print(f"No objects found in bucket '{bucket}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
existing_bucket_name = 'unique-bucket-09082023'
delete_bucket_contents(existing_bucket_name)


# Execution Output

# $ python3 4-delete-file-one-by-one.py 
# Deleting objects in bucket 'unique-bucket-09082023':
#  - Deleted: file1.txt
#  - Deleted: file2.jpg
#  - Deleted: file2.png
#  - Deleted: file3.pdf
# All objects deleted.