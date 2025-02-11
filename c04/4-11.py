pizzas = ['veggie', 'pepperoni', 'white']
for pizza in pizzas:
    print(f'I like {pizza} pizza.')

print('I just really love a good pizza')

friend_pizzas = pizzas[:]

pizzas.append('margarita')
friend_pizzas.append('stuffed crust')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friends favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)

