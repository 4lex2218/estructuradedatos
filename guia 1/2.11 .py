import math

def calcular_circulo():
    print("Cálculos del Círculo")
    
    try:
        radio = float(input("Ingrese el valor del radio:"))
        
        if radio < 0:
            return "Error: El radio no puede ser negativo."
            
        # Cálculos usando math.pi
        longitud = 2 * math.pi * radio
        area = math.pi * (radio ** 2)
        
        print(f"\nResultados para un radio de {radio}:")
        print(f"Longitud de la circunferencia: {longitud:.4f}")
        print(f"Área del círculo: {area:.4f}")
        return "Cálculo completado con éxito."
        
    except ValueError:
        return "Error: Ingrese un valor numérico válido."


print(calcular_circulo())
