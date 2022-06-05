import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'vernal-verve-351110-d85c476c21a8.json'

storage_client = storage.Client()

for bucket in storage_client.list_buckets():
    print(bucket)
