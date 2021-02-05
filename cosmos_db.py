''' 
  @Author: Uthsavi KP
  @Date: 2021-02-03 15:07:51
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-02-03 9:46:38
  @Title: Azure cosmosDB using python
'''

import azure.cosmos.cosmos_client as cosmos_client
from azure.cosmos import PartitionKey
import family


# Initialize the Cosmos client
endpoint = ""
key = ''

# Create client
client = cosmos_client.CosmosClient(endpoint, key)
database_name = 'AzureSampleFamilyDataBase'
database = client.create_database_if_not_exists(id=database_name)


# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
container_name = 'FamilyContainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/lastName"),
    offer_throughput=400
)

# Adding items to the container
family_items_to_create = [family.get_andersen_family_item()]
for family_item in family_items_to_create:
    container.create_item(body=family_item)

# Read items ,key value lookups by partition key and id
for family in family_items_to_create:
    item_response = container.read_item(item=family['id'], partition_key=family['lastName'])
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

query = "SELECT * FROM c WHERE c.lastName IN ('Andersen')"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))