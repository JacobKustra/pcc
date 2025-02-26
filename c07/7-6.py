# Ticket pricing: under 3 = $0, 3-12 = $10, 12 and older = $15

prompt = "\nPlease enter your age:"
prompt += "\n(Type 'quit' to exit) "

# Exit 1
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

# Exit 2
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print(f'Since you are {age}, your ticket is $0')
        elif (age >= 3) & (age < 12):
            print(f'Since you are {age}, your ticket is $10')
        else:
            print(f'Since you are {age}, your ticket is $15')

# Exit 3
age = ""
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        continue
    else:
        age = int(age)
        if age < 3:
            print(f'Since you are {age}, your ticket is $0')
        elif (age >= 3) & (age < 12):
            print(f'Since you are {age}, your ticket is $10')
        else:
            print(f'Since you are {age}, your ticket is $15')

