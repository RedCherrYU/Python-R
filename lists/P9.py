A = [1 ,2 ,3]
B = [4 ,5 ,6]
list9 = []

for i in range(len(B)):
    list9.append(B[i])

for i in range(len(A)):
    list9.append(A[i])

print(list9)

list = []

list.extend(A)
list.extend(B)

print(list)

list0 = A+B

print(list0)
    
