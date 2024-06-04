# Linear Search to Find an element in an aaray if exist return true Otherwise False


def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "Element doesnot exist"


arr = [1, 7, 4, 2, 6, 9]
target = 2
print(Linear_Search(arr, target))


# Linear Search to Find index of an element in an aaray(Target)


def Linear_Search(arr, value):
    for elem in arr:
        if elem == target:
            return True
    return False


arr = [1, 7, 4, 2, 6, 9]
value = 4
print(Linear_Search(arr, value))
