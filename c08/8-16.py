users_list = ['leo', 'tommy', 'fred']
print('\n1')
import greet_users
greet_users.greet_users(users_list)

print('\n2')
from greet_users import greet_users
greet_users(users_list)

print('\n3')
from greet_users import greet_users as gu
gu(users_list)

print('\n4')
import greet_users as g
g.greet_users(users_list)

print('\n5')
from greet_users import *
greet_users(users_list)
