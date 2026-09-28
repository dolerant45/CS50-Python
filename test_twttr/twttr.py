def main():
    word = input('Input: ')
    print(shorten(word))


def shorten(twt):
    for i in twt:
        if i in 'AaEeIiOoUu':
            twt = twt.replace(i, '')
        else:
            continue
    return twt

if __name__ == "__main__":
    main()
