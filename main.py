import json
import sys
import time
import requests

from config import TOKEN, GUILD_ID, VANITY

def change_vanity():
    '''
    Returns True if the vanity was changed, False if not.
    '''
    res = requests.patch(
        f"https://discord.com/api/v8/guilds/{GUILD_ID}/vanity-url",
        headers={"Authorization": TOKEN, "Content-Type": "application/json"},
        data=json.dumps({ "code": VANITY }),
        timeout=10
    )

    return res.status_code == 200

def check_vanity():
    '''
    Returns True if the vanity is available, False if not.
    '''
    res = requests.get(f"https://discord.com/api/v10/invites/{VANITY}", timeout=5)
    body = res.json()

    return "message" in body

def main():
    if not TOKEN:
        print("Please enter your token in config.py.")
        sys.exit(1)

    if not GUILD_ID:
        print("Please enter your guild ID in config.py.")
        sys.exit(1)

    if not VANITY:
        print("Please enter your vanity in config.py.")
        sys.exit(1)

    print("Starting checker...")
    while True:
        print("Checking...")
        if check_vanity():
            # Is Available
            print("Vanity is available, changing...")
            while not change_vanity():
                print("Failed to change vanity, retrying...")
                time.sleep(1)
            sys.exit(0)
        print("Vanity is not available, waiting...")
        time.sleep(10)

if __name__ == "__main__":
    main()
