"""
   AWS_DynamoDB_Solutions #kiddjsh

"""
"""
    Gets item of an Amazon DynamoDB table used to store data.
    The table uses Entity as the partition key, no sort key is used.

    :Python Version: Python 3.7.10
    :param Key: The primary key of the item to be updated.
    :param ProjectionExpression: A string that identifies one or more attributes to retrieve from the table. 
"""

# boto3 is the aws software development kit (sdk) for python
import boto3

# Gets the service resource.
DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

# A resource representing an Amazon DynamoDB Table
table = DDB_RESOURCE.Table("Architecture")

# Returns a set of attributes for the item with the given primary key. 
response = table.get_item(
    # A map of attribute names to objects, representing the primary key of the item to retrieve.
    Key={
        "Entity": "00000"
    },
    # Determines the read consistency model.
    ConsistentRead=True,
    # Determines the level of detail about either provisioned or on-demand throughput consumption.
    ReturnConsumedCapacity='TOTAL',
    # A string that identifies one or more attributes to retrieve from the table.
    ProjectionExpression="Echo, #E",
    # One or more substitution tokens for attribute names in an expression.
    ExpressionAttributeNames={
        '#E': 'Locus'
    }
)

# Prints out some data about the item.
print(response['Item'])


