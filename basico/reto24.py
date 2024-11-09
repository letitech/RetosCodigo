#Encuentra el menor número en una lista
lista = [7, 9, 6, 87, 9]
menor = lista[0]

for i in lista:
    if menor > i:
        menor = i

print(menor)