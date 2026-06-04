import json

with open("users.json") as file:
    users = json.load(file)

with open("reports/report.txt", "w") as report:
    report.write(f"Total Users: {len(users)}\n")

print("Report generated successfully")