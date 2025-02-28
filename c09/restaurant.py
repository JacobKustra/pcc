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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'strawberry', 'chocolate', 'swirl']

    def display_flavors(self):
        print("Here is our IceCream menu.")
        for flavor in self.flavors:
            print(flavor)

