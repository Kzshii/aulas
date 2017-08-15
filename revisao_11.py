data = int(input('Digite a data do seu aniversário: '))
DD = data//10000
MM = data//100 - DD*100
AA = data - DD*10000 - MM*100
print(AA,MM,DD)
