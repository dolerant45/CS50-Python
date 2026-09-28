import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<hours>[1-9]|1[0-2]):?(?P<minutes>[0-5][0-9])? (?P<time>PM|AM) to (?P<hours_to>[1-9]|1[0-2]):?(?P<minutes_to>[0-5][0-9])? (?P<time_to>PM|AM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError
    if match.group("time") == "AM" and match.group("hours") == "12":
        m = match.group("minutes")
        h = "00"
    elif match.group("time") == "AM":
        m = match.group("minutes")
        if len(match.group("hours")) == 1:
            h = f"0{match.group("hours")}"
        else:
            h = match.group("hours")
    elif match.group("time") == "PM" and match.group("hours") == "12":
        h = match.group("hours")
        m = match.group("minutes")
    elif match.group("time") == "PM":
        h = int(match.group("hours")) + 12
        m = match.group("minutes")
    if match.group("time_to") == "AM" and match.group("hours_to") == "12":
        m = match.group("minutes_to")
        h = "00"
    elif match.group("time_to") == "AM":
        m_to = match.group("minutes_to")
        if len(match.group("hours_to")) == 1:
            h_to = f"0{match.group("hours_to")}"
        else:
            h_to = match.group("hours_to")
    elif match.group("time_to") == "PM" and match.group("hours_to") == "12":
        h_to = match.group("hours_to")
        m_to = match.group("minutes_to")
    elif match.group("time_to") == "PM":
        h_to = int(match.group("hours_to")) + 12
        m_to = match.group("minutes_to")
    if m == None:
        m = "00"
    if m_to == None:
        m_to = "00"
    return f"{h}:{m} to {h_to}:{m_to}"

if __name__ == "__main__":
    main()
