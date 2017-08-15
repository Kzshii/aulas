N=int(input('Insira um número de 3 algarismos: '))
C = N//100
D = N//10 - C*10
U = N - C*100 - D*10
print('O inverso deste número é: ',U,D,C)
