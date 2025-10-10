t = ('a', 'b')
print(t)

t_unica = "a"
print(type(t_unica))

t= tuple("fiap")
print(t)

a=5
b=10
print(f"a{a}, b{b}")

a,b = b,a
print(f"a{a}, b{b}")


#recebe um email "rm123456@fiap.com.br"
#separar  o email entre usuario e dominio
email = "rm123456@fiap.com.br"
usuario, dominio = email.split("@")
print(usuario)
print(dominio)