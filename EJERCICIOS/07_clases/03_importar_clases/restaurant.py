class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} cuisine restaurant.")
    
    def open_restaurant(self):
        print(f"The {self.name} restaurant is opened!")