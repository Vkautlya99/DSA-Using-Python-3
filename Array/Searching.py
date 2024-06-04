my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 36, 22, 30, 78, 67, 56, 45]

target = int(input("Enter The Digit : "))

# If we are using in operator than the Time complexity becomes O(n)
# if target in my_list:
#     print(f"{target} is in My_list ")
# else:
#     print(f"{target} is not in the My_list ")


# Linear Search


# Q) Find The idex of an element in an array
def linear_search(list, p_target):
    for i, val in enumerate(list):
        if val == p_target:
            return i
    return -1


print(linear_search(my_list, target))
