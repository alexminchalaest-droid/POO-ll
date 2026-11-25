class controladorLaboratorio:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion = ""
        while opcion != "4":
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                try:
                    nombre, marca, unidades = self.vista.solicitar_datos_equipo()
                    mostrar_mensaje = self.modelo.registrar_equipo(nombre, marca, unidades)
                    self.vista.mostrar_mensaje(mostrar_mensaje)

                except ValueError as e:
                    self.vista.mostrar_mensaje(f"Error: {e}")

            elif opcion == "2":
                self.vista.mostrar_equipos(self.modelo.mostrar_equipos())

            elif opcion == "3":
                codigo = self.vista.leer_entero("Codigo: ", minimo=1)
                equipo = self.modelo.buscar(codigo)
                if equipo is None:
                    self.vista.mostrar_mensaje("Error, el codigo no existe")
                else:
                    cantidad = self.vista.leer_entero("Cantidad: ", minimo=1)
                    resultado = self.modelo.prestar_equipo(codigo, cantidad)
                    if resultado is True:
                        self.vista.mostrar_mensaje("Prestamo realizado")
                    else:
                        self.vista.mostrar_mensaje(resultado[1])

            elif opcion == "4":
                self.vista.mostrar_mensaje("Programa finalizado")
                break

            else:
                self.vista.mostrar_mensaje("Opcion no valida")