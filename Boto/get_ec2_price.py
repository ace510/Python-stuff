import boto3

pricing_client = boto3.client('pricing')

boiler_plate = {'Type':'TERM_MATCH'}



boiler_plate['Field'] = 'memory'
boiler_plate['Value'] = '0.5 GiB'

testy = pricing_client.get_products(
    ServiceCode='AmazonEC2',
    Filters=[boiler_plate],)

# print(testy['FormatVersion'])
# testy['PriceList']
# print(testy['NextToken'])

#print(testy['PriceList'][0])

print(testy['PriceList'][0] is str)