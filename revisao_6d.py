tempo=int(input("Insira o tempo gasto em minutos: "))
velocidade=int(input("Insira a velocidade em KM/h: "))
distancia=(tempo/60)*velocidade
litros=distancia/12
print("O tempo gasto na viagem foi de {} horas \nA Velocidade foi de {} Km/h \nA distância foi de {} km \nA quantidade de combustivel gasto foi de {} litro".format(tempo/60, velocidade, distancia, litros))
