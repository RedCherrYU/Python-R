list7 = [1, 2, 3, 4, 1, 2, 2, 4]
a = 0
count = 1

for i in set(list7):
    a = i
    count = 1
    for j in range(i+1, len(list7)):
        if a == list7[j]:
            count += 1
    print(a, " -> ", count)

        