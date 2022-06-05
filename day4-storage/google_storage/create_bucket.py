import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'vernal-verve-351110-d85c476c21a8.json'

storage_client = storage.Client()


bucket = storage_client.bucket("sample-bucket-python-test-from-vscode")
bucket.storage_class = 'STANDARD' # Archive | Nearline | Standard | Coldline
bucket.location = 'asia-southeast1'   # https://cloud.google.com/storage/docs/locations
bucket = storage_client.create_bucket(bucket)
