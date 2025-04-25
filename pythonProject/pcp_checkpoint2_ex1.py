codigoEstado = int(input("digite o valor do codigo da origem da carga: (1 a 5)"))
pesoT = float(input("digite o peso da carga em toneladas: "))
codigoCarga = int(input("digite o codigo da carga(de 10 a 40): "))

pesoKg = pesoT * 1000
precoCarga = 0
precoimposto = 0

if (codigoCarga > 10 and codigoCarga <= 20):
    precoCarga = pesoKg * 100
elif(codigoCarga >= 30):
    precoCarga = pesoKg * 250
else:
    precoCarga = pesoKg * 340

print(f"O valor da carga sem imposto é: {precoCarga}")

if codigoEstado == 1:
    precoimposto = precoCarga * 0.35
elif codigoEstado == 2:
    precoimposto = precoCarga * 0.25
elif codigoEstado == 3:
    precoimposto = precoCarga * 0.15
elif codigoEstado == 4:
    precoimposto = precoCarga * 0.05
else:
    precoimposto = precoCarga * 0

print(f"O valor do imposto é: {precoimposto}")
print(f"O valor transrportado pelo caminhão é: {precoCarga + precoimposto}")



