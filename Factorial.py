# 3! = 3*2*1 = 6

n = int(input("Enter any number: "))
fact = 1
for x in range(1, n+1, 1):
    fact = fact*x
print("The factorial of the number is: ", fact)