import random
def main():
    points = 0
    i = 0
    level = get_level()
    equation = generate_integer(level)
    while i < 20:
        a = 0
        while a < 3:
            try:
                answer = int(input(f"{equation[i]} + {equation[i + 1]} = "))
            except ValueError:
                a += 1
                print("EEE")
                continue

            if answer == equation[i] + equation[i + 1]:
                points += 1
                break
            else:
                print("EEE")
                a += 1
        else:
            print(f"{equation[i]} + {equation[i+1]} = {equation[i] + equation[i+1]}")
        i += 2
    print(f"Points: {points}")

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l > 3 or l < 1:
                raise ValueError
            break
        except ValueError:
            pass
    return l

def generate_integer(lev):
    numbers = []
    for i in range(10):
        if lev == 1:
            numbers.append(random.randint(0, 9))
            numbers.append(random.randint(0, 9))
        elif lev == 2:
            numbers.append(random.randint(10, 99))
            numbers.append(random.randint(10, 99))
        elif lev == 3:
            numbers.append(random.randint(100, 999))
            numbers.append(random.randint(100, 999))
    return numbers

if __name__ == "__main__":
    main()
