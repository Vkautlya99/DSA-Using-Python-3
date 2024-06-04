def UniqueChar(string):
    my_str = set(string)
    return len(my_str)


string = input()
print(UniqueChar(string))
