"""
   AWS_DynamoDB_Solutions #kiddjsh

"""
"""
    Updates items to an Amazon DynamoDB table used to store data.
    The table uses Entity as the partition key, no sort key is used.

    :Python Version: Python 3.7.10
    :param Key: The primary key of the item to be updated.
    :param UpdateExpression: A collection of attributes containing at least name.
"""

# boto3 is the aws software development kit (sdk) for python
import boto3

# Gets the service resource.
DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

# A resource representing an Amazon DynamoDB Table
table = DDB_RESOURCE.Table("Architecture")

Entity = "00011"

# Edits an item's attribute, or adds a new item if it does not already exist. 
table.update_item(
    #The primary key of the item to be updated.
    Key={
        "Entity": Entity
    },
    #An expression that defines one or more attributes to be updated.
    UpdateExpression="SET Echo = :E",
    #One or more values that can be substituted in an expression. 
    ExpressionAttributeValues={
        ":E": "AWS Cloud Architect"
    },
    #Gets the item attributes as they appear before they were deleted.
    ReturnValues="UPDATED_NEW"
)
