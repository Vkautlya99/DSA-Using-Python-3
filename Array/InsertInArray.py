import array

my_arr1 = array.array("i", [1, 22, 30, 45, 60])  # O(N)
print(my_arr1)


# Inserting Element With Index

my_arr1.insert(0, 0)
print(my_arr1)


# Random Inserting

my_arr1.append(70)
print(my_arr1)


# Time Complexity =  O(N)
# Space Complexity = O(1)
