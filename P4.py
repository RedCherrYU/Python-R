
list4 = [9, 8, 7, 4, 3, 2, 89]
evensum = 0
oddsum = 0

for i in range(len(list4)):
    if list4[i]%2 == 0:
        evensum += 1
    else:
        oddsum += 1

print("Number of even numbers: ", evensum)
print("Number of odd numbers: ", oddsum)
    