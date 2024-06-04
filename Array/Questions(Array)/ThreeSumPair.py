# Find Three numbers whose sum is equals to the guven target value


def ThreeSum(arr, targetSum):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == targetSum:
                    return [i, j, k]
    return []


arr = [3, 2, 4, 7, 6, 5, 8, 1, 9]  # for UserInput :- list(map(int,input().split()))
targetSum = 21
print(ThreeSum(arr, targetSum))
