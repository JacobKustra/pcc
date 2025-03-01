from pathlib import Path
import json

def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    user = {}
    user['username'] = input("What is your name? ")
    user['age'] = int(input("What is your age? "))
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['username']}, you are {user['age']} "
              f"years old!")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")

greet_user()
