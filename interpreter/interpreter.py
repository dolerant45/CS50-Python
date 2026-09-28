v = input('Expression: ')
x, y, z = v.split(' ')
x, z = int(x), int(z)
if y == '+':
    print(float(x+z))
elif y == '-':
    print(float(x-z))
elif y == '*':
    print(float(x*z))
elif y == '/' and z != 0:
    print(float(x/z))
