prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you?")
print(age)

# print(age >= 18) # Can't do because user input is a string by default
age = int(age)
print(age >= 18)

