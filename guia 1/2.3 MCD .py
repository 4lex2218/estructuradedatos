def calcular_mcd(a, b):
    print(f"Calculando MCD de {a} y {b}")
    
    # usamos numeros positivos
    a = abs(a)
    b = abs(b)
    
    # identificamos el mayor y el menor
    mayor = max(a, b)
    menor = min(a, b)
    
    while menor != 0:
        resto = mayor % menor
        print(f"Dividiendo {mayor} entre {menor}, el resto es: {resto}")
        
        # El divisor pasa a ser el dividendo (el mayor)
        # El resto pasa a ser el divisor (el menor)
        mayor = menor
        menor = resto
        
    return f"El último divisor (MCD) es: {mayor}"

# se le pueden cambiar los valores a los que se les va a calcular el MCD
print(calcular_mcd(48, 18))
