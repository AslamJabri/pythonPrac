class first:
    pass

obj = first()
print(obj)

class Employee():
    ID = None
    salary = None
    Department = None

Aslam = Employee()

Aslam.ID = 123
Aslam.salary = 1000000
Aslam.Department = "SDE"
Aslam.company = "Google"

print("ID" , Aslam.ID)
print("salary" , Aslam.salary)
print("Department" , Aslam.Department)
print("company" , Aslam.company)


class employee():
    def __init__(self,Id,salary,department) :
        self.Id = Id
        self.salary = salary
        self.department = department


Steve = employee(456,3000,"Engg")
Steve.company = "Google"

print(Steve.company)