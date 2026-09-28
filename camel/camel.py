variable = input('camelCase: ')
for i in variable:
    if i.isupper():
       variable = variable.replace(i, f"_{i.lower()}")
print(variable)
