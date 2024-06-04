# Find that an Array is Sorted or Not


def sortedArray(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                return True
    return False


arr = [1, 2, 3, 4, 5]
n = len(arr)
ans = sortedArray(arr, n)
if ans:
    print("True")
else:
    print("False")
