#-----------------------------------------
# Condicional Simples
#----------------------------------

nota = 7

if(nota>6):
    print(f"sua not é {nota}")

print("FIM")


# -----------------------------------------
# Condicional Composta
# ------------------------------------

nota = 7

if(nota>6):
    print(f"sua not é {nota}, voce esta aprovado")
else:
    print(f"sua not é {nota}, voce esta reprovado")


print("FIM")


# -----------------------------------------
# Condicional Encadeada
# ------------------------------------

nota = 7

if (nota <4):
    print(f"sua not é {nota}, voce esta reprovado")

else:
    if(nota<6):
        print(f"sua not é {nota}, voce esta em recuperação")

    else:
        print(f"sua not é {nota}, voce esta aprovado")


print("FIM")


# -----------------------------------------
# Condicional Composta V2
# ------------------------------------

nota = 7

if (nota < 4):
    print(f"sua not é {nota}, voce esta reprovado")

elif (nota < 6):
    print(f"sua not é {nota}, voce esta em recuperação")

else:
    print(f"sua not é {nota}, voce esta aprovado")

print("FIM")
