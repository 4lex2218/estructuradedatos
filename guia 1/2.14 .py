def contar_letras():
    print("Contador de Frecuencia de Letras")
    
    palabra = input("Ingrese una palabra: ")
    
    # convertimos a minusculas
    palabra_procesada = palabra.lower()
    
    # almacenamos resultados
    frecuencias = {}
    
    for letra in palabra_procesada:
       
        if letra.isalpha():
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
                
    print(f"\nAnálisis de la palabra: '{palabra}'")
    for letra, cantidad in frecuencias.items():
        print(f"La letra '{letra}' aparece {cantidad} {'vez' if cantidad == 1 else 'veces'}.")
    
    return "Conteo finalizado."

print(contar_letras())
