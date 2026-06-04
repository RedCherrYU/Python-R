
list5 = []
list = []
length = int(input(f"Enter the desired length of list: "))

for i in range(length):
    a = int(input(f"Enter the list elements:"))
    list5.append(a)

for i in range(len(list5)):
    if list5[i]%2 == 0:
        list.append(list5[i])

print(list)