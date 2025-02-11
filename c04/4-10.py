cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

print('The first three items in the list are:')
print(cubes[0:3])
print('Some middle three items in the list are:')
print(cubes[2:5])
print('The last three items in the list are:')
print(cubes[-3:])

