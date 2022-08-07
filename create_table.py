"""
   AWS_DynamoDB_Solutions #kiddjsh

"""
"""
    Creates an Amazon DynamoDB table that can be used to store data.
    The table uses Entity as the partition key, no sort key is used.

    :param TableName: The name of the table to create.
    :param KeySchema: Specifies the primary key for the table.
"""

# boto3 is the aws software development kit (sdk) for python
import boto3

# Gets the service resource.
DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

# Creates the DynamoDB table.
table = DDB_RESOURCE.create_table(
    # The name of the table to create.
    TableName="Architecture",
    
    # Specifies the attributes that make up the primary key for a table or an index.
    KeySchema=[
        {
            #The name of this key attribute.
            "AttributeName": "Entity",
            #The role that the key attribute will assume.
            "KeyType": "HASH"
        }
    ],
    #An array of objects that describe one attribute in the table and 
    #index key schema.
    AttributeDefinitions=[
        {
            #The name of the attribute.
            "AttributeName": "Entity",
            #The data type for the attribute.
            "AttributeType": "S"
        }
    ],
    #The settings for the table, consisting of read and write capacity units, 
    #along with data about increases and decreases.
    ProvisionedThroughput={
        #The maximum number of strongly consistent reads consumed per second 
        #before DynamoDB returns a ThrottlingException .
        "ReadCapacityUnits": 10,
        #The maximum number of writes consumed per second before DynamoDB 
        #returns a ThrottlingException .
        "WriteCapacityUnits": 10
    }
)

# Waits until the table exists.
table.wait_until_exists()

# Prints out some data about the table.
print(table)
print("Table created successfully!")