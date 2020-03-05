class Dog:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def dog_temp(self):
        if self.temperature > 100:
            print(self.name, "has Fever")
        else:
            print(self.name, "has No Fever")



dogs_list = []

print()
for i in range(3):
    print("-" * 25, "DOG", i+1, "-" * 25)
    name = input("Enter Name: ")
    temperature = int(input("Enter Temperature: "))
    dogs_list.append(Dog(name, temperature))

print()
for dog in dogs_list:
    dog.dog_temp()