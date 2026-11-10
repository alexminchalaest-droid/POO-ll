lista = [1, 2, 3, 4, 5]
print("La lista es:", lista)
#primer elemento de la lista
print("El primer elemento de la lista es:", lista[0])
#imprimir lista con for each
for elemento in lista:
    print("Elemento:", elemento)

#imprimir pares e impares
print("Pares:")
for elemento in lista:
    if elemento % 2 == 0:
        print("Elemento par:", elemento)
    else:
        print("Elemento impar:", elemento)
#Solicitar al usuario ingresar un saldo, si el saldo es igual a mayor o mil, imprimir "categoria oro", si es menor a mil pero mayor o igual a 500, imprimir "categoria plata", si es menor a 500 imprimir "categoria bronce"
saldo = float(input("Ingrese su saldo: "))
if saldo >= 1000:
    print("categoria oro")
elif saldo >= 500:
    print("categoria plata")
else:
    print("categoria bronce")   
