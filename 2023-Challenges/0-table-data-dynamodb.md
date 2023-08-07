<!-- START -->

# Configure aws cli -> 
    $ aws configure 
    AWS Access Key ID [****************5V7G]: 
    AWS Secret Access Key [****************MF1Y]: 
    Default region name [us-east-2]: 
    Default output format [json]: 

# Create a DynamoDB Table
    aws dynamodb create-table \
        --table-name Books \
        --attribute-definitions AttributeName=ISBN,AttributeType=S \
        --key-schema AttributeName=ISBN,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

# Once table created, cross check in AWS UI

# Check the python version
# python3 --version
    $ Python 3.11.3

# Install boto3 
    $ pip3 install boto3

# Create a <script-name>.sh file 
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'MyTable'

def upload_data_to_dynamodb(data):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=data)
    print('Item added to DynamoDB table:', response['ResponseMetadata']['HTTPStatusCode'])

if __name__ == "__main__":
    data_to_upload = {
        'ISBN': '1234567890',  # Primary key attribute
        'Title': 'Example Book',
        'Author': 'John Doe',
        'Year': 2023
    }

    upload_data_to_dynamodb(data_to_upload)

# Provide permission to shell script
    $ chmod +x <script-name>.sh 

# Execute the script
    $ ./<script-name>.sh

# Cross check the populated data once script executed successfully via AWS UI

# Cross check the table contents via CLI
    $ aws dynamodb scan --table-name Books

# Delete DynamoDB Table
    $ aws dynamodb delete-table --table-name Books

<!-- END  -->