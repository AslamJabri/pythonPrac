def hello():
    print("This is a new function")


hello()

def cal(first , second):
    a= first+second
    b = first-second
    return a,b

result = cal(20,20)
print(result)

def show_employee(name , salary):
    if(salary < 9000):
        return 9000
    return salary , name

result = show_employee("sab" , 51000)
print(result)


grocery = "rice" 

def update_list(first , second):
    first = "cake"
    second = "butter"
    grocery = first , second
    print("the updated list of the groceries : " , grocery)
    return first , second


update_list(grocery , grocery)
print("This is my old list :" , grocery)



groc = ["rice" , "flour" , "cake"]
#print(groc)


def new_groc(grocery):
    grocery[0] = "maggie"
    grocery[1] = "hope"
    return grocery


print(groc)    
print(new_groc(groc))

# built in functions are used with the .find() and so on known as method.

stri = "Hello this is a find method"

print(stri.find("this"))
# this gives us the index of the string -1 refers to None.

print(stri.replace("Hello" , "Welcome"))
# replaces the hello to welcome

#lower and upper case

print(stri.upper())
print(stri.lower())


#joining the string
print("'".join(stri))
print(">>".join(stri))


#formatting the string

str1 = "Hello This is Python {version} and we are learning at {cname}".format(version = 1 , cname = "EduCative" )
print(str1)
str2 = "Hello This is Python {0} and we are learning at {1}".format(2,"eDucative")
print(str2)
str3 = "Hello This is Python {} and we are learning at {}".format(3 , "educative")
print(str3)


#lambdas syntax
    #lambda num : num * 20
triple = lambda num : num * 20
print(triple(20))

#lambdas can also be used in a if else statement.Note else has to be included.

triple1 = lambda num : "high" if num > 50 else "low"
print(triple1(42))

listt = lambda a,b,c : a[0]+b[0]+c[0]


print(listt("World", "Wide", "Web"))


# argument in  a function

# making a calculator

def multiply(n1,n2):
    return n1*n2
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2

def calc (operation , n1,n2):
    return operation(n1,n2)

print(calc(multiply,10,20))
print(calc(add,10,20))
print(calc(sub,10,20))
print(calc(divide,10,20))

# making the same function in a lambdas
print(calc(lambda n1 , n2 : n1 * n2 ,10,20))
print(calc(lambda n1 , n2 : n1 // n2 , 10,20 ))

#using map built in 
    # map(function , list)

lisstt = [1,2,3,4,5 , 26,21]
sq_list = map(lambda n : n*2 , lisstt)
print(list(sq_list))

#filter method
sq_list1 = list(filter(lambda n : n > 10 ,lisstt))
print(sq_list1)