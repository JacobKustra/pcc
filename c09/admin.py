from users_classes import User
class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 
                                   'can ban user']):
        self.privileges = privileges

    def show_privileges(self): 
        for privileges in self.privileges:
            print(privileges)

class Admin(User):
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = Privileges() 


