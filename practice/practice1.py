class dog: 
    # create cups/initialize class constructor
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    # create function to check temp
    def check_temp(self):
        if self.temp > 100:
            print(self.name, "has super high fever")
        else:
            print(self.name, "has no fever")

    # create object variables
dog1_name = 'lily'
dog1_temp = 97

# order cups / create object
object1 = dog(dog1_name, dog1_temp)

# call function check temp
object1.check_temp()



















            

