def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    d = ''
    for i in s:
        if i.isdigit():
            d += i
        else:
            continue
    return s[:2].isalpha() and 2 <= len(s) <= 6 and s.isalnum() and (d[0] != '0' and s.endswith(d) if len(d) > 0 else True)



main()
