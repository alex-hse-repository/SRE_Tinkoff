#!/bin/python3

import requests
import json

HOST = "http://localhost:8080"

users = [
    {
        "name": "s.petrov",
        "info": {
            "contacts": {
                "call": "+7 111-111-1111",
                "email": "s.petrov@student.com",
                "slack": "s.petrov",
                "sms": "+7 111-111-1111",
            },
            "full_name": "Sergey Petrov",
            "photo_url": None,
            "time_zone": "Europe/Moscow",
            "active": 1,
        },
    },
    {
        "name": "a.chikov",
        "info": {
            "contacts": {
                "call": "+7 222-222-2222",
                "email": "a.chikov@student.com",
                "slack": "a.chikov",
                "sms": "+7 222-222-2222",
            },
            "full_name": "Alexander Chikov",
            "photo_url": None,
            "time_zone": "Europe/Moscow",
            "active": 1,
        },
    },
    {
        "name": "s.kuznezov",
        "info": {
            "contacts": {
                "call": "+7 333-333-3333",
                "email": "s.kuznezov@student.com",
                "slack": "s.kuznezov",
                "sms": "+7 333-333-3333",
            },
            "full_name": "Sergey Kuznezov",
            "photo_url": None,
            "time_zone": "Europe/Moscow",
            "active": 1,
        },
    },
    {
        "name": "d.tikhomirov",
        "info": {
            "contacts": {
                "call": "+7 444-444-4444",
                "email": "d.tikhomirov@student.com",
                "slack": "d.tikhomirov",
                "sms": "+7 444-444-4444",
            },
            "full_name": "Dmitry Tikhomirov",
            "photo_url": None,
            "time_zone": "Europe/Moscow",
            "active": 1,
        },
    },
]


def main():
    print("Clearing the old users...")
    existing_users = requests.get(f"{HOST}/api/v0/users").json()
    for user in existing_users:
        requests.delete(f"{HOST}/api/v0/users/{user['name']}")

    print("Creating new users...")
    for user in users:
        requests.post(
            f"{HOST}/api/v0/users",
            json={
                "name": user["name"],
            },
        )
        requests.put(
            f"{HOST}/api/v0/users/{user['name']}",
            json=user["info"],
        )

    print("List of users:")
    existing_users = requests.get(f"{HOST}/api/v0/users").json()
    print(json.dumps(existing_users, indent=4))


if __name__ == "__main__":
    main()
