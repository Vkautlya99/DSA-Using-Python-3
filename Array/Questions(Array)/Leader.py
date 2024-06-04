# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.


def printLeaders(arr, n):
    ans = []

    # Last element of an array is always a leader,
    # push into ans array.
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.insert(0, arr[i])
            max_elem = arr[i]

    return ans[i]


n = 6
arr = [10, 22, 12, 3, 0, 6]
print(printLeaders(arr, n))
# ans = printLeaders(arr, n)

# for i in range(len(ans) - 1, -1, -1):
#     print(ans[i], end=" ")

# print()
