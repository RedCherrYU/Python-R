
list6 = [10, 2, 32, 46, 7, 5, 83]
flag = True
a = 0

num = int(input("Enter a number:"))

for i in range(len(list6)):
    if num == list6[i]:
        flag = False
        a = i

if flag == False:
    print("Number matched at index ", a)
else:
    print("No match!")

