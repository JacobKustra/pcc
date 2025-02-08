locations = ['thailand', 'bali', 'switzerland', 'japan', 'poland']
print('\nOriginal list:')
print(locations)

print('\nTemp sorted list:')
print(sorted(locations))
print('\nOriginal list remains unchanged:')
print(locations)

print('\nTemp reverse sorted list:')
print(sorted(locations, reverse = True))
print('\nOriginal list remains unchanged:')
print(locations)

print('\nReversed sorted list:')
locations.reverse()
print(locations)

print('\nReversed sorted list again:')
locations.reverse()
print(locations)

print('\nSorted list:')
locations.sort()
print(locations)

print('\nReversed sorted list again but with sort:')
locations.sort(reverse = True)
print(locations)
