a = list(map(int, input("Enter numbers: ").split(' ')))
print(a)

b = set(a)
print(b)
b.remove(0)
print(b)