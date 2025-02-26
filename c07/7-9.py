sandwich_orders = [
    'pastrami', 'blt', 'veggie', 'pastrami', 'turkey club', 'tuna', 'pastrami'
]
finished_sandwiches = []

print('The deli has run out of pastrami sandwiches')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")

    finished_sandwiches.append(sandwich)

print("\nHere are the completed orders:")
for sandwich in finished_sandwiches:
    print(sandwich)
