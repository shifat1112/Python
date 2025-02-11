n1 = {1,2,3,4}
n2 = set([4,5,6])

n1.add(8)
n2.remove(4)

print(2 in n1)
print(2 in n2)
print(7 not in n1)
print(5 not in n2)
print(n1 | n2)
print(n1 & n2)
print(n1 - n2)