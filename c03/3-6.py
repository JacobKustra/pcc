dinner_guests = ['elon musk', 'nikola tesla', 'grandpa']

print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[2].title()}, I invite you to be my dinner guest.')

print('A bigger dinner table was found so three more guests will be invited')

dinner_guests.insert(0, 'Dad')
dinner_guests.insert(2, 'Mom')
dinner_guests.append('Pat')

print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[2].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[3].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[4].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[5].title()}, I invite you to be my dinner guest.')
