current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n\nCounting to 10")
current_number = 0
while current_number < 10:
    current_number += 1  # omitting this would make this run infinitely
    if (current_number % 2) == 0:
        continue
    print(current_number)
