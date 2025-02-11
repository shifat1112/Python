pi = 3.14159

a, b, c = list(map(float, input().split( )))

tr= 0.5*a*c
circle = pi *c*c
tra = 0.5 *(a+b)*c
sq = b*b
rec = a*b
print("TRIANGULO:", format(tr, ".3f"))
print("CIRCULO:", format(circle, ".3f"))
print("TRAPEZIO:", format(tra, ".3f"))
print("QUADRADO:", format(sq, ".3f"))
print("RETANGULO:", format(rec, ".3f"))
