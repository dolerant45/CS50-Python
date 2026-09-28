def main():
    x = input("Fraction: ")
    return print(gauge(convert(x)))


def convert(fraction):
    fraction = fraction.split("/")
    try:
        perc = (int(fraction[0]) / int(fraction[1])) * 100

    except ValueError:
        return "Error"

    except ZeroDivisionError:
        return "Error"

    return perc

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
