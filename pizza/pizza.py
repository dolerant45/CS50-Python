import sys
import csv
from tabulate import tabulate

def main():
    art(open_file())

def verify():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        return sys.argv[1]
    else:
        sys.exit("Not a CSV file")

def open_file():
    pizza = []
    with open(f"{verify()}") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pizza.append(row)
        return pizza

def art(l):
    print(tabulate(l, headers="keys", tablefmt="grid"))


main()
