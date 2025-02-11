a = list(map(int, input().split()))
c = []
b = len(a)

if b<2:
    print("Not Possible.")
else:
    """for x in range(2, b):
        c.append(x)
    print(c)"""
    print(a[1:-1])