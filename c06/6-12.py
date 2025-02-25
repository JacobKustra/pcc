cities = {
    'San Francisco': {
        'population': 808908,
        'state': 'california'
    },

    'Austin': {
        'population': 979882,
        'state': 'texas'
    },

    'Bristol': {
        'population': 61601,
        'state': 'connecticut'
    },
}

for city, facts in cities.items():
    print(f'\nFacts about {city}:')
    for fact, details in facts.items():
        print(f'\t{fact.title()}: {details}')
