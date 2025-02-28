class User:
    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is a {self.age} "
        f"{self.gender}, living in {self.location}.")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}.")

bob = User('Bob', 'johnson', 27, 'texas', 'male')
jess = User('Jess', 'McKinney', 19, 'california', 'female')
greg = User('greg', 'philips', 65, 'georgia', 'male')

bob.describe_user()
bob.greet_user()
jess.describe_user()
jess.greet_user()
greg.describe_user()
greg.greet_user()
