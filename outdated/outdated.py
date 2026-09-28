def main():
    day = input("Date: ")
    print(date(day))



def date(d):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            if "/" in d:
                s = d.split('/')
                year = s[2].strip()
                month = int(s[0])
                day = int(s[1])

            elif "," in d:
                s = d.split(",")
                ss = s[0].split(' ')
                year = s[1].strip()
                month = months.index(ss[0]) + 1
                day = int(ss[1])
            if 1 <= day <= 31 and 1 <= month <= 12:
                return f"{year}-{month:02d}-{day:02d}"
            else:
                raise ValueError
        except UnboundLocalError:
            d = input("Date: ")
        except ValueError:
            d = input("Date: ")



main()
