class shape:
    #step 1 create cups/initialize class constructor
    def __init__(self,l,b):
        self.l = l
        self.b = b

    #step 2 create function
    def find_area(self):
        self.area = self.l * self.b
        print("Megan area =",self.area)
# step 3 create object variables
l = 347
b = 463
# step 4 order cups/create object
object1 = shape(l,b)

# step 5 call function
object1.find_area()
