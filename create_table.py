"""
   mySolution @ kiddjsh

"""
"""
    Creates an Amazon DynamoDB table that can be used to store data.
    The table uses Key as the partition key, no sort key is used.

    :param TableName: The name of the table to create.
    :return: The newly created table.
"""

#boto3 is the aws software development kit (sdk) for python
import boto3

# Gets the service resource.
DDB_RESOURCE = boto3.resource('dynamodb', region_name="us-east-1")

# Create the DynamoDB table.
table = DDB_RESOURCE.create_table(
    TableName='Services',
    KeySchema=[
                    {'AttributeName': 'Key', 
                     'KeyType': 'HASH' # Partition key
                    },  
        ],
        AttributeDefinitions=[
                    {'AttributeName': 'Key',
                     'AttributeType': 'S'
                    },
        ],
        ProvisionedThroughput={
                     'ReadCapacityUnits': 10, 
                     'WriteCapacityUnits': 10
            
        }
)

# Waits until the table exists.
table.wait_until_exists()

# Prints out some data about the table.
print(table)
print("Table created successfully!")



