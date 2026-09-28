import inflect
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break

    return print(f"Adieu, adieu, to {p.join(names)}")

main()
