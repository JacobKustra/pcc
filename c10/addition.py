print("Give me two numbers and I will add them")
print("Enter 'q' to quit.")

first_number = input("\nFirst number: ")
if first_number == 'q':
second_number = input("Second number: ")
if second_number == 'q':

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please enter numbers only!")
else:
    print(answer)
