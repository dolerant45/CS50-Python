import sys
import csv


def main():
    open_file(verify())


def verify():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        return sys.argv[1], sys.argv[2]
    else:
        sys.exit("Not a CSV file")


def open_file(l):
    with open(f"{l[0]}") as r, open(f"{l[1]}", "w") as w:
        reader = csv.DictReader(r)
        writer = csv.DictWriter(w, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
                })

main()
