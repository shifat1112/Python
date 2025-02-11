# 1 + 1/2 + 1/3 + 1/4 + ....... + 1/n

n = int(input("Enter the last number: "))

sum = 0
x = 0
for x in range(1, n+1, 1):
    print("The number is: 1/",x)
    sum = sum + 1/x

print("The sum is: ", sum)