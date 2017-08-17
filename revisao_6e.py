valor=float(input("Insira o valor da prestação: "))
taxa=float(input("Insira a porcentagem da taxa: "))
tempo=int(input("Insira o tempo de atraso: "))
print("O valor a ser pago é de",valor+(valor*(taxa/100))*tempo,"reais")
