def main():
    fraction = input("Fraction: ").split("/")
    return print(percentage(fraction))


def percentage(x):
    try:
        perc = (int(x[0]) / int(x[1])) * 100
        if perc > 100 or perc < 0:
            x = input("Fraction: ").split("/")
            perc = (int(x[0]) / int(x[1])) * 100
            
    except ValueError:
        x = input("Fraction: ").split("/")
        perc = (int(x[0]) / int(x[1])) * 100

    except ZeroDivisionError:
        x = input("Fraction: ").split("/")
        perc = (int(x[0]) / int(x[1])) * 100

    if perc > 100 or perc < 0:
        x = input("Fraction: ").split("/")
        perc = (int(x[0]) / int(x[1])) * 100

    elif 0 <= perc <= 1:
        return "E"

    elif 99 <= perc <= 100:
        return "F"

    return f"{round(perc)}%"

main()
