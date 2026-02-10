'''  #(EJERCICIO DE LLAMADA QUITAR LOS 3 APOSTROFES)
def realizar_llamada(numero_destino, minutos):
    print(f"llamando a {numero_destino}")
    
    if minutos < 1:
        return "sin saldo."
    
    print("cogiendo el telefono")
    print(f"Marcando el número {numero_destino}...")
    
    timbre = True 
    contestan = True 
    
    if timbre and contestan:
        print("contestó. hablando...")
        print("llamada terminada, colgando ")
        return "llamada realizada con éxito."
    else:
        print("no hay respuesta")
        return "llamada sin exito."

print(realizar_llamada("3145678911", 22)) 

'''   #(EJERCICIO DE LLAMADA QUITAR LOS 3 APOSTROFES)

''' #EJERCICIO DE TORTILLA (B) QUITAR 3 APOSTROFES PARA PROBAR
def cocinar_tortilla(huevos, aceite):
    print(" Preparar tortilla ")
    
    if huevos < 2 or not aceite:
        return "Faltan ingredientes."

    print("Batiendo los huevos")
    print("Calentando la sartén con un poco de aceite")
    
    sarten_caliente = False
    while not sarten_caliente:
        print("Esperando a que el aceite esté caliente")
        sarten_caliente = True # El aceite se calienta
        
    print("Echando el huevo")
    print("Dando vuelta a la tortilla")
    print("Tortilla lista")
    return "tortilla terminada"

cocinar_tortilla(3, True)
''' #EJERCICIO DE TORTILLA (B) QUITAR 3 APOSTROFES PARA PROBAR

''' #EJERCICIO (C) DE LLANTA PINCHADA QUITAR LOS 3 APOSTROFES PARA PROBAR
def arreglar_llanta():
    print("reparacion de llanta")
    
    
    herramientas = True
    
    if not herramientas:
        return "No puedes arreglar la llanta sin herramientas."

    print("1. quitando la rueda de la cicla.")
    print("2. quitandole el aire.")
    print("3. encontrar la fuga.")
    
    fuga_localizada = True
    if fuga_localizada:
        print("4. Lijando la zona de la llanta donde esta pinchada.")
        print("5. Poner pegamento y el parche.")
        print("6. Comprobando que no haya más fugas.")
        print("7. Poner la rueda en la cicla.")
        print("8. Inflando correctamente.")
        return "Cicla lista para rodar."
    
    return "No se encontró el llanta."

print(arreglar_llanta())
''' #EJERCICIO (C) DE LLANTA PINCHADA QUITAR LOS 3 APOSTROFES PARA PROBAR

''' #EJERCICIO DE FRITAR HUEVO ( EJERCICIO D) QUITAR LOS 3 APOSTROFES PARA PROBAR
def fritar_huevo():
    print("Fritar huevo")
    
    
    temperatura_aceite = 0 # Grados imaginarios
    
    print("Poniendo la sartén al fuego")
    
    # Refinamiento: Esperar a que el aceite esté en su punto
    while temperatura_aceite < 180:
        temperatura_aceite += 60
        print(f"Calentando sartén temperatura actual: {temperatura_aceite}°C")
        
    print("Rompiendo la cáscara y echando el huevo")
    print("Cocinando bien")
    print("Retirando el huevo y quitando el exceso de aceito")
    
    return "Huevo servido en el plato."

print(fritar_huevo())
''' #EJERCICIO DE FRITAR HUEVO ( EJERCICIO D) QUITAR LOS 3 APOSTROFES PARA PROBAR
