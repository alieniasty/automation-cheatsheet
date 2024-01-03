from azure.identity import ClientSecretCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
import base64

TENANT_ID = ""
CLIENT_ID = ""
CLIENT_SECRET = ""

credential = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)

key_client = KeyClient(vault_url="", credential=credential)

key_name = "key"
key = key_client.get_key(key_name)

crypto_client = CryptographyClient(key, credential)

encrypted_password = ""
decoded_encrypted_pwd = base64.b64decode(encrypted_password)

decrypted_password = crypto_client.decrypt(EncryptionAlgorithm.rsa_oaep, decoded_encrypted_pwd)

password = decrypted_password.plaintext.decode('utf-8')

print(password)