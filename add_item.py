"""mySolution @ kiddjsh"""
from pprint import pprint
import boto3


"""Encapsulates an Amazon DynamoDB table of core services data."""

def put_item(Core, Service, ServiceID, dynamodb = None):
    if dynamodb is None:
        DDB_RESOURCE = boto3.resource('dynamodb', region_name="us-east-1")
    """
    Adds a Core Service to the table.

    :param Core: The title of the position.
    :param Service: Type of service preformed.
    :param Service ID: Service Identifier for service preformed.
    """
    
    table = DDB_RESOURCE.Table('DynamoDB_TestTable')
    response = table.put_item(
            Item={
                'Core': Core,
                'Service': Service,
                'ServiceID': ServiceID,
            }
        )
    return response
        
if __name__ == '__main__':
    """
    item_resp = put_item("Solutions Architect", "Database Architecture", "001")
    """
    item_resp = put_item("Solutions Architect", "Amazon Database Infrastructure", "002")
    item_resp = put_item("Solutions Architect", "Database Migration - Deploying Microsoft SQL", "003")
    print("Put item succeeded:")
    pprint(item_resp)
    