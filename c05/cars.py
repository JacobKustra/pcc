cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

print('\nCapitalization matters')
car = 'Audi'
print(car)
print(car == 'audi')
print(car.lower() == 'audi')

