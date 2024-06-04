def Arm_Strong(num, n):
    num_str = str(num)

    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
    if sum == num:
        return "Yes Number is an Arm Strong Number"
    else:
        return "No, Number is an Arm Strong Number"


n = int(input())
num = int(input())
print(Arm_Strong(num, n))
