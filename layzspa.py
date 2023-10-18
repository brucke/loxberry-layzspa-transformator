#!/usr/bin/env python3
import sys
from dataclasses import dataclass
import json

DEBUG = True


def skills():
    print("description=Transfomer to controll LayzSpa via loxone")
    print("link=https://todefine")
    print("input=json")
    print("output=json")


if sys.argv[1] == "skills":
    skills()
    exit(0)

values = sys.argv[1]
data = json.loads(values)
for key, value in data.items():
    input = value.split(" ")

    if input[0] == "air":
        cmd = {
            "CMD": int(2),  # SETBUBBLES
            "VALUE": int(input[1]),
            "XTIME": 0,
            "INTERVAL": 0,
        }

    if input[0] == "heating":
        cmd = {
            "CMD": int(3),  # SETHEATER
            "VALUE": int(input[1]),
            "XTIME": 0,
            "INTERVAL": 0,
        }

    if input[0] == "filter":
        cmd = {
            "CMD": int(4),  # SETPUMP
            "VALUE": int(input[1]),
            "XTIME": 0,
            "INTERVAL": 0,
        }

    if input[0] == "ambient":
        cmd = {
            "CMD": int(15),  # SETAMBIENTC
            "VALUE": int(float(input[1])),
            "XTIME": 0,
            "INTERVAL": 0,
        }

    print(json.dumps({key: json.dumps(cmd)}))
