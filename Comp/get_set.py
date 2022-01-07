class Student:
#declaring a global variables.
    __name =None
    __rollNumber = None

#setting the name in a private method
    def setName(self,x):
        self.__name = x

#getter
    def getName(self):
        return self.__name

#setter
    def setRollNumber(self,y):
        self.__rollNumber = y
        
#getter method to access the private properties
    def getRollNumber(self):
        return self.__rollNumber

demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())
    