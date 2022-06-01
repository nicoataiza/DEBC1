import os
from dotenv import load_dotenv

load_dotenv('.env')

print(os.getenv("DOMAIN"))
print(os.getenv("DOMAIN_PASSWORD","testing"))