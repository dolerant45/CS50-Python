am = 50
while am > 0:
    coin = int(input('Insert coin: '))
    if coin == 25 or coin  == 10 or coin == 5:
        if coin >= am:
            am -= coin
            print(f"Change owed: {abs(am)}")
        else:
            am -= coin
            print(f"Amount Due: {am}")
    else:
        print(f"Amount Due: {am}")
