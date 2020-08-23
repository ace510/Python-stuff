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


def main():
    pricing_client = boto3.client('pricing')
    
    
    # building list of all service Descriptors
    #basically a dict with the service names and all the atribute names for them
    service_descriptor : dict = pricing_client.describe_services()
    write_file(service_descriptor['Services'],'service_discriptor')

    
    
    # this code grabs all the info specific to EC2, i'm grabbing all the
    # attribute names and all their availible options
    ec2_stuff= pricing_client.describe_services(
        ServiceCode='AmazonEC2')
    attribute_names = ec2_stuff['Services'][0]['AttributeNames']
    write_file(attribute_names,'attribute_names', True)


    attribute_dict = dict()

    for attribute_name in attribute_names:
        pricing_first_try =pricing_client.get_attribute_values(
            ServiceCode = 'AmazonEC2',
            AttributeName = attribute_name
        )
        available_values = pricing_first_try['AttributeValues']
        available_values_list = [item['Value'] for item in available_values]

        attribute_dict[attribute_name]= available_values_list

    with open('docs/attributes.txt','w+') as file:
        for key, value in attribute_dict.items():
            file.write(f'{key}: {value} \n')

if __name__ == "__main__":
    main()