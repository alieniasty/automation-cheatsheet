from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import ipaddress

# Authenticate with Azure
credential = DefaultAzureCredential()
subscription_id = ''  # replace with your subscription ID

# Create a Network Management Client
client = NetworkManagementClient(credential, subscription_id)

# Define the IP address to check
ip_to_check = ipaddress.ip_address('')

# List all virtual networks in the subscription and check if the IP is in their range
try:
    for vnet in client.virtual_networks.list_all():
        for subnet in vnet.address_space.address_prefixes:
            network = ipaddress.ip_network(subnet)
            if ip_to_check in network:
                print(f"The IP address {ip_to_check} is within the VNet: {vnet.name}, CIDR: {subnet}")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"The IP address {ip_to_check} is NOT within the following CIDR blocks: {vnet.address_space.address_prefixes}")    
