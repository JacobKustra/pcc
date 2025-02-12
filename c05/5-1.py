car = 'Lambo'
car2 = 'toyota'

print("Is car == 'Lambo'? I predict True.")
print(car == 'Lambo')

print("Is car == 'lambo'? I predict False.")
print(car == 'lambo')

print("Is car.lower() == 'lambo'? I predict True.")
print(car.lower() == 'lambo')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'Lambo' and car2 == 'toyota'? I predict True.")
print(car == 'Lambo' and car2 == 'toyota')

print("Is car == 'Lambo' and car2 == 'Toyota'? I predict False.")
print(car == 'Lambo' and car2 == 'Toyota')

print("Is car == 'Lambo' or car2 == 'dodge'? I predict True.")
print(car == 'Lambo' or car2 == 'dodge')

print("Is car == 'toyota' or car2 == 'Lambo'? I predict False.")
print(car == 'toyota' or car2 == 'Lambo')

print("Is car == 'Lambo' and car2.title() == 'Toyota'? I predict True.")
print(car == 'Lambo' and car2.title() == 'Toyota')

print("Is car == '' or car2 == ''? I predict False.")
print(car == '' or car2 == '')
