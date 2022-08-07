"""
   AWS_DynamoDB_Solutions #kiddjsh
   
"""
"""
    Adds Items to an Amazon DynamoDB table used to store data.
    The table uses Entity as the partition key, no sort key is used.

    :Python Version: Python 3.7.10
    :param Item: A collection of attributes containing at least name.
"""

# boto3 is the aws software development kit (sdk) for python
import boto3

# Gets the service resource.
DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

# A resource representing an Amazon DynamoDB Table
table = DDB_RESOURCE.Table("Architecture")

# Creates a new item, or replaces an old item with a new item. 
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Software Engineering & Consulting",
        "Locus": "Simple Software Engineer (SSE)",
        "Entity": "00000",
    }
)

# Creates a new item, or replaces an old item with a new item. 
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Network Architecture",
        "Locus": "Solutions Architect (SA)",
        "Entity": "00001",
    }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Database Architecture",
        "Locus": "Solutions Architect (SA)",
        "Entity": "00002",
   }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Performance Architecture",
        "Locus": "Solutions Architect",
        "Entity": "00003"
    }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Compute Architecture",
        "Locus": "Solutions Architect (SA)",
        "Entity": "00004",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Storage Architecture",
        "Locus": "Solutions Architect (SA)",
        "Entity": "00005",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud Operating Model Architecture",
        "Locus": "Cloud Infrastructure Architect (CIA)",
        "Entity": "00006",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud Infrastructure Design",
        "Locus": "Cloud Infrastructure Architect (CIA)",
        "Entity": "00007",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud Integration & APIs",
        "Locus": "Cloud Infrastructure Architect (CIA)",
        "Entity": "00008",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud Migration",
        "Locus": "Cloud Infrastructure Architect (CIA)",
        "Entity": "00009",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Technical Artifacts Development",
        "Locus": "Cloud Infrastructure Architect (CIA)",
        "Entity": "00010",
        }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Database Architecture",
        "Locus": "Certified Cloud Practitioner (CCP)",
        "Entity": "00011"
   }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "SysOps Administration",
        "Locus": "Certified Cloud Practitioner (CCP)",
        "Entity": "00012"
   }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud Development",
        "Locus": "Certified Cloud Practitioner (CCP)",
        "Entity": "00013"
   }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud DevOps Engineer",
        "Locus": "Certified Cloud Practitioner (CCP)",
        "Entity": "00014"
   }
)

# Creates a new item, or replaces an old item with a new item.
table.put_item(
    # A map of attribute name/value pairs, one for each attribute.
    Item={
        #Attribute described as a name-value pair. 
        #The name is the data type, and the value is the data itself.
        "Echo": "Cloud Software Engineer",
        "Locus": "Certified Cloud Practitioner (CCP)",
        "Entity": "00014"
   }
)

# Waits until the table exists.
table.wait_until_exists()

# Prints response after table exits.
print("Items created successfully!")


