class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type} food.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open.')

olive_garden = Restaurant('Olive Garden', 'Italian')
print(olive_garden.restaurant_name)
print(olive_garden.cuisine_type)

olive_garden.describe_restaurant()
olive_garden.open_restaurant()
