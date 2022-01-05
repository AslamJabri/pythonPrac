print("Hello",end="")
print("World")
print(complex(10,20))

random_String= "Hello This is a String"
print(random_String)

#gets the length of the string
print(len(random_String))

#accessing the string
print(random_String[4])

#keyword none
sal= None
print(type(sal))

#Inserting Strings Within a String
val = "I like this %s" %"python"
print(val)

#Inserting Integer Within a Integer
num = "%i + %i = %i" % (2,3,5)
print(num)

#Inserting Integer Within a Integer
float = "%.002f" % (2.5567)
print(float)

#search in string
stri = "Hello This is AJ"
print("is" in stri)
print("of" in stri)

#grouping all the values in a string

group = [3,5.6,"hello"]
print(len(group[2]))
print(len(group))

my_string = "0123456789"
print(my_string[-2: -6 : -2])