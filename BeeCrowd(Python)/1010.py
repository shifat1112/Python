product1 = input().split(' ')
product2 = input().split(' ')
code1,unit1,price1 = product1
code2,unit2,price2 = product2
total = int(unit1)*float(price1) + int(unit2)*float(price2)
re = format(total, ".2f") 

print("VALOR A PAGAR: R$", re)