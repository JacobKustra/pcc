sandwich_orders = ['blt', 'veggie', 'turkey club', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")

    finished_sandwiches.append(sandwich)

print("\nHere are the completed orders:")
for sandwich in finished_sandwiches:
    print(sandwich)
