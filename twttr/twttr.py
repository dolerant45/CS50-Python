twt = input('Input: ')
for i in twt:
    if i in 'AaEeIiOoUu':
        twt = twt.replace(i, '')
    else:
        continue


print(twt)
