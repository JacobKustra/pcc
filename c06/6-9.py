favorite_places = {
    'jacob': [
        'poland',
        'california',
        'texas',
    ],

    'emily': [
        'bar habor, maine',
        'los angeles',
        'vegas',
    ],
    
    'leo': [
        'gravy bowl',
        'couch',
        'box',
    ],
}

for friend, favorites in favorite_places.items():
    print(f"{friend.title()}'s favorite places are:")
    for fav in favorites:
        print(fav)
