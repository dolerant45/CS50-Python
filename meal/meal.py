def main():
    t = input('What time is it: ')
    if 7 <= convert(t) <= 8:
        print('breakfast time')
    elif 12 <= convert(t) <= 13:
        print('lunch time')
    elif 18 <= convert(t) <= 19:
        print('dinner time')

def convert(time):
    x = time.split(':')
    s = float(x[0])+float(x[1])/60
    return s

if __name__ == "__main__":
    main()  
