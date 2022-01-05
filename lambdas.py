birth = lambda a , b : a[0] + b[0] 
print(birth("30" ,"40"))


cont = lambda num :  "high" if num > 50 else "low"
print(cont(49.99))


ch = lambda n1,n2 : (n1*n2) + (n1+n2)

def check(operation , n1 , n2):
    return operation(n1,n2)

result = check(ch,2,3)
print(result)

seq = [1,2,3,4,5,6,7,8,9]
even = filter(lambda num : num % 2 == 0 , seq )
print(even)

a = int(input(3))
b = int(input(3))
c = a+b
c1 = a-b
c2 = a*b
print(c)
print(c1) 
print(c2)