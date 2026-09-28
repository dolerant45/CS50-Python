x = input()
fr = '🙁'
sm = '🙂'
w = x.split(' ')
for i in range(len(w)):
    if w[i] == ':)':
        w[i] = sm
    elif w[i] == ':(':
        w[i] = fr
print(' '.join(w))
