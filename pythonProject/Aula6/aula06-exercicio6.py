n = 0
while n<= 0:
    n = int(input("digite um numero de posições do vetor: "))

#Criação e preenchimento do vetor de caracteres
vetor = []
print("digite os caracteres (um por vez): ")
for i in range(n):
    caractere = input(f"Caractere da posição {i}: ")
    vetor.append(caractere)

#Exibição do vetor original
print(f"\nVetor original: {vetor}")

#inversão manual
for i in range(n//2):
    temp = vetor[i]
    vetor[i]= vetor[n-1-i]
    vetor[n-1-i]= temp

#Exibição do vetor invertido
print(f"\nVetor invertido: {vetor}")