class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} with {self.mileage} miles")

    def drive(self, miles):
        if miles > 0:
            self.mileage += miles
            print(f"Driven {miles} miles.")
        else:
            print("Miles must be positive.")

my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
my_car.drive(100)
my_car.display_info()
