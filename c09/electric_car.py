class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back the odometer!')
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('Filling the gas tank!')

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print('This car does not have a gas tank!')

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# 
# lambo = Car('lamborghini', 'huracan', 2022)
# lambo.fill_gas_tank()
# my_leaf.fill_gas_tank()
# 
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
