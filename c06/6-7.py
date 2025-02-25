person1 = {
    'first_name': 'Jacob', 
    'last_name': 'Kustra',
    'age': 25,
    'city': 'San Francisco',
}

person2 = {
    'first_name': 'emily', 
    'last_name': 'stadnicki',
    'age': 26,
    'city': 'San Francisco',
}

person3 = {
    'first_name': 'Leo', 
    'last_name': 'Kustra',
    'age': 4,
    'city': 'San Francisco',
}

people = [person1, person2, person3]

for peeps in people:
    for data, details in peeps.items():
        print(f'{data.title()}: {details}')
    print()
