def Fibo(num):
    if num < 0:
        return False
    elif num == 1 or num == 2:
        return 1
    else:
        return Fibo(num - 1) + Fibo(num - 2)


num = 9
print(Fibo(num))


# Using Dynamic Programming
def Fib(number):
    a = 0
    b = 1

    for i in range(1, number):
        c = a + b
        a = b
        b = c
    return b


number = 9
print(Fib(number))
