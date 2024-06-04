# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Note: Start the array with positive elements.


def RearrangeElement(arr):
    positive = []
    negative = []

    for i in range(len(arr)):
        if arr[i] > 0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])
    for i in range(len(positive)):
        arr[2 * i] = positive[i]
    for i in range(len(negative)):
        arr[2 * i + 1] = negative[i]

    return arr


arr = [1, 2, -4, -5]
print(RearrangeElement(arr))
