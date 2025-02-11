def add():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    sum = a + b
    print("Summation is: ", sum)

def sub():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    sub = a - b
    print("Subtraction is: ", sub)

def mul():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    mu = a * b
    print("Multiplication is: ", mu)

def div():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    di = a / b
    print("Division is: ", di)

def mod():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    mo = a % b
    print("Modulus is: ", mo)
i = 0
while i<7:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    n = int(input("Enter your choice: "))

    if n==1:
        add()
    elif n==2:
        sub()
    elif n==3:
        mul()
    elif n==4:
        div()
    elif n==5:
        mod()
    else:
        print("Enter your valid choice")

    i = i+1