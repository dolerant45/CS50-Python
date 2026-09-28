import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        pattern = r".+src=\"https?://(www\.)?youtube\.com/embed/(?P<link>[a-zA-z0-9]+)\".+"
        match = re.search(pattern, s)
        return f"https://youtu.be/{match.group("link")}"
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
