"""
I need to use: sort, reverse, sorted, len, remove, pop, del, insert, append
and accessing values within the list
"""
langs = [
    'english', 'polish', 'spanish', 'japanese', 'chinese', 'korean', 
    'dutch'
]
print('\nOriginal list order:')
print(langs)

print('\nTemp reverse sorted list order:')
print(sorted(langs, reverse = True))

print('\nOriginal list order:')
print(langs)

print('\nTemp sorted list order:')
print(sorted(langs))

print('\nOriginal list order:')
print(langs)

print('\nSorted list order:')
langs.sort()
print(langs)

print('\nReversed list order:')
langs.reverse()
print(langs)

print(len(langs))

langs.remove('english')
print(langs)

langs.append('english')
print(langs)

del langs[-1]
print(langs)

langs.pop()
print(langs)

# Intential index error 
# print(f'the second element in the list is {langs[22]}')
