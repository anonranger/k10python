class dog:
    # create cups/initialize class constructor
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    # create function to check temp
    def check_temp(self):
        if self.temp > 99:
            print(self.name, "has high fever.")
        else:
            print(self.name, "definitely does not have fever.")

# create object variables
dog1_name = 'goldie'
dog1_temp = 0

# order cups / create object
object1 = dog(dog1_name, dog1_temp)

# call function check temp
object1.check_temp()
