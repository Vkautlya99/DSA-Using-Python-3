# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
def Count_One(nums):
    count = 0
    maximum_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        maximum_count = max(maximum_count, count)
    return maximum_count


nums = [1, 1, 1, 1, 0, 0, 1, 1, 1]
print("The Number Of 1's in The Above List(Array) is :- ", Count_One(nums))
