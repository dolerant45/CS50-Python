x = input('File name: ').strip().lower()
y = x.split('.')
if x.endswith(('.gif', '.png')):
    print(f'image/{y[-1]}')
elif x.endswith(('.jpeg','.jpg')):
    print('image/jpeg')
elif x.endswith(('.pdf', '.zip')):
    print(f'application/{y[-1]}')
elif x.endswith(('.txt')):
    print('text/plain')
else:
    print('application/octet-stream')

