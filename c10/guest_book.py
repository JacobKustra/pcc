from pathlib import Path

path = Path('guest_book.txt')

guest_list = ''

active = True
while active:
    guest = input("Enter 'q' to quit or your name here: ")
    if guest == 'q':
        active = False
    else:
        guest_list += f'{guest}\n'

path.write_text(guest_list)
