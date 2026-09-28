import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::([0-5][0-9]))? (AM|PM) to (\d{1,2})(?::([0-5][0-9]))? (AM|PM)$"
    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


def to_24(hour, minute, period):
    hour = int(hour)

    if not 1 <= hour <= 12:
        raise ValueError

    minute = minute or "00"

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()
