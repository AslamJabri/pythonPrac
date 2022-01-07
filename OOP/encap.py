class Rectangle:
    def __init__(self,length,width):
        #encapsulation using __ so that the property can be accessed privately
       self.__length = length
       self.__width = width 

    def area(self):
        return (self.__length*self.__width)

    def perimeter(self):
        p = 2*(self.__length + self.__width)
        return p

rect = Rectangle(3,5)
print(rect.area())
print(rect.perimeter())