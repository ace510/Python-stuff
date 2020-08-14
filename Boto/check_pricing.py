import boto3

pricing_client = boto3.client('pricing')

service_descriptor : dict = pricing_client.describe_services()

with open('docs/service_discriptors.txt','w') as file:
    for item in service_descriptor:
        file.write(str(service_descriptor['Services']))

service_descriptor : dict = pricing_client.describe_services()

with open('docs/services.txt','w') as file:
    for item in service_descriptor['Services']:
        file.write(str(item))

ec2_stuff= pricing_client.describe_services(
    ServiceCode='AmazonEC2'
)

blarga = ec2_stuff['Services'][0]['AttributeNames']
