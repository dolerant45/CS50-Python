import pyfiglet
import sys


def main():
    try:
        font = sys.argv[1:]
        if font[0] != "-f" and font[0] != "--font":
            sys.exit("Error")
        if font[1] not in pyfiglet.FigletFont.getFonts():
            sys.exit("Error")
    except IndexError:
        pass
    text = input("Input: ")
    print(f"Output: {figlet(text, font)}")


def figlet(t, f):
    try:
        return pyfiglet.figlet_format(t, font=f[1])
    except IndexError:
        return pyfiglet.figlet_format(t)
    except pyfiglet.FontNotFound:
        sys.exit("Error")


main()
