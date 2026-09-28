import sys

def main():
    open_file()


def verify():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".py"):
        return sys.argv[1]
    else:
        sys.exit("Not a python file")

def open_file():
    try:
        with open(f"{verify()}", "r") as f:
            contents = f.readlines()
            count(contents)
    except FileNotFoundError:
        print("File does not exist")

def count(file):
    i = 0
    for line in file:
        stripped = line.strip()
        if stripped.startswith("#") or stripped == "":
            i += 0
        else:
            i += 1
    print(i, end="")

main()
