answer = 17
if answer != 42:
    print('That is not correct! Please try again.')

age = 19
print(age)
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

print('\nMultiple checks with "and"')
age_0 = 22
age_1 = 19

print(age_0, age_1)
print(age_0 >= 21 and age_1 >=21)

age_1 = 21
print(age_0, age_1)
print(age_0 >= 21 and age_1 >=21)

print('\nMultiple checks with "or"')
age_0 = 22
age_1 = 18

print(age_0, age_1)
print(age_0 >= 21 or age_1 >=21)

age_0 = 18
print(age_0, age_1)
print(age_0 >= 21 or age_1 >=21)

