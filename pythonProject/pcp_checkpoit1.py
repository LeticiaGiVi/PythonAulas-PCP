#exercicio 1

valor = float(input("digite o valor que voce quer converter (em reais): "))

dolar = valor / 5.9
euro = valor / 6.62
peso = valor / 181.8
libra = valor / 7.68
iene = valor / 24.5

print ("Valor em real: ", round(valor, 2))
print ("Valor em Dólar Americano: ", round(dolar, 2))
print ("Valor em Euro: ", round(euro, 2))
print ("Valor em Peso Argentino: ", round(peso, 2))
print ("Valor em Libra Esterlina: ", round(libra, 2))
print ("Valor em Iene: ", round(iene, 2))


#exercicio 2

num1 = int(input("digite o valor (entre 1 e 999): "))

if (num1 > 0 & num1 < 1000):
    centena = num1 // 100
    restocem = num1 % 100
    dezena = restocem // 10
    unidade = restocem % 10
    print("Centena: ",centena)
    print("dezena: ", dezena)
    print('unidade: ',unidade)

else:
    print("o numero não pode ser calculado")



#exercicio 3

anos = int(input("digite quantos anos você tem: "))
meses = int(input("digite quantos meses você tem: "))
dias = int(input("digite quantos dias você tem: "))

anosemdias = anos * 365
mesesemdias = meses * 30

print ("você já viveu ", anosemdias+mesesemdias+dias, "dias")

#exercicio 4
diasTotal = int(input("digite quantos dias você já viveu: "))

diasEmAnos = diasTotal // 365
restoAnos = diasTotal % 365
diasEmMeses = restoAnos // 30
diasEmDias = restoAnos % 30

print ("você já viveu ",diasEmAnos, " anos ", diasEmMeses, " meses e ",diasEmDias , " dias")