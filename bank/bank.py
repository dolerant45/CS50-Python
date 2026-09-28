greeting = input('Greeting: ').strip().lower()

g = greeting.split(' ')
if g[0][:-1] == 'hello' or g[0] == 'hello':
    print('$0')
elif 'h' == g[0][0]:
    print('$20')
else:
    print('$100')
