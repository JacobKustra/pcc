motorcycles = ['honda', 'yamaha', 'suzuki', 'harley']

print(motorcycles)

motorcycles[-1] = 'ducati'

print(motorcycles)

motorcycles.append('harley')

print(motorcycles)

motorcycles = []

print(motorcycles)

motorcycles.append('harley')
motorcycles.append('harley')
motorcycles.append('harley')
print(motorcycles)

motorcycles.insert(0, 'yamaha')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()


print(motorcycles)
print(popped_motorcycles)

print(f'The last motorcycle I owned was the {popped_motorcycles}')

first_owned = motorcycles.pop(0)

print(f'The first  motorcycle I owned was the {first_owned}')

motorcycles = ['honda', 'yamaha', 'suzuki', 'harley']
print(motorcycles)

motorcycles.remove('harley')

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'harley']
print(motorcycles)

not_good = 'harley'

motorcycles.remove(not_good)

print(motorcycles)

print(f'The {not_good} is not my kind of motorcycle.')
