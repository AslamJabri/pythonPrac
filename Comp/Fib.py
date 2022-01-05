def fib(n):
# starting the fibonacci numbers with 0 and 1
    first = 0
    second = 1

    if n == 1:
        return first
    if n == 2:
        return second
    if n < 0:
        return -1

    count =3
    while count <= n:
        #creating a variable and storing the sum of first and second number
        third = first+second
        first = second
        second = third
        count +=1
        print(third)
    return third
(fib (6))