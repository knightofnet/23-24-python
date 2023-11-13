numeros = [543,318,68,54,597]
print(len(numeros))
print(numeros[1])

for x in numeros :
    x+=1
print(numeros)

for i in range(len(numeros)) :
    numeros[i]+=1
print(numeros)

numeros.append(745)
numeros.insert(len(numeros), 745)
numeros.extend([745])