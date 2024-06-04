# Q) Find The idex of an element in an array


def Linear_Search(my_list, target):
    for i, val in enumerate(my_list):
        if target == val:
            return i
    return -1


my_list = list(map(int, input().split()))
target = int(input("Enter the Digit :-- "))

print(Linear_Search(my_list, target))
