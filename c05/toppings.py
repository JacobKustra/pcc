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
