def greet(fx):
    def mfx(*args, **kwargs):
        print("Hey sir !")
        fx(*args, **kwargs)
        print("Thanks for using me")
    return mfx

def calculate(a,b,c):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    n = int(input("Enter choice: "))

    if n == 1:
        print("Sum is: ", a+b+c)
    elif n==2:
        print("Sub is: ", a-b-c)
    elif n==3:
        print("Mul is: ", a*b*c)

greet(calculate)(10,20,30)