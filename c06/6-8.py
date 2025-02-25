cat = {
    'age': 4,
    'sex': 'male',
    'name': 'leo',
}

dog = {
    'age': 6,
    'sex': 'female',
    'name': 'ruby',
}

lizard = {
    'age': 14,
    'sex': 'male',
    'name': 'Stevie',
}

pets = [cat, dog, lizard]

for pet in pets:
    for data, datapoints in pet.items():
        print(f'{data}: {datapoints}')
    print()
