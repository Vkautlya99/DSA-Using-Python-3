# WAP to arrange the list in Ascending order using ubble Sort


def Ascending_Order(Arr):
    n = len(Arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if Arr[j] > Arr[j + 1]:
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
    return Arr


Arr = [23, 34, 54, 2, 12, 28]
print(Ascending_Order(Arr))
