from pathlib import Path

path = Path('guest.txt')

active = True
guest = input("Enter 'q' to quit or your name here: ")

path.write_text(guest)
