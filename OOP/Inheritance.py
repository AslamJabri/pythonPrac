#declaring a base class
class Vehicle:
    def __init__(self,make,color,model) :
        self.make = make
        self.color = color
        self.model = model

    def print(self):
        print("Manufacturer: " , self.make)
        print("Color: " , self.color)
        print("model: " , self.model)
#reusing the base class which will inherit all the properties from the base class
class Car(Vehicle):
    def __init__(self, make, color, model,doors):
    #inherited the properties from base class
#can be used either like this ir by using super        #Vehicle.__init__(self,make, color, model)
    #this can also be used with super
       super().__init__(make,color,model)
       self.doors = doors
    
    def final(self):
        self.print()
        print("doors: " ,self.doors)



obj1 = Car("Suzuki" , "Grey" , "2015" , 4)
(obj1.final())