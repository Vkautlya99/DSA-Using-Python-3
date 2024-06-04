def bestScore(arr):
    max1, max2 = float("-inf"), float("-inf")
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2


arr = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(bestScore(arr))
