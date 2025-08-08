# criando matriz 4x5 com numeros de 1 a 20

qtd_linhas = 4
qtd_colunas= 5
matriz = []

numero=1

for i in range(qtd_linhas):
    linha=[]
    for j in range(qtd_colunas):
        linha.append(numero)
        numero += 1
    matriz.append(linha)

#exibindo matriz
for linha in matriz:
     print(linha)