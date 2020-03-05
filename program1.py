class Dog:
    def __init__(self, name, temperature):
        # create class containers
        self.name = name
        self.temperature = temperature

    # Function to check for fever
    def temp(self):
        if self.temperature > 99:
            print(self.name, "has Fever")
        else:
            print(self.name, "has No Fever")

# Create Objects and assign values to variables
dog1_name = 'cupcake'
dog1_temp = 100
dog1 = Dog(dog1_name, dog1_temp)
dog1.temp()