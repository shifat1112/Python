# 1*1 * 2*2 * 3*3 * 4*4 * ........... * n*n

n = int(input('Enter any number: '))
sum = 1
x = 0

for x in range(1, n+1, 1):
    print("The number is: ", x)
    sum = sum * x*x

print("Sum of the series is: ", sum)