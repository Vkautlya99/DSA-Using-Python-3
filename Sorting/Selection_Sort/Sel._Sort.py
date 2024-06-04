def Selection_Sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


arr = [2, 9, 3, 7, 6, 1, 5]
print(Selection_Sort(arr))
