primos=[]

for i in range(2,100,1):
    for j in primos:
        if i % j != 0:
            primos.append(i)


for num in primos:
    print(num)