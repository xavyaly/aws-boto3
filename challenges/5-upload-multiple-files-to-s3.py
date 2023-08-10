#!/usr/bin/python3

# Certainly! You can upload multiple files to an S3 bucket using a loop to iterate through the list of files. Here's an example using the `upload_file` function from Boto3 to upload multiple files:

import boto3
import os

def upload_files(files, bucket):
    """Upload multiple files to an existing S3 bucket

    :param files: List of file paths to upload
    :param bucket: Existing bucket to upload files to
    """
    s3_client = boto3.client('s3')
    
    for file_path in files:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            try:
                s3_client.upload_file(file_path, bucket, file_name)
                print(f"Uploaded '{file_path}' to bucket '{bucket}' as '{file_name}'")
            except Exception as e:
                print(f"Error uploading '{file_path}': {e}")
        else:
            print(f"File '{file_path}' not found.")

# List of file paths to upload
file_paths = ['file1.txt', 'file2.png', 'file3.pdf']

# Example usage
existing_bucket_name = 'unique-bucket-09082023'
upload_files(file_paths, existing_bucket_name)

# Replace `'your-existing-bucket-name'` with the name of your existing S3 bucket, and update the `file_paths` list with the paths to the files you want to upload.

# This code iterates through the list of file paths, uses the `upload_file` function to upload each file to the specified bucket, and provides feedback on the upload process for each file.


# Execution Output

# $ python3 5-upload-multiple-files-to-s3.py 
# Uploaded 'file1.txt' to bucket 'unique-bucket-09082023' as 'file1.txt'
# Uploaded 'file2.png' to bucket 'unique-bucket-09082023' as 'file2.png'
# Uploaded 'file3.pdf' to bucket 'unique-bucket-09082023' as 'file3.pdf'