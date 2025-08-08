#validação de entrada

n = 0
while n<= 0:
    n = int(input("digite um numero inteiro positivo: "))

#calculo da soma

soma = 0

for i in range(1, n+1, 1):
    soma += i
 #exibição do resultado

print (f"A soma de 1 até {n} é: {soma}")