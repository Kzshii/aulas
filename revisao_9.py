Codigo = int(input('Insira um valor com 5 digitos: '))
A = Codigo//10000
B = Codigo//1000 - A*10
C = Codigo//100 - A*100 - B*10
D = Codigo//10 - A*1000 - B*100 - C*10
E = Codigo - A*10000 - B*1000 - C*100 - D*10
S = 6*A + 5*B + 4*C + 3*D + 2*E
DigitoV = S%7
print(DigitoV)
