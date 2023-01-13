import boto3
from botocore.exceptions import ClientError
from rayka.local_settings import ACCESS_KEY, SECRET_KEY
import time
from django.http import Http404

#Connect to AWS account
client = boto3.client(
    'dynamodb',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-west-2'
    )


#Create DynamoDB table
def create_device_table():
    table = client.create_table(
        TableName='RaykaDevices',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
                                          

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

##Create record in a DynamoDB table
def put_device(id, deviceModel, name, note, serial):
    print("Creating New Record in DynamoDB")
    response = client.put_item(
       TableName='RaykaDevices',
       Item={
            'id': {
                'S': "{}".format(id),
            },
            'deviceModel': {
                'S': "{}".format(deviceModel),
            },
            'name': {
                "S": "{}".format(name),
            },
            'note': {
                "S": "{}".format(note),
            },
            'serial': {
                "S": "{}".format(serial),
            }
        }
    )
    # print(response)
    return response

##Get a record in from DynamoDB table
def get_device(id):
    try:
        response = client.get_item(       
                TableName='RaykaDevices',
                Key={
                        'id': {
                                'S': "{}".format(id),
                        },

                    }
                )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if response.get('Item'):
            return response['Item']
        raise Http404

if __name__ == '__main__':
    # Create DynamoDB
    device_table = create_device_table()
    print("Create DynamoDB succeeded............")
    print("Table status:{}".format(device_table))