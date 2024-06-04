def Two_MaxNum_product(arr):
    max_num1, max_num2 = 0, 0
    for num in arr:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif num > max_num2:
            max_num2 = num

    return max_num1 * max_num2


arr = [1, 55, 67, 12, 45, 69, 87]
print(Two_MaxNum_product(arr))
