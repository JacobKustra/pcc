current_users = ['jake', 'admin', 'john', 'emily', 'barry']
new_users = ['Jake', 'EMILY', 'Tuan', 'Molly', 'sara']
current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('You will need to enter a new username')
    else:
        print('Username available')
