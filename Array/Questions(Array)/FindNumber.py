def find_num(arr, target):
    for indx, val in enumerate(arr):
        if val == target:
            return indx
    return -1


arr = [3, 4, 6, 7, 89, 12, 34, 30]
target = 89
print(find_num(arr, target))
