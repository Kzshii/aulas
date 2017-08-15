HT = int(input('Insira a quantidade de horas trabalhadas: '))
VH = int(input('Insira o valor das horas trabalhadas: '))
PD = float(input('Insira o percentual de desconto: '))
SB = HT*VH
TD = (PD/100)*SB
SL = SB-TD
print('O total de horas trabalhadas e {}, o Salário bruto é {}, o total de desconto é {} e o Salário Líquido é {}'.format(HT,SB,TD,SL))
