import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            pass
    while True:
            try:
                g = int(input("Guess: "))
                if g <= 0:
                    raise ValueError
                break
            except ValueError:
                pass
    return print(game(n, g))

def game(level, guess):
    class TooSmallError(Exception):
        pass

    class TooLargeError(Exception):
        pass

    while True:
        try:
            number = random.randint(1, level)
            if number == guess:
                return "Just right!"
            elif guess < number:
                raise TooSmallError
            elif guess > number:
                raise TooLargeError
        except TooSmallError:
            print("Too small!")
            guess = int(input("Guess: "))
        except TooLargeError:
            print("Too large!")
            guess = int(input("Guess: "))


main()
