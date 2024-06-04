def Arm_strong(num):
    s = num
    l = len(str(num))
    sums = 0

    while num != 0:
        r = num % 10
        sums = sums + (r**l)
        num = num // 10

    if s == sums:
        return "It's an Arm Strong Number"
    else:
        return False


num = int(input())
print(Arm_strong(num))
