from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient
import csv
import time

TENANT_ID = ''
CLIENT_ID = ''
CLIENT_SECRET = ''

credential = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
client = GraphClient(credential=credential)

def list_ad_groups_with_prefix(prefix):
    query_parameters = {
        '$filter': f"startswith(displayName, '{prefix}')"
    }
    groups = client.get('/groups', params=query_parameters)
    return groups.json()

prefix = "some-prefix"
groups = list_ad_groups_with_prefix(prefix)

with open('displayNames_ids.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for item in groups['value']:
        writer.writerow([item['displayName'], item['id']])