def Bubble_Sort(arr, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


n = 5
arr = [2, 4, 8, 1, 9]
print(Bubble_Sort(arr, n))
