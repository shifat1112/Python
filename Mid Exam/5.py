def mark(a,b):
    if b>3.50:
        return float(a - (a*.2))
    elif 3.00<=b<=3.50:
        return float(a - (a*.1))
    elif 0<=b<3.00:
        return float(a - (a*.05))
    else:
        return "Enter correct cgpa."


fee = int(input("Enter the semester fee: "))
result = float(input("Enter the result: "))

print(mark(fee, result))