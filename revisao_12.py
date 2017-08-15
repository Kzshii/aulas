matricula = int(input('Insira aqui a sua matricula: '))
AA = matricula//100000
S = matricula//10000 - AA*10 
print('O ano matriculado é {} e o semestre é o {}'.format(AA,S))
