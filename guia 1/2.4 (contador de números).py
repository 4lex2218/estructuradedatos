def contar_numeros():
    print("--- Lector de Números (Ingresa 0 para detener) ---")
    
    contador = 0
    # entramos con algo que no sea cero para entrar al bucle
    numero = None 
    
    while numero != 0:
        # pedimos el numero al usuario
        entrada = input("Ingresa un número (o 0 para salir): ")
        
        # la entrada la convertimos a entero
        numero = int(entrada)
        
        if numero != 0:
            print(f"Número leído: {numero}")
            contador += 1  # usamos un contador
            
    return f"Total de valores leídos (sin contar el cero): {contador}"


print(contar_numeros())
