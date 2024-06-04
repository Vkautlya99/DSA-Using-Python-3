# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.
def majorityElem(arr):
    n = len(arr)
    # count = 0      It's Wrong

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1

        if count > (n // 2):
            return arr[i]

    return "No Any Number Found That is Greater N//2"


arr = [4, 4, 2, 4, 3, 4, 0, 3, 2, 0]
arr1 = [4, 4, 2, 4, 3, 4, 4, 3, 2, 4]
print(majorityElem(arr))  # No Any Number Found That is Greater N//2
print(majorityElem(arr1))  # 4
