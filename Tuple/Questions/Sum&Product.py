# Find The Sum and Product in A Tuple


def sum_product(tup):
    sum_result = 0
    product_result = 1
    for num in tup:
        sum_result += num
        product_result *= num

    return sum_result, product_result


tup = (1, 2, 3, 4, 5)
sum_result, sum_product = sum_product(tup)
print(sum_result, sum_product)
