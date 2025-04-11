#logica E (and)

verifica_Email = True
verifica_senha = False

verifica_Login = verifica_senha and verifica_Email
print(verifica_Login)

if(verifica_Login):
    print("Entra no sistema")

#Logica ou (or)

jogo_br = False
sol_dom = True

churrasco = jogo_br or sol_dom

if(churrasco):
    print("churrasco")

#operação Não (not)

negacao =  not False
print(negacao)
