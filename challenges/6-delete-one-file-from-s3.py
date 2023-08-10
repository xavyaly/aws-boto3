#!/usr/bin/python3

# Certainly! To delete individual files from an S3 bucket at runtime, you can use the `delete_object` operation in Boto3. Here's an example:


import boto3

def delete_file(bucket, object_key):
    """Delete a file from an existing S3 bucket

    :param bucket: Existing bucket containing the file
    :param object_key: Key (name) of the file to delete
    """
    s3_client = boto3.client('s3')
    
    try:
        s3_client.delete_object(Bucket=bucket, Key=object_key)
        print(f"Deleted '{object_key}' from bucket '{bucket}'")
    except Exception as e:
        print(f"Error deleting '{object_key}': {e}")

# Example usage
existing_bucket_name = 'unique-bucket-09082023'
file_to_delete = 'file.txt'  # Replace with the key of the file to delete
delete_file(existing_bucket_name, file_to_delete)


# Replace `'your-existing-bucket-name'` with the name of your existing S3 bucket, and update `file_to_delete` with the key (name) of the file you want to delete.

# This code uses the `delete_object` operation to remove a specific file from the bucket and provides feedback on the deletion process. You can run this code for each file you want to delete from the bucket.


# Execution Output

# $ ls -l
# $ python3 3-list-s3-contents.py 
# No objects found in bucket 'unique-bucket-09082023'.
# $ 
# $ python3 5-upload-multiple-files-to-s3.py 
# Uploaded 'file1.txt' to bucket 'unique-bucket-09082023' as 'file1.txt'
# Uploaded 'file2.png' to bucket 'unique-bucket-09082023' as 'file2.png'
# Uploaded 'file3.pdf' to bucket 'unique-bucket-09082023' as 'file3.pdf'
# $ 
# $ python3 3-list-s3-contents.py 
# Objects in bucket 'unique-bucket-09082023':
#  - file1.txt
#  - file2.png
#  - file3.pdf
# $ 
# $ python3 2-upload-a-file-to-s3.py 
# File 'file.txt' uploaded successfully to 'unique-bucket-09082023'.
# $ 
# $ python3 3-list-s3-contents.py 
# Objects in bucket 'unique-bucket-09082023':
#  - file.txt
#  - file1.txt
#  - file2.png
#  - file3.pdf
# $ 
# $ python3 6-delete-one-file-from-s3.py 
# Deleted 'file.txt' from bucket 'unique-bucket-09082023'
# $ 
# $ python3 6-delete-one-file-from-s3.py 
# Deleted 'file.txt' from bucket 'unique-bucket-09082023'



