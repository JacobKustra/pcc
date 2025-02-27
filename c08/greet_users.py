def greet_users(names):
    '''Print a simple greeting for everyone in the list'''
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ["Jake", "emily", "ty"]
greet_users(usernames)
