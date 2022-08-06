"""
   mySolution @ kiddjsh

"""
"""
    Creates an Amazon DynamoDB table that can be used to store data.
    The table uses Key as the partition key, no sort key is used.

    :param TableName: The name of the table to create.
"""

# boto3 is the aws software development kit (sdk) for python
import boto3

# Gets the service resource.
DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

# A resource representing an Amazon DynamoDB Table
table = DDB_RESOURCE.Table("Services")

# Creates a new item, or replaces an old item with a new item. 
table.put_item(
    Item={
        "Key": "00000",
        "Resource": "Solutions Architect (SA)",
        "Solution": "Network Architecture",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00001",
        "Resource": "Solutions Architect (SA)",
        "Solution": "Database Architecture",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00002",
        "Resource": "Solutions Architect",
        "Solution": "Performance Architecture",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00003",
        "Resource": "Solutions Architect (SA)",
        "Solution": "Compute Architecture",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00004",
        "Resource": "Solutions Architect (SA)",
        "Solution": "Storage Architecture",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00005",
        "Resource": "Cloud Infrastructure Architect (CIA)",
        "Solution": "Cloud Operating Model Architecture",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00006",
        "Resource": "Cloud Infrastructure Architect (CIA)",
        "Solution": "Cloud Infrastructure Design",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00007",
        "Resource": "Cloud Infrastructure Architect (CIA)",
        "Solution": "Cloud Integration & APIs",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00008",
        "Resource": "Cloud Infrastructure Architect (CIA)",
        "Solution": "Cloud Migration",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
   Item={
        "Key": "00009",
        "Resource": "Cloud Infrastructure Architect (CIA)",
        "Solution": "Technical Artifacts Development",
        }
)

# Waits until the table exists.
table.wait_until_exists()

# Prints response after table exits.
print("Items created successfully!")
