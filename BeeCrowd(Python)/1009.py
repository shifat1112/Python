name = input()
salary = float(input())
sold = float(input())
sa = format(salary, ".2f")
if sold>0:
    result = salary + (sold*.15)
    re = format(result, ".2f")
    print("Total = R$", re)
else:
    print("Total = R$",sa)