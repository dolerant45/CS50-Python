def main():
    greet = input('Greeting: ')
    print(f"${value(greet)}")

def value(greeting):
    g = greeting.strip().lower().split(' ')
    if g[0][:-1] == 'hello' or g[0] == 'hello':
        return 0
    elif 'h' == g[0][0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
