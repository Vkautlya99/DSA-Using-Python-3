# Write A programm in Python and Return True if the array contains duplicate elements in python


# Method :- 1
class Solution:
    def Duplicate(arr):
        set_items = set()
        for num in arr:
            if num in set_items:
                return True
            set_items.add(num)
        return False


# sol = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = Solution.Duplicate(arr)
print(res)


# Method :- 2
def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True  # For returning The Number : (return arr[i] or arr[j])
        return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(duplicate(arr))
