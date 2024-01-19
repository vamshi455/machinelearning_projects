import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=singamgen2;AccountKey=zPkw1+PlXzcaH8HBOYD2faE671p7ZvKoTw79qbbiLgaBBozrhkgK5JrgmA6XmVYwQypQ9S/Ua+6H+AStRw0B2g==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Example: List containers
containers = blob_service_client.list_containers()
for container in containers:
    print(container.name)
