import boto3

def write_file(collection, file_name, new_eol = False):
    if new_eol == True:
        new_eol = '\n'
    else:
        new_eol = ''
    
    file_string = str(file_name)

    with open(f'docs/{file_string}.txt','w') as file:
        for item in collection:
            file.write(str(item)+ new_eol )


pricing_client = boto3.client('pricing')

service_descriptor : dict = pricing_client.describe_services()

# with open('docs/service_discriptors.txt','w') as file:
#     for item in service_descriptor:
#         file.write(str(service_descriptor['Services']))

write_file(service_descriptor['Services'],'service_discriptor')


ec2_stuff= pricing_client.describe_services(
    ServiceCode='AmazonEC2'
)

attribute_names = ec2_stuff['Services'][0]['AttributeNames']

write_file(attribute_names,'attribute_names', True)

# for i in attribute_names:
#     print(i)
#     print(pricing_client.get_attribute_values(
#         ServiceCode = 'AmazonEC2',
#         AttributeName= i
#     ))
attribute_dict = dict()

for attribute_name in attribute_names:
    pricing_first_try =pricing_client.get_attribute_values(
        ServiceCode = 'AmazonEC2',
        AttributeName = attribute_name
    )
    available_values = pricing_first_try['AttributeValues']
    available_values_list = [item['Value'] for item in available_values]
    # print(available_values_list)

    attribute_dict[attribute_name]= available_values_list
    


