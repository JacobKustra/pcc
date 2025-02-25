rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'mississippi': 'usa',
}

for key, value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}.')
for key in rivers.keys():
    print(f'{key.title()}')
for value in rivers.values():
    print(f'{value.title()}.')
