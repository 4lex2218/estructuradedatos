import math

def encontrar_primos():
    print("Buscador de Números Primos hasta N")
    
    try:
        n = int(input("Ingrese el valor de N: "))
    except ValueError:
        return "Error: Debe ingresar un número entero."

    if n < 2:
        return "No hay números primos menores que 2."

    primos = []

    for num in range(2, n + 1):
        es_primo = True
        
        limite = int(math.sqrt(num))
        
        for i in range(2, limite + 1):
            if num % i == 0:
                es_primo = False
                break
        
        if es_primo:
            primos.append(num)

    print(f"Números primos encontrados hasta {n}:")
    print(primos)
    return f"Total encontrados: {len(primos)}"


print(encontrar_primos())
