import os
import requests

token = os.getenv("API_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

print(response.status_code)