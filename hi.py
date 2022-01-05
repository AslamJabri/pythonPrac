n = 25
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n < 5:
    print("Not Weird")
elif n %2 ==0 and range(6,20):
    print("Weird")
elif n % 2 == 0 and n > 20 :
    print("Not Weird")


for i in range(1,10):
    if i % i == 0 :
        print(i)
    else:
        print("odd")

heel = "Hello"
for i in heel:
    print (list(i*2))


ch = 2
power = 0
val = ch
while val < 2000:
    power += 1
    val *= ch
print(power)


brackets = "[[[[]]]]]]"

def check_brackets(brackets):
    check = 0
    for bracket in brackets:
        if bracket == "[":
            check += 1
        elif bracket == "]":
            check -= 1
        
        if check < 0:
            break
    return check == 0


print(check_brackets(brackets))

num_list = [10, -14, 26, 5, -3, 13, -5]


def check_sum(num_list):
    for num1 in  range (len(num_list)):
        for num2 in range (num1 , len(num_list)):
            if num_list[num1] + num_list[num2] == 0:
                return True
    return False
       


print(check_sum(num_list))


def fib(n):
    a = 0
    b = 1

    if n < 0:
        return -1
    if n == 1:
        return a
    if n == 2:
        return b
    
    count = 3

    while count <= n:
        c = a + b
        a = b
        b = c
        count += 1
        print(c)
    return c
    
print(fib(15))