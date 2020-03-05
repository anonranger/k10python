class Dog:
    # create cups/initialize class constructor
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    # create function to check temperature
    def check_temp(self):
        if self.temperature > 99:
            print(self.name, "has high fever.")
        else:
            print(self.name, "has no fever.")

# create and assign object variables
dog1_name = 'cupcake'
dog1_temp = 100

# order cups / create object
object1_dog = Dog(dog1_name, dog1_temp)

# call function check temperature
object1_dog.check_temp()
