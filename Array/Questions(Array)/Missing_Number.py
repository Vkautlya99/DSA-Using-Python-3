# Find the Missing Number in an Array


def Missing_num(arr, n):
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    Missing_num = total_sum - actual_sum

    return Missing_num


n = int(input())
arr = list(map(int, input().split()))

print(Missing_num(arr, n))
