list7 = [1, 2, 3, 4, 1, 2, 2, 4]
a = 0
count = 1

for i in range(len(list7)):
    a = list7[i]
    for j in range(2, len(list7)):
        if a == list7[j]:
            count += 1
            print(a, " -> ", count)

for i in range(len(list7)):
    a = list7[i]
    
        