from modelo import*
from vista import vistaOperaciones
from controlador import controladorLaboratorio

modelo = ListaEquipos()
vista = vistaOperaciones()
controlador = controladorLaboratorio(modelo, vista)
controlador.ejecutar() 