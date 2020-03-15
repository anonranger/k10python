class shape:
    #  Step 1 - create cup/initialize class constructor
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    
    # Step 2 - Create function to calculate area, perimeter
    def calc_area_peri(self):
        self.area = self.length * self.breadth
        print("Area =", self.area)

        self.peri = (2*self.length) + (2*self.breadth)
        print("Perimeter =", self.peri)
        
# Step 3 - create object variable
length = 2
breadth = 6

#Step 4 - create object
object1 = shape(length,breadth)

#step 5 - call function
object1.calc_area_peri()


        
