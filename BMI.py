print("BMI Calculator\n")

h = float(input("Enter your height(in meters): "))
w = float(input("Enter your weight(in kgs): "))

BMI = w / (h*h)

if h<=0 and w<=0:
    print("Enter valid input.")

    a = float(input("Enter your height(in meters): "))
    b = float(input("Enter your weight(in kgs): "))

    BMI = b / (a*a)

    print("BMI Category: ", end='')
    if  BMI < 18.5:
        print("Under Weight")
    elif  18.5 <= BMI < 25:
        print("Normal Weight")
    elif  25 <= BMI < 30:
        print("Over Weight")
    elif  BMI >= 30:
        print("Obese")
else:

    print("BMI Category: ", end='')
    if  BMI < 18.5:
        print("Under Weight")
    elif  18.5 <= BMI < 25:
        print("Normal Weight")
    elif  25 <= BMI < 30:
        print("Over Weight")
    elif  BMI >= 30:
        print("Obese")
    else:
        print("Enter valid input.")
