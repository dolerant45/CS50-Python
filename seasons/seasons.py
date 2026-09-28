import time
import inflect
import datetime as dt
class Minutes:
    def __init__(self, year_1, year_2):
        self.year_1 = year_1
        self.year_2 = year_2

    def split(self):
        self.year_1 = self.year_1.split("-")
        self.year_2 = self.year_2.split("-")

    def __str__(self):
        return self.year_1, self.year_2

def main():
   """ y = [2024, 1, 1]
    today = dt.date(2024, 1, 1)
    x = dt.date(2025, 1, 1)"""

   year_1 = input()
   year_2 = input()
   print(Minutes(year_1, year_2))




if __name__ == "__main__":
    main()
