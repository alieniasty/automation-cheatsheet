#!/bin/bash

# Variables
container_name="your-container-name"
file_path="path/to/your/local/file"
blob_name="your-blob-name"
connection_string="your-storage-account-connection-string"
storage_account_name="your-storage-account-name"

az storage blob upload \
    --container-name $container_name \
    --file $file_path \
    --name $blob_name \
    --account-name $storage_account_name \
    --connection-string $connection_string

echo "File $file_path uploaded to $container_name/$blob_name."
