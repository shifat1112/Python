print("Shopping Discount Calculator\n")

a = float(input("Enter total purchase amount: "))

if a<=0:
    print("Enter the correct purchase amount.")
elif 100<a<=200:
    print("Total cost after discount: $",  (a-(a*.1)))
elif 200<a<=300:
    print("Total cost after discount: $", (a-(a*.2)))
elif a>300:
    print("Total cost after discount: $", (a-(a*.3)))
else:
    print("Total cost after discount: $", a)