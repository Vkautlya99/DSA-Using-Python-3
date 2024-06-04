# Iterative Approach


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


n = 5
print(factorial(n))


# Using Recursion
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)


num = 5
print(fact(num))
