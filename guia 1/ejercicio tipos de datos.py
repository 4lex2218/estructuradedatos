# numeros enteros (positivos o negativos)

edad = 20
puntos = -22
print(f"Entero: {edad} | Tipo: {type(edad)}")


# reales o decimales
precio = 22.87
pi = 3.14159265
print(f"Real: {precio} | Tipo: {type(precio)}")


# verdadeor o falso
es_valido = True
es_mayor = False
print(f"Lógico: {es_valido} | Tipo: {type(es_valido)}")


# simbolo letra o numero para definir si es str de 1 de longitud
inicial = 'A'
simbolo = '/'
print(f"Carácter: {inicial} | Tipo: {type(inicial)}")


# cadena de caracteres
saludo = "Estructura de datos"
print(f"Cadena: '{saludo}' | Tipo: {type(saludo)}")


# clases u objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

usuario = Persona("Alejandro Olaya", 20)
print(f"Definido por usuario: {usuario.nombre}, {usuario.edad} años | Tipo: {type(usuario)}")
