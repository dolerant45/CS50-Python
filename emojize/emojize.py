import emoji

def main():
    text = input('Input: ')
    print(f"Output: {emojitt(text)}")


def emojitt(t):
    return emoji.emojize(t, language='alias')

main()
