import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
    match = re.search(pattern, ip)
    if match:
        a, b, c, d = ip.split(".")
        if all(int(x) < 256 and ((len(x) == 3 and not x.startswith(("00", "0"))) or (len(x) == 2 and not x.startswith("0")) or len(x) == 1) for x in [a, b, c, d]):
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
