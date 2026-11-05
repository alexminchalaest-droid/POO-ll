#Creando una lista de notas
notas=[10,8,9,5]
#Imprimimos la lista de notas
print(notas)
#Agregamos un elemento a la lista
notas.append(20)
#Insertamos un elemento en una posición específica
notas.insert(1,10)
#Imprimimos el elemento en la posición 3 de la lista
print(notas[3])
#Presentamos el máximo de la lista
print(max(notas))
#Tamaño de la lista
print(len(notas))
#Presentamos el último elemento de la lista
print(notas[-1])
#Presentamos el primer elemento de la lista
print(notas[0])
#Sumamos todos los elementos de la lista
print(sum(notas))
#Presentamos los dos últimos elementos de la lista
print(notas[2:])
#Presentamos los dos primeros elementos de la lista
print(notas[:2])
#Presentamos el mínimo de la lista
print(min(notas))
#Presentamos la lista ordenada
print(sorted(notas))
#Eliminamos un elemento de la lista
notas.remove(5)
#Imprimir la lista alreves
print(notas[::-1])

#Tuplas
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
#Imprimimos el primer elemento de la tupla
print(meses[0])
#Imprimimos el último elemento de la tupla
print(meses[-1])
# No se puede modificar una tupla
# meses[3]=15

#Diccionarios
estudiante={
    "cedula":"0150572600",
    "nombre":"Alex Minchala",
    "edad":18,
    "correo":"alexalva200821@gmail.com",
    "notas":[10,8,9,5]
}
#Impriimos el valor de la clave nombre del diccionario
print(estudiante.get("nombre"))
print(estudiante["nombre"])
#Imprimir las claves del diccionario
print(estudiante.keys())
#agregar un elemento al diccionario
estudiante["telefono"]="0987654321"
conjunto_a= {1,1,5,4,6,8}
conjunto_b= {1,9,6,4,5,4}
#Imprimir la intersección de los conjuntos
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.union(conjunto_b))