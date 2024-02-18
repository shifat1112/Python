print("Marks")

a = int(input("Enter your mark: "))

if a<0 or a>100:
    print("Enter a valid mark between 0-100.")

elif a>=80:
    print("A+")
elif a>=70 and a<80:
    print("A")
elif a>=60 and a<70:
    print("B")
elif a>=50 and a<60:
    print("C")
elif a>=40 and a<50:
    print("D")
elif a<40:
    print("F")