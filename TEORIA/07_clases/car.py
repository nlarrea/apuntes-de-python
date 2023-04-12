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
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers


# ALMACENAR VARIAS CLASES EN UN ÚNICO MÓDULO

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 420
        elif self.battery_size == 100:
            range = 500
        
        print(f"This car can go about {range} kilometers on a full charge.")

    
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()