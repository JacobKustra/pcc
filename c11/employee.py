class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first = first_name
        self.last = last_name
        self.salary = annual_salary

    def give_raise(self, raise_amount=None):
        if raise_amount:
            self.salary += raise_amount
        else:
            self.salary += 5000
