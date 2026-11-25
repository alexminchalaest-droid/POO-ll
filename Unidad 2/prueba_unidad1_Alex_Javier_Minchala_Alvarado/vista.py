class vistaOperaciones:
    def __init__(self):
        pass

    def mostrar_menu(self):
        print()
        print("MENU")
        print("1. Registrar equipo")
        print("2. Mostrar equipos")
        print("3. Prestar equipo")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        return opcion

    def solicitar_datos_equipo(self):
        nombre = self.leer_texto("Nombre: ")
        marca = self.leer_texto("Marca: ")
        unidades = self.leer_entero("Unidades: ", minimo=0)
        return nombre, marca, unidades

    def leer_texto(self, mensaje):
        while True:
            texto = input(mensaje).strip()
            if texto:
                return texto
            print("Error, el campo no puede estar vacio")

    def leer_entero(self, mensaje, minimo=None):
        while True:
            try:
                valor = int(input(mensaje).strip())
            except ValueError:
                print("Error, ingrese solo numeros enteros.")
                continue
            if minimo is not None and valor < minimo:
                print(f"Error, el valor debe ser mayor o igual a {minimo}.")
                continue
            return valor

    def mostrar_equipos(self, equipos):
        print("los equipos registrados son:")
        print("Codigo  Nombre                  Marca                   Unidades")
        for equipo in equipos:
            print(equipo)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

