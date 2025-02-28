class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type} food.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open.')

    def set_number_served(self, guests):
        olive_garden.number_served = guests

    def increment_number_served(self, num):
        olive_garden.number_served += num

olive_garden = Restaurant('Olive Garden', 'Italian')
olive_garden.describe_restaurant()
olive_garden.open_restaurant()
print(olive_garden.number_served)

olive_garden.number_served = 33
print(olive_garden.number_served)

olive_garden.set_number_served(100)
print(olive_garden.number_served)

olive_garden.increment_number_served(44)
print(olive_garden.number_served)
