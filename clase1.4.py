#Declaracion de funciones
def saludar():
    print("Hola, Alex")
saludar()
#Funcion con parametros


#def calcular_edad(anio_nacimiento, anio_actual):
#   print("La edad es: ", anio_actual - anio_nacimiento)
#a = int(input("Ingrese el año de nacimiento: "))
#b = int(input("Ingrese el año actual: "))
#calcular_edad(a, b)

#Funcion con retorno
def calcular_iva(precio, valor_iva):
    return precio * valor_iva
resultado = calcular_iva(10, 0.15)
print("El IVA es: ", resultado)
#Funcion con valores por defecto
def calcular_iva(precio, valor_iva=0.15):
    return precio * valor_iva
resultado = calcular_iva(100)
print("El IVA es: ", resultado)
resultado = calcular_iva(100, 0.14)
print("El IVA es: ", resultado)
#Funciones con listas
def calcular_par(numeros):
    for n in numeros:
        if n % 2 == 0:
            print("El numero ", n, " es par")
        else:
            print("El numero ", n, " es impar")
lista_numeros = range(0, 1000, 2)
calcular_par(lista_numeros)
lista_numeros = range(5, 0, -1)
for i in lista_numeros:
    print(i, end=" ")
#Funciones con tuplas
def suma_numeros(*numeros):
    return sum(numeros)
print(suma_numeros(1, 2, 3, 4, 5))
#Funciones con diccionarios
def estuantes(**lista_estudiantes):
    suma_edades = 0
    for nombre, edad in lista_estudiantes.items():
        print("El estudiante ", nombre, " tiene ", edad, " años")
        suma_edades += edad
    print("La suma de las edades es: ", suma_edades)

estuantes(Alex=18, Juan=21, Maria=22, David=18, Henry=18, AlexL=20, Andersson=21)

# Funcion CoopTec
def mostrar_coop_tec():
    coop = 0
    tec = 0
    coop_tec = 0

    for i in range(1, 31):
        if i % 3 == 0 and i % 5 == 0:
            print("CoopTec")
            coop_tec += 1
        elif i % 3 == 0:
            print("Coop")
            coop += 1
        elif i % 5 == 0:
            print("Tec")
            tec += 1
        else:
            print(i)

    print(f"Coop aparece {coop} veces")
    print(f"Tec aparece {tec} veces")
    print(f"CoopTec aparece {coop_tec} veces")


mostrar_coop_tec()
""" Menu usuario
1.Ingrese el nombre:Mensaje de Bienvenida
2.Menu de preguntas: Va a presentar las 11 preguntas, darle nombre a cada pregunta y mostrar el resultado de cada una, 12.Salir, 13.Regresar al menu principal,
3.salir"""