#!/bin/python3

import pandas as pd
import requests

HOST = "http://localhost:8080"
TEAMS = ["Team_1", "Team_2"]
ROSTER_NAME = "On Duty"
ROLES = ["primary", "secondary"]
SHIFT_HOUR = 10
START_DATETIME = pd.to_datetime(f"2022-11-02 {SHIFT_HOUR}:00:00")
SHIFT_LEN_DAYS = 3
TIME_PERIOD_DAYS = 62
SHIFT_LEN_DELTA = pd.to_timedelta(SHIFT_LEN_DAYS, unit="D")
NUMBER_OF_SHIFTS = TIME_PERIOD_DAYS // SHIFT_LEN_DAYS + 1
SHIFTS = [START_DATETIME + i * SHIFT_LEN_DELTA for i in range(NUMBER_OF_SHIFTS)]


def create_schedule(team):
    print(f"Create schedule for team {team}")
    rost_members = requests.get(f"{HOST}/api/v0/teams/{team}").json()["rosters"][ROSTER_NAME]["users"]
    rost_members = [x for x in rost_members if x["in_rotation"]]
    print(f"Team members: {rost_members}")

    for shift_datetime in SHIFTS:
        start_unix_timestamp = int(shift_datetime.timestamp())
        end_unix_timestamp = int((shift_datetime + SHIFT_LEN_DELTA).timestamp())
        for role, user in zip(ROLES, rost_members):
            requests.post(
                f"{HOST}/api/v0/events",
                json={
                    "user": user["name"],
                    "team": team,
                    "role": role,
                    "start": start_unix_timestamp,
                    "end": end_unix_timestamp,
                },
            )
        rost_members = list(reversed(rost_members))


if __name__ == "__main__":
    for team in TEAMS:
        # Change the scheduling timezone of the team
        requests.put(f"{HOST}/api/v0/teams/{team}", json={"scheduling_timezone": "Europe/Moscow"})
        create_schedule(team=team)
