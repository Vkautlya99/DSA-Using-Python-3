# Find The Largest Element in An Array


# Method :- 1
def LargestElem(arr):
    arr.sort()
    return arr[-1]


arr = [3, 4, 1, 22, 45, 67, 7, 6, 5, 11]
# print(LargestElem(arr))


# Method :- 2
def Largestelement(arr, n):
    largest_num = arr[0]

    for num in arr:
        if num > largest_num:
            largest_num = num
    return largest_num


n = int(input())
arr = list(map(int, input().split()))
print(Largestelement(arr, n))
