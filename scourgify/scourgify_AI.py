import sys
import csv


def main():
    input_file, output_file = verify()

    try:
        with open(input_file, "r") as r, open(output_file, "w", newline="") as w:
            reader = csv.DictReader(r)
            writer = csv.DictWriter(w, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


def verify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()
