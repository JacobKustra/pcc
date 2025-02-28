class User:
    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is a {self.age} "
        f"{self.gender}, living in {self.location}.")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self): 
        for privileges in self.privileges:
            print(privileges)

bob = Admin('Bob', 'johnson', 27, 'texas', 'male')
bob.show_privileges()

