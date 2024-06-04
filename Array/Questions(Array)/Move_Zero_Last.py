def MoveZero(arr):
    non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero], arr[i] = arr[i], arr[non_zero]
            non_zero += 1
    for i in range(non_zero, len(arr)):
        arr[i] = 0


arr = [0, 2, 0, 4, 0, 6, 8, 10, 0, 12]
print("Original Array:", arr)

MoveZero(arr)

print("Array after moving zeros to the end:", arr)
