#Imprime la tabla de multiplicar de un número dado

numero = int(input("Introduce un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")