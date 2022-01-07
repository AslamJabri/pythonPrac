'''Problem statement#

Implement a class - Student - that has four properties and two methods. All these attributes (properties and methods) should be public. This problem can be broken down into three tasks.
Task 1#

Implement a constructor to initialize the values of four properties: name, phy, chem, and bio.
Task 2#

Implement a method – totalObtained – in the Student class that calculates total marks of a student.

Sample properties

name = Mark
phy  = 80
chem = 90 
bio  = 40

Sample method output

obj1.Total()=210

Task 3#

Using the totalObtained method, implement another method, percentage, in the Student class that calculates the percentage of students marks. Assume that the total marks of each subject are 100. The combined marks of three subjects are 300.

The formula for calculating the percentage is given below.

Percentage=Percentage=Percentage= MarksObtainedTotalMarks×100\frac{Marks\:Obtained}{Total \: Marks}\times100​TotalMarks​​MarksObtained​​×100

Sample input

phy  = 80
chem = 90 
bio  = 40

Sample output

70

Coding exercise#

Design a step-by-step algorithm before jumping to the implementation. This problem is designed for your practice, so initially, try to solve it on your own. If you get stuck, you can always refer to the solution provided in next lesson.

Good luck!
'''


class Student:
    def __init__(self,name,phy,chem,bio) :
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def Total(self):
        p = self.phy
        c = self.chem
        b = self.bio
        return (p+c+b)


    def Percentage(self ):
        return(self.Total()/300*100)


obj = Student("CR7" , 78,87,90)

print("Name: " , obj.name)
print("phy: " , obj.phy)
print("chem: ",obj.chem)
print("bio: ",obj.bio)
print(obj.Total())
print(obj.Percentage())