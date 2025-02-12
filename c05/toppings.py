requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('hold the anchovies!')

print()
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(requested_toppings)
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#new toppings

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('Finished making your pizza')

print('Would not work as elifs')

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('Finished making your pizza')

print('\n\nMore efficient way:')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print('Finished making your pizza')

print('\n\nMore efficient way but missing green peppers:')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we are out of green peppers')
    else:
        print(f'Adding {requested_topping}.')

print('Finished making your pizza')


print('\n\nCheck if list is empty:')
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
         print(f'Adding {requested_topping}.')
    print('Finished making your pizza')
else:
    print('Are you sure you want a plain pizza?')


print('\n\nCheck if toppings are available:')
available_toppings = [
    'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
    'extra cheese'
]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f'Sorry, we do not have {requested_topping}')

print("\nFinished making your pizza")

