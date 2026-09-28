import re
ip = input()
pattern = r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}'
if match := re.fullmatch(pattern, ip):
    print(True)
else:
    print(False)
