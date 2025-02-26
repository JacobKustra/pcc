responses = {}

while True:
    name = input('\nWhat is your name? ')
    response = input('\nWhat is your dream vacation spot? ')
    
    responses[name] = response

    cont = input('\nDo you want to poll more people? (yes/no) ')
  
    if cont == 'no':
        break

print("Poll results:")
for name, response in responses.items():
    print(f"{name.title()} responded with: {response}")
