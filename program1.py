class Dog:
    # create cups/Class constructor
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    # create function to check temperature
    def check_temp(self):
        if self.temperature > 99:
            print(self.name, "has high Fever.")
        else:
            print(self.name, "has No Fever.")

# Create Objects and assign values to variables
dog1_name = 'cupcake'
dog1_temp = 100

# Create object / order cups
object1_dog = Dog(dog1_name, dog1_temp)

# call function check temperature
object1_dog.check_temp()
