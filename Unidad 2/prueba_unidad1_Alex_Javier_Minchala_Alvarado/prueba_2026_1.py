class Equipo:
    def __init__(self, codigo, nombre, marca, unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.unidades = unidades

    def prestar(self, cantidad):
        if cantidad <= 0:
            print("Error, la cantidad debe ser mayor que cero")
            return False
        if cantidad > self.unidades:
            print(f"Error, solo hay {self.unidades} unidades")
            return False
        self.unidades -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<24}{self.marca:<24}{self.unidades:<14}"
def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error, el campo no puede estar vacio")
def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error, ingrese solo numeros enteros.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Error, el valor debe ser mayor o igual a {minimo}.")
            continue
        return valor

def buscar(lista, codigo):
    for elemento in lista:
        if elemento.codigo == codigo:
            return elemento
    return None
lista = [
    Equipo(1, "Multimetro", "Fluke", 10),
    Equipo(2, "Osciloscopio", "Rigol", 4),]
while True:
    print()
    print("MENU")
    print("1. Registrar equipo")
    print("2. Mostrar equipos")
    print("3. Prestar equipo")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ").strip()
    if opcion == "1":
        nombre = leer_texto("Nombre: ")
        marca = leer_texto("Marca: ")
        unidades = leer_entero("Unidades: ", 0)
        codigo = len(lista) + 1
        lista.append(Equipo(codigo, nombre, marca, unidades))
        print(f"Registrado con el codigo {codigo}.")
    elif opcion == "2":
        print("Codigo  Nombre                  Marca                   Unidades")
        for elemento in lista:
            print(elemento)
    elif opcion == "3":
        codigo = leer_entero("Codigo: ")
        elemento = buscar(lista, codigo)
        if elemento is None:
            print("Error, no existe ese codigo.")
        else:
            cantidad = leer_entero("Cantidad: ")
            if elemento.prestar(cantidad):
                print(f"Listo, Quedan {elemento.unidades} unidades.")
    elif opcion == "4":
        print("Programa finalizado")
        break
    else:
        print("Opcion no valida")
    
