'''
#Exercício em dupla até o #5
#Autores: Daniel Patricio e Ramon Kazushi
#1. Ler dois valores numéricos inteiros e apresentar o resultado da diferença
#do maior pelo menor valor.
a = int(input("insira o valor: "))
b = int(input("insira o valor: "))
if b<a:
	print(a/b)
else:
	print(b/a)
'''
'''
#2. Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número
#lido como sendo um valor positivo, ou seja, o programa deverá apresentar o módulo
#de um número fornecido. Lembre-se de verificar se o número fornecido é menor que
#zero; sendo, multiplique-o por –1.
a=int(input("Insira um valor: "))
if a<0:
	print(a*(-1))
else:
	print(a)
'''
'''
#3. Ler quatro valores referentes a quatro notas escolares de um aluno e escrever uma
#mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou
#igual a 7. Se o aluno não for aprovado indicar uma mensagem informando esta condição.
#Apresentar junto das mensagens o valor da média do aluno para qualquer condição. 
a=float(input("Insira o valor da primeira nota: "))
b=float(input("Insira o valor da segunda nota: "))
c=float(input("Insira o valor da terceira nota: "))
d=float(input("Insira o valor da quarta nota: "))
media=(a+b+c+d)/4
if media>=7:
	print("Aprovado, sua média é",media)
else:
	print("Aluno reprovado. Sua média foi de",media)
'''
'''
#4. Ler quatro valores referentes a quatro notas escolares de um aluno e escrever
#uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for
#maior ou igual a 7. Se o valor da média for menor do que 7, solicitar a nota de
#exame, somar com o valor da média e obter nova média. Se a nova média for maior
#ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado
#em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta
#condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição.
a=float(input("Insira o valor da primeira nota: "))
b=float(input("Insira o valor da segunda nota: "))
c=float(input("Insira o valor da terceira nota: "))
d=float(input("Insira o valor da quarta nota: "))
media=(a+b+c+d)/4

if media>=7:
	print("Aluno aprovado! Sua média foi",media)
else:
	print("Média",media)
	e=float(input("Insira o valor do exame: "))

novaMedia=(media+e)/2

if novaMedia>=5:
	print("Aluno aprovado em exame. Média é",novaMedia)
else:
	print("Aluno reprovado em exame. Média é",novaMedia)
'''
'''
#5. Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo
#da equação completa de segundograu, apresentando as duas raízes, se para os
#valores informados for possível efetuar o referido cálculo. Lembre-se de que a
#variável A deve ser diferente de zero. 
a = float(input("Digite um valor diferente de zero:" ))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))
delta = (b**2)-(4*a*c)
bas1 = -b+(delta**(1/2))/(2*a)
bas2 = -b-(delta**(1/2))/(2*a)
print("As raízes da equação são %.2f e %.2f " % (bas1,bas2))
'''
'''
#6.   Efetuar a leitura de três valores (variáveis A, B e C) e apresenta-los dispostos em ordem crescente. Para
#solucionar o problema, utilizar os conceitos da propriedade distributiva e troca de valores entre variáveis. 

def main(args):
	a=int(input("Insira um número: "))
	b=int(input("Insira um número: "))
	c=int(input("Insira um número: "))
	if a<b and a<c:
		if c<b:
			c,b=b,c
	elif b<a and b<c:
		a,b=b,a
		if (c<b):
			b,c=c,b
	else:
		a,c=c,a
		if c<b:
			b,c=b,c
	print(a,b,c)
	
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
'''
#7.Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis, ao mesmo tempo,
#por 2 e 9.

def main(args):
	a=int(input("Insira um número: "))
	b=int(input("Insira um número: "))
	c=int(input("Insira um número: "))
	d=int(input("Insira um número: "))

	if a%2==0 and a%9==0:
		print(a,"é um número divisível por 2 e 9")
	if b%2==0 and b%9==0:
		print(b,"é um número divisível por 2 e 9")
	if c%2==0 and c%9==0:
		print(c,"é um número divisível por 2 e 9")
	if d%2==0 and d%9==0:
		print(d,"é um número divisível por 2 e 9")
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
'''
#8. Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valor.
def main (args):
	a=int(input("Insira um valor: "))
	b=int(input("Insira um valor: "))
	c=int(input("Insira um valor: "))
	d=int(input("Insira um valor: "))
	e=int(input("Insira um valor: "))
	if a<b and a<c and a<d and a<e:
		if b<c and c<d:
			print (a,d)
	if b<c and b<d and b<a
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
'''#9. Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem informando
#se o número é par ou ímpar.

def main (args):
	a=int(input("Insira um número: "))
	if a%2==0:
		print("O número é par")
	else:
		print("O número é ímpar")
	return 0 
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
'''
#10. . Elaborar um programa que efetue a leitura de um valor que esteja entre a faixa de 1 a 9. Após a leitura
#do valor fornecido pelo usuário, o programa deverá indicar uma de duas mensagens: “O valor está na faixa
#permitida”, caso o usuário forneça o valor nesta faixa, ou a mensagem “O valor está fora da faixa permitida”,
#caso o usuário forneça valores menores que 1 ou maiores que 9.

def main(args):
	a=int(input("Insira um valor: "))
	if a>1 and a<9:
		print("O valor estã na faixa permitida")
	else:
		print("O valor está fora da faixa permitida")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
'''
#11.  Elaborar um programa que efetue a leitura de um número inteiro e efetue a sua apresentação, caso o
#valor não seja maior que três. 
def main (args):
	a=int(input("Insira um valor: "))
	if a<3:
		print("O valor é",a)
	else:
		print("")
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
'''
#12. Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário
#escrever NÃO É MAIOR QUE 10!
def main (args):
	a=int(input("Insira um valor: "))
	if a>10:
		print("Valor maior que 10")
	else:
		print("Valor não é maior que 10")
	return 0
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
'''
'''
#13.Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)
def main (args):
	a=int(input("Insira um valor :"))
	if a>0:
		print("Valor positivo")
	else:
		print("Valor negativo")
	return 0
if __name__=='__main__':
	import sys
	sys.exit(main(sys.argv))
'''
'''
#14. . As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas
#pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total
#da compra.
def main (args):
	a=int(input("Insira a quantidade de maças a serem compradas "))
	b=1
	c=1.3
	if a<12:
		print("A quantidade de maças é {} e o valor é {}".format(a,(a*c)))
	else:
		print("A quantidade de maças é {} e o valor é {}".format(a,(a*b)))
	return 0
if __name__=='__main__':
	import sys
	sys.exit(main(sys.argv))
'''
#15.Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma
#mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é
#aprovado). Escrever também a média calculada.
def main (args):
	a=float(input("Insira o valor da primeira avaliação: "))
	b=float(input("Insira o valor da segunda avaliação: "))
	media=(a+b)/2
	if media >=6:
		print("Aluno aprovado! Média",media)
	else:
		print("Aluno reprovado! Média",media)
	return 0
if __name__=='__main__':
	import sys
	sys.exit(main(sys.argv))
