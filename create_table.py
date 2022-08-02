import boto3


DDB_RESOURCE = boto3.resource('dynamodb', region_name="us-east-1")
"""
    Creates an Amazon DynamoDB table that can be used to store data.
    The table uses the core of the service as the partition key and the
    service as the sort key.

    :param table_name: The name of the table to create.
    :return: The newly created table.
"""
    
DDB_RESOURCE.create_table(
        
    TableName='DynamoDB_TestTable',
    KeySchema=[
                    {'AttributeName': 'Core', 
                     'KeyType': 'HASH' # Partition key
                    },  
                    {'AttributeName': 'Service', 
                     'KeyType': 'RANGE' # Sort key
                    }  
        ],
        AttributeDefinitions=[
                    {'AttributeName': 'Core', 
                     'AttributeType': 'S'
                    },
                    {'AttributeName': 'Service', 
                     'AttributeType': 'S'
                    }
        ],
        ProvisionedThroughput={
                     'ReadCapacityUnits': 10, 
                     'WriteCapacityUnits': 10
            
        }
    )
    
print("Table status:", DDB_RESOURCE.create_table)



