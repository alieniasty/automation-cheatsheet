from azure.storage.blob import BlobServiceClient, BlobClient
import os

def upload_file_to_blob(container_name, blob_name, file_path, connection_string):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
            print(f"File {file_path} uploaded to {container_name}/{blob_name}.")
    except Exception as ex:
        print(f"Error occurred: {ex}")

container_name = 'your-container-name'
blob_name = 'your-blob-name' # The name you want the uploaded file to have
file_path = 'path/to/your/local/file'
connection_string = 'your-storage-account-connection-string'

upload_file_to_blob(container_name, blob_name, file_path, connection_string)
