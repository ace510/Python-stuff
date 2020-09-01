import boto3
import json
from refresh_pricing_docs import write_file

pricing_client = boto3.client("pricing")

boiler_plate = dict(Type="TERM_MATCH", Field="memory", Value="0.5 GiB")
filter2 = dict(Type="TERM_MATCH", Field="location", Value="US East (N. Virginia)")


testy = pricing_client.get_products(
    ServiceCode="AmazonEC2",
    Filters=[boiler_plate, filter2],
)

# print(testy['FormatVersion'])
# testy['PriceList']
# print(testy['NextToken'])

test_dict = json.loads(testy["PriceList"][0])
write_file(test_dict.keys(), "pricelistparts", True)

write_file(testy["PriceList"], "availible_listings")

print(test_dict["terms"])
