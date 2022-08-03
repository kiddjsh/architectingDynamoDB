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
    print(f"Creating item...")
    return response
        
if __name__ == '__main__':
    item_resp = put_item("Solutions Architect", "Database Architecture", "001")
    item_resp = put_item("Solutions Architect", "Amazon Database Infrastructure", "002")
    item_resp = put_item("Solutions Architect", "Database Migration - Deploying Microsoft SQL", "003")
    item_resp = put_item("Solutions Architect", "Performance Architecture", "004")
    item_resp = put_item("Solutions Architect", "Performance: Custom Benchmark Tests", "005")
    item_resp = put_item("Solutions Architect", "Performance: TPC-DS Industry Test", "006")
    item_resp = put_item("Solutions Architect", "Performance: Load Testing", "007")
    item_resp = put_item("Solutions Architect", "Performance: Amazon CloudWatch", "008")
    item_resp = put_item("Solutions Architect", "Compute Architecture", "009")
    item_resp = put_item("Solutions Architect", "Storage Architecture", "010")
    item_resp = put_item("Solutions Architect", "Storage: On-Premises Infrastructure", "011")
    item_resp = put_item("Solutions Architect", "Storage: Amazon EBS Solutions", "012")
    item_resp = put_item("Solutions Architect", "Storage: Amazon EC2 Instance Store Solutions", "013")
    item_resp = put_item("Solutions Architect", "Storage: Amazon EFS Solutions", "014")
    item_resp = put_item("Solutions Architect", "Storage: Amazon FSx Solutions", "015")
    item_resp = put_item("Solutions Architect", "Storage: Amazon EBS Solutions", "016")
    item_resp = put_item("Solutions Architect", "Storage: Amazon S3 Solutions", "017")
    item_resp = put_item("Solutions Architect", "Storage: Amazon S3 Glacier Solutions", "018")
    item_resp = put_item("Solutions Architect", "Network Architecture", "019")
    """
    """
    print(f"Items created")
    pprint(item_resp)
    