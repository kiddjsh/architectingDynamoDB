"""
   AWS_DynamoDB_Solutions #kiddjsh

"""
"""
    Querys table of an Amazon DynamoDB used to store data.
    The table uses Entity as the partition key, no sort key is used.

    :Python Version: Python 3.7.10
    :param Key: The primary key of the item to be updated.
"""

# boto3 is the aws software development kit (sdk) for python
import boto3

from boto3.dynamodb.conditions import Key, Attr

# Gets the service resource.
DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

# A resource representing an Amazon DynamoDB Table
table = DDB_RESOURCE.Table("Architecture")

Entity = "Entity"

# Returns all items with the given primary key. 
response = table.query(
    # Returns all of the item attributes from the specified table or index.
    Select='ALL_ATTRIBUTES',
    # The maximum number of items to evaluate.
    Limit=50,
    # Determines the read consistency model.
    ConsistentRead=True,
    # The condition that specifies the key values for items to be retrieved.
    KeyConditionExpression=Key("Entity").eq("00000"),

)

# Prints out some data about the item.
for i in response['Items']:
    print(i['Entity'], ":", i['Echo'], ":", i['Locus'])