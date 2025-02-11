def swap(c,d):
    temp = c
    c = d
    d = temp

    print("After Swapping: ", c,d)



a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("Before swapping: ", a, b)
swap(a,b)

