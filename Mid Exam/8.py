a = [1,2,5]
b = [2, 5, 8]
c = []
for x in range(len(a)):
    for y in range(len(b)):
        if a[x] == b[y]:
            c.append(b[y])

print(c)

