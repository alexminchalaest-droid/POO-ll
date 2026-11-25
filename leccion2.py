# Pregunta 1: Referencias a listas
print("Pregunta 1")
a = [1, 2, 3]
b = a
b[0] = 5
print(a)

# Pregunta 2: Tipo de dato float
print("Pregunta 2")
print(type(10.0))

# Pregunta 3: Cantidad de palabras en una frase
print("Pregunta 3")
frase = "aprendo Python en TEC"
print(len(frase.split()))

# Pregunta 4: Valor predeterminado de un diccionario
print("Pregunta 4")
socio = {"nombre": "Ana", "saldo": 120}
print(socio.get("correo", "Sin correo"))

# Pregunta 5: Intersección de conjuntos
print("Pregunta 5")
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(len(a & b))

# Pregunta 6: Suma de números pares
print("Pregunta 6")
suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)

# Pregunta 7: Suma de números usando while
print("Pregunta 7")
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)

# Pregunta 8: Comprensión de listas con números pares
print("Pregunta 8")
print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])

# Pregunta 9: Uso de else en un ciclo for
print("Pregunta 9")
for x in [2, 4, 6]:
    if x == 7:
        print("Encontrado")
        break
else:
    print("No encontrado")

# Pregunta 10: Evaluación de condiciones if, elif y else
print("Pregunta 10 ")
saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Básica")

# Ejercicio 11: Coop-TEC
# Mostrar los números del 1 al 30 y contar cada palabra.
print("Ejercicio 11: Coop-TEC")
coop = 0
tec = 0
coop_tec = 0

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("CoopTEC")
        coop_tec += 1
    elif i % 3 == 0:
        print("Coop")
        coop += 1
    elif i % 5 == 0:
        print("TEC")
        tec += 1
    else:
        print(i)

print(f"Coop aparece {coop} veces")
print(f"TEC aparece {tec} veces")
print(f"CoopTEC aparece {coop_tec} veces")
