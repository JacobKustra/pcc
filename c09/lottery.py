from random import choice

grouping = [10, 22, 45, 99, 65, 5, 2, 12, 100, 89, 'a', 'p', 'r', 's', 'c']

win = [choice(grouping), choice(grouping), choice(grouping), choice(grouping)]

print('winning numbers: ')
for n in win:
    print(n)
