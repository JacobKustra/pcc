my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)
print('\nMy friends favorite foods are:')
print(friend_foods)

print()
print()
print('this wont work')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)
print('\nMy friends favorite foods are:')
print(friend_foods)

print()
print()
print('for loops:')

for food in my_foods:
    print(food)
for food in friend_foods:
    print(food)
