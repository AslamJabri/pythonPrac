def fib(n):
    a =0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    if n < 0:
        print(-1)

    count = 3
    while count <= n:
        c = a + b
        a = b
        b = c
        count += 1
        print(c)
    return c



fib(15)