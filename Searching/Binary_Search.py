# Implement Binary_Search To finf the index of a given target Value


def Binary_Search(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    mid = (left + right) // 2

    while not (arr[mid] == target):
        if arr[mid] > target:
            right -= 1
        else:
            left += 1
        mid = (left + right) // 2
        print(left, mid, right)
    return mid


arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 7
print(Binary_Search(arr, target))
