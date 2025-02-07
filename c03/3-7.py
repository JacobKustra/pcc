dinner_guests = ['elon musk', 'nikola tesla', 'grandpa']

print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[2].title()}, I invite you to be my dinner guest.')

print('\nA bigger dinner table was found so three more guests will be invited')

dinner_guests.insert(0, 'Dad')
dinner_guests.insert(2, 'Mom')
dinner_guests.append('Pat')

print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[2].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[3].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[4].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[5].title()}, I invite you to be my dinner guest.')

print('\nA bigger dinner table was not able to be found, actually so guests '
'have to be uninvited.')

popped_guest = dinner_guests.pop()
print(f'Sorry {popped_guest}, you are no longer invited.')
popped_guest = dinner_guests.pop()
print(f'Sorry {popped_guest}, you are no longer invited.')
popped_guest = dinner_guests.pop()
print(f'Sorry {popped_guest}, you are no longer invited.')
popped_guest = dinner_guests.pop()
print(f'Sorry {popped_guest}, you are no longer invited.')

print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)
