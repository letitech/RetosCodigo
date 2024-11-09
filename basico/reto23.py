#Encuentra el mayor número en una lista
lista = [4, 5, 8, 32, 9, 7, 75]
mayor = lista[0]

for i in lista:
    if mayor < i:
        mayor = i
        
print(mayor)