def leer_opcion(mensaje, minimo, maximo):
    while True:
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            print(f"Seleccione una opcion entre {minimo} y {maximo}.")
        except ValueError:
            print("Ingrese un numero valido.")
 

def mostrar_pregunta(numero, codigo, resultado):
    print(f"Pregunta {numero}")
    print(codigo)
    print(f"Resultado:{resultado}")


def pregunta_1():
    codigo = """a = [1, 2, 3]
b = a
b[0] = 5
print(a)"""
    a = [1, 2, 3]
    b = a
    b[0] = 5
    mostrar_pregunta(1, codigo, a)


def pregunta_2():
    codigo = "print(type(10.0))"
    mostrar_pregunta(2, codigo, type(10.0))


def pregunta_3():
    codigo = """frase = "aprendo Python en TEC"
print(len(frase.split()))"""
    frase = "aprendo Python en TEC"
    mostrar_pregunta(3, codigo, len(frase.split()))


def pregunta_4():
    codigo = """socio = {"nombre": "Ana", "saldo": 120}
print(socio.get("correo", "Sin correo"))"""
    socio = {"nombre": "Ana", "saldo": 120}
    mostrar_pregunta(4, codigo, socio.get("correo", "Sin correo"))


def pregunta_5():
    codigo = """a = {1, 2, 3, 4}
b = {3, 4, 5}
print(len(a & b))"""
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    mostrar_pregunta(5, codigo, len(a & b))


def pregunta_6():
    codigo = """suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)"""
    suma = 0
    for n in range(1, 5):
        if n % 2 != 0:
            continue
        suma += n
    mostrar_pregunta(6, codigo, suma)


def pregunta_7():
    codigo = """total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)"""
    total = 0
    n = 1
    while n <= 5:
        total += n
        n += 1
    mostrar_pregunta(7, codigo, total)


def pregunta_8():
    codigo = "print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])"
    resultado = [n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0]
    mostrar_pregunta(8, codigo, resultado)


def pregunta_9():
    codigo = """for x in [2, 4, 6]:
    if x == 7:
        print("Encontrado")
        break
else:
    print("No encontrado")"""
    for x in [2, 4, 6]:
        if x == 7:
            resultado = "Encontrado"
            break
    else:
        resultado = "No encontrado"

    mostrar_pregunta(9, codigo, resultado)


def pregunta_10():
    codigo = """saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Basica")"""
    saldo = 350
    if saldo >= 1000:
        resultado = "Oro"
    elif saldo >= 100:
        resultado = "Plata"
    else:
        resultado = "Basica"
    mostrar_pregunta(10, codigo, resultado)


def mostrar_coop_tec():
    print("Pregunta 11: Ejercicio Coop-TEC")
    coop = 0
    tec = 0
    coop_tec = 0

    for numero in range(1, 31):
        if numero % 3 == 0 and numero % 5 == 0:
            print("CoopTEC")
            coop_tec += 1
        elif numero % 3 == 0:
            print("Coop")
            coop += 1
        elif numero % 5 == 0:
            print("TEC")
            tec += 1
        else:
            print(numero)

    print(f"Coop aparece {coop} veces")
    print(f"TEC aparece {tec} veces")
    print(f"CoopTEC aparece {coop_tec} veces")


def menu_preguntas():
    preguntas = {
        1: pregunta_1,
        2: pregunta_2,
        3: pregunta_3,
        4: pregunta_4,
        5: pregunta_5,
        6: pregunta_6,
        7: pregunta_7,
        8: pregunta_8,
        9: pregunta_9,
        10: pregunta_10,
        11: mostrar_coop_tec,
    }

    while True:
        for numero in range(1, 12):
            titulo = "Ejercicio Coop-TEC" if numero == 11 else "¿Que imprime el codigo?"
            print(f"{numero}. {titulo}")
        print("12. Salir")
        print("13. Regresar al menu principal")

        opcion = leer_opcion("Seleccione una opcion: ", 1, 13)
        if opcion == 12:
            return False
        if opcion == 13:
            return True

        preguntas[opcion]()
        input("Presione ENTER para volver al menu de preguntas")


def menu_principal():
    nombre = ""

    while True:
        print("MENU PRINCIPAL")
        print("1. Ingresar nombre y mostrar mensaje de bienvenida")
        print("2. Menu de preguntas")
        print("3. Salir")

        opcion = leer_opcion("Seleccione una opcion: ", 1, 3)
        if opcion == 1:
            nombre = input("Ingrese su nombre: ").strip()
            while not nombre:
                print("El nombre no puede estar vacio.")
                nombre = input("Ingrese su nombre: ").strip()
            print(f"Bienvenido/a, {nombre}")
        elif opcion == 2:
            if not menu_preguntas():
                break
        else:
            break


menu_principal()

