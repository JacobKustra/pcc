from random import choice

grouping = [10, 22, 45, 99, 65, 5, 2, 12, 100, 89, 'a', 'p', 'r', 's', 'c']

win = []

def lottery_roll():
    win = []
    for i in range(1, 5):
        roll = choice(grouping)
        grouping.remove(roll)
        win.append(roll)

    print(win)

def lottery_print():
    print('winning numbers: ')
    for n in win:
        print(n)

my_ticket = [22, 2, 100, 45]

times_played = 0
active = True
while active:
    if my_ticket == win:
       times_played += 1
       active = False
       print(times_played)
    else:
        times_played += 1
        grouping = [10, 22, 45, 99, 65, 5, 2, 12, 100, 89, 'a', 
                    'p', 'r', 's', 'c']
        lottery_roll() 
