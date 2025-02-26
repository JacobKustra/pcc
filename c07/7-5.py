# Ticket pricing: under 3 = $0, 3-12 = $10, 12 and older = $15

prompt = "\nPlease enter your age:"
prompt += "\n(Type 'quit' to exit) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print(f'Since you are {age}, your ticket is $0')
        elif (age >= 3) & (age < 12):
            print(f'Since you are {age}, your ticket is $10')
        else:
            print(f'Since you are {age}, your ticket is $15')
