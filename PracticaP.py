def operaciones(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return suma, resta, multiplicacion, division
    
print(operaciones(5, 3))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

while True:
    try:
        opcion = int(input("Ingrese 1 para realizar operaciones o 2 para crear una persona: "))
        if opcion == 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultados = operaciones(a, b)
            print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")
        elif opcion == 2:
            break
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
    else:
        print("Opción no válida. Intente de nuevo.")
    finally:
        print("Gracias por usar el programa.")

#Usar diccionarios, listas, funciones, y clases para crear un programa que permita al usuario realizar operaciones matemáticas básicas (suma, resta, multiplicación, división) y crear objetos de tipo Persona con nombre y edad. El programa debe manejar errores de entrada y permitir al usuario elegir entre realizar operaciones o crear una persona.
diccionario_personas = {}
while True:
    try:
        opcion = int(input("Ingrese 1 para realizar operaciones, 2 para crear una persona o 3 para salir: "))
        if opcion == 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultados = operaciones(a, b)
            print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la persona: ")
            edad = int(input("Ingrese la edad de la persona: "))
            persona = Persona(nombre, edad)
            diccionario_personas[nombre] = persona
            print(persona.saludar())
        elif opcion == 3:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
    finally:
        print("Gracias por usar el programa.")