prompt = "\nPlease enter your pizza toppings: "
prompt += "\n(Enter 'quit' when you are done)"

while True:
    message = input(prompt)
    if message != 'quit':
        print(f'Adding {message} to your pizza')
    else:
        break
