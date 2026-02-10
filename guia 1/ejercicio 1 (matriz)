import random 

#importo el random de python para generar los números aleatorios y llenar la matriz

matriz = []
for i in range(10):
    fila = []
    for j in range(10):
        fila.append(random.randint(1, 100))
    matriz.append(fila)


print("Se desplegaran los elementos de la matriz al revés yendo del 9 al 0\n")

contador = 0

for i in range(9, -1, -1):
    #
    for j in range(9, -1, -1):
        elemento = matriz[i][j]
        print(f"Valor: {elemento} (Fila: {i}, Col: {j})")
        
        contador += 1
        
        
        if contador % 10 == 0:
            print(f"Salieron {contador} elementos de la matriz\n")
