# Find That Two List contains the equal and similar elements


def Permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


list1 = [1, 22, 44, 55]
list2 = [44, 22, 55, 1]
print(Permutation(list1, list2))
