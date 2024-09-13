import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
client = boto3.client('dynamodb')

# Replace these with actual values for db_type, aws_account_id, and table_name

db_type = "rds"
aws_account_id = "234"
table_name = "rds1"

try:
    # Update the item by setting 'onboarding_needed' to false
    update_response = client.update_item(
        TableName='central',
        Key={
            'db_type': {'S': db_type},  # Partition key
            'aws_account_id': {'S': aws_account_id},  # Sort key
            # If table_name is part of key schema, add it here too
        },
        UpdateExpression="set onboarding_needed = :val",
        ExpressionAttributeValues={
            ':val': {'BOOL': False}
        },
        ReturnValues="UPDATED_NEW"
    )
    # Print the updated attributes
    print(f"Updated item: {update_response['Attributes']}")
except ClientError as e:
    print(f"Error updating item: {e.response['Error']['Message']}")
