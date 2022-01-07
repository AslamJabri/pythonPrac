#create a global class 
# create two instance variables name and physical

class Players():
    teamname = "Real Madrid"
    teamMembers = []
    salary = 7000
    def __init__(self ,name ) :
        self.name = name
        self.position = []
        self.style = []
        self.teamMembers.append(self.name)
       

    def tax (self):
        return (self.salary * 0.2)
        
    def ato (self):
        return (self.salary *0.5/2)
    def salaryperday(self):
        return (self.salary/30 ) 
    def demo(self , a,b,c,d=5,e = None):
        print("a=" , a)
        print("b=" , b)
        print("c=" , c)
        print("d=" , d)
        print("e=",e)


p1 = Players("Cr7")
p1.position.append("striker")
p1.style.append("Ninja")
p1.tax()
p1.ato()
p1.salaryperday()

print("\n")
print("Name:" ,p1.name)
print("Position:" , p1.position)
print("Style:" , p1.style)
print("Team:" , p1.teamname)
print("Tax:" ,p1.tax())
print("ATO: ", p1.ato())
print("salary per day: " , p1.salaryperday())
p1.demo(1,2,3)

p2 = Players("Bale")
p2.position.append("Left Wing")
p2.style.append("Anchor")
print("Name:" ,p2.name)
print("Position:" , p2.position)
print("Style:" , p2.style)
print("Team:" , p1.teamname)
p2.demo(1,2,3,4)
p3 = Players("Rooney")
p3.position.append(" Forward")
p3.style.append("Python")
print("Name:" ,p3.name)
print("Position:" , p3.position)
print("Style:" , p3.style)
print("Team:" , p1.teamname)
p3.demo(1,2,3,4,5)
p4 = Players("Pele")
p4.position.append("Center Forward")
p4.style.append("Marksman")
print("Name:" ,p4.name)
print("Position:" , p4.position)
print("Style:" , p4.style)
print("Team:" , p1.teamname)

p5 = Players("Messi")
p5.position.append("Left Forward")
p5.style.append("Leader")
print("Name:" ,p5.name)
print("Position:" , p5.position , end= "\n")
print("Style:" , p5.style)
print("Team:" , p1.teamname)

print("TeamMembers" , p1.teamMembers)