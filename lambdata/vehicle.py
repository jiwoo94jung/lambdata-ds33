# parent class is more generic
class Vehicle:
    # static attribute
    wheels = 4

    # Constructor - defines user supplied attributes that we want to use in creating an object
    def __init__(self, make, model, color, year=2021, mileage=0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        print("HOOOOOONK!")

    def drive(self, miles_driven):
        print('VROOOM!')
        self.mileage = self.mileage + miles_driven

# child class is more specific and inherits attributes and methods from the parent class
class Car(Vehicle):
    # Constructor - defines user supplied attributes that we want to use in creating an object
    # 3 required attributes, two optional attributes, and one static
    def __init__(self, make, model, color, style, year=2021, mileage=0):
        super().__init__(make, model, color, year, mileage)
        # only need to add the attribute that is not being inherited
        self.style = style

# detect if the file is being imported in a REPl or being run as a script
# This if statement condition will only be true if the file is being run as a script

print('running in a REPL or script')

if __name__ == '__main__':
    my_car = Car('toyota','camry','gray', 2007, 251000, 'sedan')

    print(my_car.style)
    print(my_car.mileage)
    print(my_car.honk())

    print('running as a script')
