cp = 0
while cp < 3:
    print("produto",cp)
    cp = cp + 1

cp = 4
while cp >= 0:
    print("produto", cp)
    cp = cp - 1

jogar= "sim"
while jogar.lower() == "sim":
    print("Repete ou iniciar o jogo")
    jogar = input("deseja jogar novamente?")

i = 0
while i < 10:
    i += 1
    if i == 3 or i==5:
        continue

    if i == 7:
        break

    print("produto", i)
