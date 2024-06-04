# Q)1 Find index Two numbers whose sum is equals to the guven target value


def pairsSum(arr, nums):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == nums:
                return [i, j]
    return []


arr = [3, 2, 4, 7, 6, 5, 8, 1, 9]
nums = 9
print(pairsSum(arr, nums))


# Q)2 Find Two numbers whose sum is equals to the guven target value
def TwoSumNum(myarr, target):
    res = []
    for i in range(len(myarr)):
        for j in range(i + 1, len(myarr)):
            if myarr[i] + myarr[j] == target:
                res.append(f"{myarr[i]} + {myarr[j]}")
    return res


myarr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7
print(TwoSumNum(myarr, target))
