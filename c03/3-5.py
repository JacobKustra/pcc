dinner_guests = ['elon musk', 'nikola tesla', 'grandpa']

print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[2].title()}, I invite you to be my dinner guest.')

print('\nGrandpa cannot make it to dinner')
dinner_guests.pop()

dinner_guests.append('Emily')
print(f'{dinner_guests[0].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[1].title()}, I invite you to be my dinner guest.')
print(f'{dinner_guests[2].title()}, I invite you to be my dinner guest.')

