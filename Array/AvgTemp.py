numofdays = int(input("Enter The Number Of Days : "))
total = 0
temp = []
for i in range(numofdays):
    nextday = int(input("Day" + str(i + 1) + "'s Temprature  : "))
    temp.append(nextday)
    total += temp[i]

avg = round(total / numofdays, 2)
print("Average " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1
print(str(above) + " day(s) is above average")
