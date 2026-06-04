import requests
import json
from datetime import datetime

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print(f"Retrieved {len(users)} users from API successfully")

with open("logs/app.log", "a") as log:
    log.write(
        f"{datetime.now()} SUCCESS Retrieved {len(users)} users\n"
    )