# WAP to arrange the list in Decending order using ubble Sort
def Solve(string):
    my_str = list(string)
    n = len(my_str)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_str[j] < my_str[j + 1]:
                my_str[j], my_str[j + 1] = my_str[j + 1], my_str[j]

    return my_str


string = "csiplearninghub"
print(Solve(string))
