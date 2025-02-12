age = 12

if age < 4:
    print('Your admission is $0')
elif age < 18:
    print('Your admission is $25.')
else:
    print('Your admission is $40.')

print('\n\nMore concise way:')
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f'Your admission is ${price}')

print('\n\nOmit else:')
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Your admission is ${price}')
