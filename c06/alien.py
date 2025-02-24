alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You just earned {new_points} points!')


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5 

print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
print(f'The alien is {alien_0['color']}!')
alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0['color']}!')

print('Alien position')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position: {alien_0['x_position']}')

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# New position is old position plus the new increment
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print(f'New position: {alien_0['x_position']}')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print('\nUsing [] on item that is not in the dict, leads to errors')

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
print("Using the get method, allows for no errors")
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
