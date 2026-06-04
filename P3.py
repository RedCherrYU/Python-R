
list3 = [1, 2, 3, 12, 14, 13, 8, 9]
a = 0

for i in range(len(list3)):
    a += list3[i]
    
print("Sum: ", a)
print("Average: ",a/len(list3))

b = list3[0]
c = list3[0]

for i in range(len(list3)):
    if b<list3[i]:
        b = list3[i]

print("Maximum: ", b)

for i in range(len(list3)):
    if c>list3[i]:
        c = list3[i]

print("Minimum: ", c)