import os
import json

os.makedirs("reports", exist_ok=True)

with open("users.json") as file:
    users = json.load(file)

with open("reports/report.txt", "w") as report:
    report.write(f"Total Users: {len(users)}\n")

print("Report generated successfully")