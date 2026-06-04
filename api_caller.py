import os
import json
import requests

token = os.getenv("API_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

users = response.json()

# CREATE FILE
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print(response.status_code)

print("Current working dir:", os.getcwd())
print("Files after API call:", os.listdir())