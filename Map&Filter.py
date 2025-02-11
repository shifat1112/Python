def square(x):
    y = x * x
    if y%2==0:
        return y

num = [1,2,3,4,5]

result = list(map(square, num))

#re = list(filter(lambda x: x%2==0, result))

#print(re)
print(result)