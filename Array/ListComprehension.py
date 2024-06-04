my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for i in my_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)
# print(new_list)


# List Comprehension
list1 = [2, 6, 7, 8, 9, 5]
new_list1 = [i * 2 for i in list1]

# print(list1)
# print(new_list1)


lang = "Python"
lang_letter = [letters for letters in lang]

# print(lang)
# print(lang_letter)


# Conditional List Comprehension

Lis = [
    -1,
    2,
    3,
    -2,
    -5,
    5,
    6,
    7,
    8,
    -3,
    -5,
    -7,
]
the_list = [number for number in Lis if number >= 0]
neg_list_to_Pos = [number * number for number in Lis if number < 0]
print(the_list)
print(neg_list_to_Pos)
