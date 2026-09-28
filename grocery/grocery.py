def main():
    items = []
    items_2 = []
    while True:
        try:
            item = input().upper()
            items.append(item)
        except EOFError:
            for i in items:
                if i not in items_2:
                    items_2.append(i)
            items_2.sort()
            for k in items_2:
                print(f"{items.count(k)} {k}")
            return

main()
