eng2sp = dict()

eng2sp['one'] = "uno"
print(eng2sp)

eng2sp = {
    "one": "uno",
    "two": "dos",
    "three": "tres"
}
print(eng2sp)

print(eng2sp["two"]) #chave que acesa um valor
# print(eng2sp["dos"]) é um valor e não tem chave, resulta em erro

print(len(eng2sp))

#operador in
print("one" in eng2sp) #true
print("uno" in eng2sp)#false

print("tres" in eng2sp.values())#true

#Contador de letras
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c] +=1
    return d

retorno = count_letters("fiapp")
print (retorno)
