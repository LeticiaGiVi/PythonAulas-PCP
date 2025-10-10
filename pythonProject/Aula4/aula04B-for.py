qtd_pordutos = int(input("Digite a quantidade de produtos"))

for cp in range(qtd_pordutos):
    print("produto", cp)

#De 2 a 10
for i in range(2,10):  #não conta o ultimo intervalo, mostra do um ao 9
     print(i)

# de 2 a 10, pulando de 2 em 2
for i in range(2,11,2):
    print(i)

# for aninhado - repetição encadeada
for i in range(0,4):     #vai de 0 A 3(4 NÃO INCLUSO)
    for j in range(2,5):     #vai de 2 A 4(5 NÃO INCLUSO)
        print(i,j)