import csv
import random
import datetime
import io
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage settings
connection_string = "DefaultEndpointsProtocol=https;AccountName=singamgen2;AccountKey=zPkw1+PlXzcaH8HBOYD2faE671p7ZvKoTw79qbbiLgaBBozrhkgK5JrgmA6XmVYwQypQ9S/Ua+6H+AStRw0B2g==;EndpointSuffix=core.windows.net"
container_name = "predictiveanalytics"

# Generate random data
def generate_random_data(num_records):
   data = []
   for _ in range(num_records):
       unique_id = random.randint(1, 1000)
       value = random.uniform(0, 1)
       data.append((unique_id, value))
   return data

# Save data as CSV in-memory
def save_data_as_csv_in_memory(data):
   csv_buffer = io.StringIO()
   writer = csv.writer(csv_buffer)
   writer.writerow(["UniqueID", "Value"])
   writer.writerows(data)
   csv_buffer.seek(0)
   return csv_buffer.getvalue()

if __name__ == "__main__":
   num_records = 100  # Change this to the number of random records you want to generate
   random_data = generate_random_data(num_records)

   # Get the current date and time for folder and file naming
   now = datetime.datetime.now()
   folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
   file_name = "random_data.csv"

   # Save data as CSV in-memory
   csv_data = save_data_as_csv_in_memory(random_data)

   # Upload the CSV data to Azure Blob Storage in the date-time folder
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   container_client = blob_service_client.get_container_client(container_name)
   blob_client = container_client.get_blob_client(f"{folder_name}/{file_name}")

   blob_client.upload_blob(csv_data, overwrite=True)

   print(f"CSV data uploaded to Azure Blob Container '{container_name}' in folder '{folder_name}' as '{file_name}'.")
