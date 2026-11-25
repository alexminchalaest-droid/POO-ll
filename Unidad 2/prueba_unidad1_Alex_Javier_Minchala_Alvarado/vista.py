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
        nombre = input("Nombre: ").strip()
        marca = input("Marca: ").strip()
        unidades = int(input("Unidades: ").strip())
        return nombre, marca, unidades

