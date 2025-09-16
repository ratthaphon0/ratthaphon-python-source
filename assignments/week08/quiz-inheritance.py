""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year 
      
    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.numbers_of_doors = number_of_doors
    def get_info(self): 
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Doors: {self.numbers_of_doors}"
        
my_car = Car("Porsche", "Cayenne", 2015, 5)
print(my_car.get_info())