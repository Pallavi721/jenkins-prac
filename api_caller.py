import requests
import time

URL = "https://jsonplaceholder.typicode.com/users"

def get_users():
    try:
        response = requests.get(URL, timeout=5)

        # Raises an exception for 4xx/5xx errors
        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        log_message("ERROR: Request timed out")

    except requests.exceptions.ConnectionError:
        log_message("ERROR: Connection error")

    except requests.exceptions.HTTPError as e:
        log_message(f"ERROR: HTTP Error - {e}")

    except Exception as e:
        log_message(f"ERROR: Unexpected Error - {e}")

    return None


def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("api_log.txt", "a") as log:
        log.write(f"{timestamp} - {message}\n")

    print(f"{timestamp} - {message}")


def save_users(users):
    with open("users.txt", "w") as file:
        for user in users:
            file.write(f"{user['name']}\n")


print("Starting API Automation Script...")

#automation loop to fetch users every 60 seconds, 
# without it the script would only run once and exit
while True:
    log_message("Fetching users from API")

    users = get_users()

    if users:
        save_users(users)
        log_message(f"SUCCESS: Retrieved {len(users)} users and saved to users.txt")

    log_message("Waiting 60 seconds for next run")
    time.sleep(60)