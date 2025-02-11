def prime(a):
    count = 0
    for x in range(2, int((a+1)/2)):
        if a%x == 0:
            count += 1
    
    if count == 0:
        print("prime")
    else:
        print("Not Prime.")


n = int(input("Enter a number: "))
prime(n)