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

class ListaEquipos:
    def __init__(self):
        self.lista = []
        self.cargar_equipos()

    def cargar_equipos(self):
        datos = [
        Equipo(1, "Multimetro", "Fluke", 10),
        Equipo(2, "Osciloscopio", "Rigol", 4),]
        for f in datos:
            self.lista.append(f)

    def registrar_equipo(self, nombre, marca, unidades):
        codigo = len(self.lista) + 1
        self.lista.append(Equipo(codigo, nombre, marca, unidades))
        print(f"Registrado con el codigo {codigo}.")

    def mostrar_equipos(self):
       return self.lista

    def prestar_equipo(self, codigo, cantidad):
        equipo = self.buscar(codigo)
        if equipo is None:
            print("Error, el codigo no existe")
            return False
        return equipo.prestar(cantidad)