# Cuaderno de ejercicios resueltos — POO II con Python

Este cuaderno complementa la [guía de estudio](<Guia_de_estudio_POO_II.md>) con ejercicios ordenados desde los fundamentos hasta pequeños programas integradores. Cada ejercicio incluye la **orden**, una posible **solución** y los conceptos que practica.

## Antes de empezar

- Ejecuta cada solución en una celda o archivo independiente.
- Lee primero la orden e intenta anticipar el resultado.
- En las primeras actividades se usan datos de ejemplo para que el código sea fácil de probar. En los programas interactivos se muestra `input()`.
- El ejercicio de archivos crea o reemplaza `movimientos_demo.txt` en la carpeta desde donde ejecutes el código. Si quieres conservar un archivo con ese nombre, cambia la ruta.
- Las soluciones son una forma correcta de resolver cada problema; puede haber otras.

---

## 1. Registro y plazo fijo

### Orden

Pide el nombre de una persona, el monto que desea invertir y el plazo en meses. No aceptes inversiones menores a $100 ni plazos menores que un mes. Usa estas tasas anuales:

- Menos de 6 meses: 4 %.
- De 6 a 11 meses: 5,5 %.
- 12 meses o más: 7 %.

Calcula el interés simple y muestra el nombre, la tasa, el interés y el total con dos decimales.

### Solución

```python
nombre = input("Nombre del socio: ").strip()
monto = float(input("Monto a invertir: "))
meses = int(input("Plazo en meses: "))

if monto < 100:
    print("El monto mínimo es $100.")
elif meses < 1:
    print("El plazo debe ser de al menos un mes.")
else:
    if meses < 6:
        tasa_anual = 0.04
    elif meses < 12:
        tasa_anual = 0.055
    else:
        tasa_anual = 0.07

    interes = monto * tasa_anual * (meses / 12)
    total = monto + interes

    print(f"Socio: {nombre}")
    print(f"Tasa anual: {tasa_anual:.1%}")
    print(f"Interés: ${interes:,.2f}")
    print(f"Total a recibir: ${total:,.2f}")
```

**Practica:** `input`, conversiones, operadores, condiciones, f-strings y cálculo de interés simple. La conversión de texto no numérico todavía puede producir `ValueError`; el ejercicio 7 muestra cómo manejarlo.

---

## 2. Limpiar y convertir una ficha

### Orden

Procesa el registro:

```text
  0102030405 ;  ana   pérez ; AHORROS ; 1250.75
```

Limpia los espacios, conserva la cédula como texto, convierte el saldo a `Decimal`, normaliza el nombre y el tipo de cuenta, y muestra una ficha. Calcula además un interés del 2 %.

### Solución

```python
from decimal import Decimal

registro = "  0102030405 ;  ana   pérez ; AHORROS ; 1250.75"
campos = [campo.strip() for campo in registro.split(";")]

cedula = campos[0]  # Se conserva como texto para no perder ceros iniciales.
nombre = " ".join(campos[1].split()).title()
tipo_cuenta = campos[2].lower()
saldo = Decimal(campos[3])
interes = (saldo * Decimal("0.02")).quantize(Decimal("0.01"))

ficha = {
    "cedula": cedula,
    "nombre": nombre,
    "tipo": tipo_cuenta,
    "saldo": saldo,
}

print(f"Socio: {ficha['nombre']} ({ficha['cedula']})")
print(f"Cuenta: {ficha['tipo']}")
print(f"Saldo: ${ficha['saldo']:,.2f}")
print(f"Interés: ${interes:,.2f}")
```

**Practica:** cadenas inmutables, `split`, `strip`, `join`, `title`, `lower`, diccionarios, conversión y aritmética decimal. Para valores monetarios, crear `Decimal` desde texto evita heredar la aproximación binaria de `float`.

---

## 3. Resumen de socios y cuentas

### Orden

Usa una lista de diccionarios para representar socios. Cada socio tiene una lista de cuentas. Obtén los saldos de todas las cuentas, el total por socio, los tipos de cuenta sin repetidos, y comprueba si algún socio está inactivo o si todas las cuentas tienen saldo positivo.

### Solución

```python
socios = [
    {
        "nombre": "Ana",
        "activo": True,
        "cuentas": [
            {"numero": "AH-001", "tipo": "ahorros", "saldo": 1250.0},
            {"numero": "PF-001", "tipo": "plazo fijo", "saldo": 3000.0},
        ],
    },
    {
        "nombre": "Luis",
        "activo": False,
        "cuentas": [
            {"numero": "AH-002", "tipo": "ahorros", "saldo": 0.0},
        ],
    },
]

for socio in socios:
    saldos = [cuenta["saldo"] for cuenta in socio["cuentas"]]
    total = sum(saldos)
    print(f"{socio['nombre']:<8} {len(saldos):>2} cuenta(s)  ${total:>9,.2f}")

tipos = {
    cuenta["tipo"]
    for socio in socios
    for cuenta in socio["cuentas"]
}

todos_los_saldos = [
    cuenta["saldo"]
    for socio in socios
    for cuenta in socio["cuentas"]
]

print("Tipos registrados:", sorted(tipos))
print("¿Hay un socio inactivo?:", any(not socio["activo"] for socio in socios))
print("¿Todos los saldos son positivos?:", all(saldo > 0 for saldo in todos_los_saldos))
```

**Practica:** listas y diccionarios anidados, comprensiones, `sum`, `len`, `any`, `all`, `set` y formato alineado. El conjunto elimina repetidos; por eso se usa `sorted` para mostrar sus valores en orden.

---

## 4. Clasificar, contar y buscar

### Orden

Con una lista de edades, clasifica cada persona como menor, adulta o adulta mayor. Cuenta cuántas personas hay en cada grupo. Luego busca una edad objetivo: si aparece, informa su posición; si el recorrido termina sin encontrarla, muestra que no existe.

### Solución

```python
edades = [17, 25, 64, 70, 15, 40]
conteos = {"menor": 0, "adulto": 0, "adulto mayor": 0}

for posicion, edad in enumerate(edades, start=1):
    if edad < 18:
        grupo = "menor"
    elif edad < 65:
        grupo = "adulto"
    else:
        grupo = "adulto mayor"

    conteos[grupo] += 1
    print(f"Persona {posicion}: {edad} años → {grupo}")

print("Resumen:", conteos)

objetivo = 40
for indice, edad in enumerate(edades):
    if edad == objetivo:
        print(f"La edad {objetivo} está en el índice {indice}.")
        break
else:
    print(f"La edad {objetivo} no aparece en la lista.")
```

**Practica:** `for`, `enumerate`, decisiones encadenadas, diccionarios como contadores y el `else` de un ciclo. El `else` se ejecuta únicamente cuando el ciclo termina sin `break`.

---

## 5. Ahorro con `while`, validación y `continue`

### Orden

Procesa estos intentos de depósito: `[100, -20, 50, 0, 75]`. Ignora los valores menores o iguales a cero, cuenta los depósitos válidos y detén el proceso cuando el acumulado llegue a $200. Muestra cada depósito válido y el resultado final.

### Solución

```python
intentos = [100, -20, 50, 0, 75]
saldo = 0
depositos_validos = 0
indice = 0

while indice < len(intentos) and saldo < 200:
    monto = intentos[indice]
    indice += 1

    if monto <= 0:
        print(f"Se ignora el monto {monto}.")
        continue

    saldo += monto
    depositos_validos += 1
    print(f"Depósito aceptado: ${monto:.2f} | Saldo: ${saldo:.2f}")

print(f"Saldo final: ${saldo:.2f}")
print(f"Depósitos aceptados: {depositos_validos}")
```

**Practica:** `while`, acumuladores, contadores, validación, `continue` y condición compuesta. Como la lista de intentos es finita, también hay una condición que asegura que el índice no se salga de rango.

---

## 6. Matriz de depósitos y ordenamiento

### Orden

Representa los depósitos trimestrales de tres socios en una matriz (lista de listas). Muestra cada socio junto con sus depósitos y total anual. Calcula el total por trimestre, empareja nombres y totales con `zip`, y ordena los socios del mayor al menor total.

### Solución

```python
socios = ["Ana", "Luis", "María"]
depositos = [
    [300, 250, 400, 350],
    [50, 0, 80, 60],
    [200, 220, 180, 260],
]

totales = []
for nombre, fila in zip(socios, depositos):
    total = sum(fila)
    totales.append(total)
    print(f"{nombre:<8} depósitos={fila} total=${total:,.2f}")

for indice_trimestre in range(4):
    total_trimestre = 0
    for fila in depositos:
        total_trimestre += fila[indice_trimestre]
    print(f"Trimestre {indice_trimestre + 1}: ${total_trimestre:,.2f}")

resumen = dict(zip(socios, totales))
ordenados = sorted(
    resumen.items(),
    key=lambda par: par[1],
    reverse=True,
)

print("Orden por saldo:")
for nombre, total in ordenados:
    print(f"{nombre:<8} ${total:,.2f}")
```

**Practica:** ciclos anidados, listas de listas, suma por fila y columna, `zip`, creación de diccionario, `sorted`, `lambda` como clave y `reverse=True`.

---

## 7. Funciones para una factura

### Orden

Crea una función `calcular_factura` con cantidad, descuento e IVA opcionales. Debe devolver subtotal, descuento, impuesto y total como una tupla. Crea además una función variádica para promediar cualquier cantidad de notas y una función que reciba información adicional con `**kwargs`.

### Solución

```python
def calcular_factura(
    precio: float,
    cantidad: int = 1,
    descuento: float = 0.0,
    tasa_iva: float = 0.15,
) -> tuple[float, float, float, float]:
    """Devuelve subtotal, descuento, IVA y total de una factura."""
    subtotal = precio * cantidad
    valor_descuento = subtotal * descuento
    base_imponible = subtotal - valor_descuento
    iva = base_imponible * tasa_iva
    total = base_imponible + iva
    return tuple(round(valor, 2) for valor in (
        subtotal, valor_descuento, iva, total
    ))


def promedio(*notas: float) -> float | None:
    """Calcula el promedio; devuelve None si no se reciben notas."""
    if not notas:
        return None
    return round(sum(notas) / len(notas), 2)


def mostrar_ficha(nombre: str, **datos: object) -> None:
    """Muestra el nombre y los datos adicionales recibidos."""
    print(f"Socio: {nombre}")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


subtotal, descuento, iva, total = calcular_factura(
    30,
    cantidad=3,
    descuento=0.10,
)
print(f"Subtotal=${subtotal:.2f}, descuento=${descuento:.2f}, "
      f"IVA=${iva:.2f}, total=${total:.2f}")

print("Promedio:", promedio(8.5, 9, 7.5))
print("Sin notas:", promedio())
mostrar_ficha("Ana", ciudad="Cuenca", activo=True)

assert calcular_factura(10) == (10.0, 0.0, 1.5, 11.5)
assert promedio(8, 10) == 9.0
assert promedio() is None
```

**Practica:** `def`, parámetros posicionales, argumentos por nombre, valores por defecto, tuplas de retorno, `*args`, `**kwargs`, docstrings, anotaciones de tipo y `assert`. En código compatible con Python anterior a 3.10, la anotación `float | None` puede escribirse `Optional[float]` importando `Optional` desde `typing`.

---

## 8. Excepciones y transferencias

### Orden

Crea una excepción propia para cuentas inexistentes. La función `transferir` debe verificar que ambas cuentas existan, que el monto sea positivo y que haya saldo suficiente. Si una regla no se cumple, lanza la excepción adecuada. Maneja los errores en el código que llama a la función.

### Solución

```python
class CuentaNoExisteError(Exception):
    """Se lanza cuando el número de cuenta no está registrado."""


def transferir(cuentas: dict[str, float], origen: str, destino: str, monto: float) -> None:
    """Mueve dinero entre dos cuentas si la operación es válida."""
    if origen not in cuentas:
        raise CuentaNoExisteError(f"No existe la cuenta de origen {origen}.")
    if destino not in cuentas:
        raise CuentaNoExisteError(f"No existe la cuenta de destino {destino}.")
    if monto <= 0:
        raise ValueError("El monto debe ser positivo.")
    if monto > cuentas[origen]:
        raise ValueError("Saldo insuficiente.")

    cuentas[origen] -= monto
    cuentas[destino] += monto


cuentas = {"AH-001": 500.0, "AH-002": 80.0}
operaciones = [
    ("AH-001", "AH-002", 100.0),
    ("AH-001", "AH-002", 1000.0),
    ("AH-009", "AH-002", 20.0),
]

for origen, destino, monto in operaciones:
    try:
        transferir(cuentas, origen, destino, monto)
    except CuentaNoExisteError as error:
        print(f"Cuenta no encontrada: {error}")
    except ValueError as error:
        print(f"Transferencia rechazada: {error}")
    else:
        print(f"Transferencia de ${monto:.2f} realizada.")
    finally:
        print("Operación terminada.")

print("Saldos:", cuentas)
```

**Practica:** excepciones específicas, `raise`, excepciones propias, `try`, `except`, `else` y `finally`. La función comunica el problema; el código que la utiliza decide qué mensaje mostrar.

---

## 9. Guardar y leer movimientos

### Orden

Guarda una lista de movimientos en `movimientos_demo.txt`, una operación por línea, con campos separados por coma. Después lee el archivo, calcula el total de depósitos y muestra el número de movimientos. Agrega una línea al final y maneja el caso en que el archivo no exista al leer.

### Solución

```python
nombre_archivo = "movimientos_demo.txt"
movimientos = [
    ("deposito", 120.50),
    ("retiro", 30.00),
    ("deposito", 75.25),
]

# Modo "w": crea el archivo o reemplaza su contenido.
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    for tipo, monto in movimientos:
        archivo.write(f"{tipo},{monto:.2f}\n")

total_depositos = 0.0
cantidad_movimientos = 0

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            tipo, monto_texto = linea.strip().split(",")
            monto = float(monto_texto)
            cantidad_movimientos += 1
            if tipo == "deposito":
                total_depositos += monto
except FileNotFoundError:
    print(f"No se encontró el archivo {nombre_archivo}.")
else:
    print(f"Movimientos leídos: {cantidad_movimientos}")
    print(f"Total depositado: ${total_depositos:.2f}")
finally:
    print("Lectura terminada.")

# Modo "a": agrega al final sin borrar las líneas anteriores.
with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("deposito,10.00\n")
```

**Practica:** `with open`, modos `"w"`, `"r"` y `"a"`, codificación UTF-8, `write`, lectura línea por línea, `strip`, `split`, conversión del texto y captura de `FileNotFoundError`.

---

## 10. Cuenta como objeto

### Orden

Crea una clase `Cuenta` con titular, número y saldo. El saldo debe usar `Decimal`. Implementa depósito y retiro con validaciones, una representación legible con `__str__` y comprueba que dos cuentas tengan estados independientes.

### Solución

```python
from decimal import Decimal


class Cuenta:
    def __init__(self, titular: str, numero: str, saldo: Decimal = Decimal("0.00")):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, monto: Decimal) -> None:
        if monto <= 0:
            raise ValueError("El depósito debe ser positivo.")
        self.saldo += monto

    def retirar(self, monto: Decimal) -> None:
        if monto <= 0:
            raise ValueError("El retiro debe ser positivo.")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= monto

    def __str__(self) -> str:
        return f"{self.numero} | {self.titular} | ${self.saldo:,.2f}"


ana = Cuenta("Ana", "AH-001")
luis = Cuenta("Luis", "AH-002", Decimal("80.00"))

ana.depositar(Decimal("150.50"))
ana.retirar(Decimal("20.25"))

print(ana)
print(luis)
assert ana.saldo == Decimal("130.25")
assert luis.saldo == Decimal("80.00")
```

**Practica:** clases, instancias, `__init__`, `self`, atributos, métodos, estado propio por objeto, `__str__`, `Decimal` y excepciones.

---

## 11. Tabla de amortización en una función

### Orden

Escribe una función que calcule una tabla de amortización con cuota fija. Debe recibir capital, tasa anual decimal y cantidad de meses; devolver una lista de diccionarios; y rechazar un capital no positivo, un plazo no positivo o una tasa negativa.

La tasa mensual es la tasa anual dividida para 12. Para tasa positiva, la cuota es:

```text
cuota = capital * tasa_mensual / (1 - (1 + tasa_mensual) ** -meses)
```

### Solución

```python
from decimal import Decimal


def tabla_amortizacion(
    capital: Decimal,
    tasa_anual: Decimal,
    meses: int,
) -> list[dict[str, Decimal | int]]:
    """Devuelve cuota, interés, capital amortizado y saldo de cada mes."""
    if capital <= 0:
        raise ValueError("El capital debe ser positivo.")
    if tasa_anual < 0:
        raise ValueError("La tasa no puede ser negativa.")
    if meses <= 0:
        raise ValueError("El plazo debe ser positivo.")

    centavo = Decimal("0.01")
    tasa_mensual = tasa_anual / Decimal(12)

    if tasa_mensual == 0:
        cuota_regular = (capital / meses).quantize(centavo)
    else:
        factor = (Decimal(1) + tasa_mensual) ** (-meses)
        cuota_regular = (
            capital * tasa_mensual / (Decimal(1) - factor)
        ).quantize(centavo)

    saldo = capital
    filas = []

    for mes in range(1, meses + 1):
        interes = (saldo * tasa_mensual).quantize(centavo)
        amortizacion = cuota_regular - interes

        # Se ajusta la última cuota para que el saldo cierre exactamente en cero.
        if mes == meses or amortizacion > saldo:
            amortizacion = saldo
            cuota = interes + amortizacion
        else:
            cuota = cuota_regular

        saldo = (saldo - amortizacion).quantize(centavo)
        filas.append({
            "mes": mes,
            "cuota": cuota,
            "interes": interes,
            "capital": amortizacion,
            "saldo": saldo,
        })

    return filas


filas = tabla_amortizacion(
    Decimal("1200.00"),
    Decimal("0.12"),
    6,
)

print(f"{'Mes':>3} {'Cuota':>9} {'Interés':>9} {'Capital':>9} {'Saldo':>10}")
for fila in filas:
    print(
        f"{fila['mes']:>3} "
        f"{fila['cuota']:>9.2f} "
        f"{fila['interes']:>9.2f} "
        f"{fila['capital']:>9.2f} "
        f"{fila['saldo']:>10.2f}"
    )

assert filas[-1]["saldo"] == Decimal("0.00")
```

**Practica:** funciones con parámetros y anotaciones, validación con `raise`, `Decimal`, `for` con `range`, acumulación de resultados, listas de diccionarios, formato y pruebas con `assert`.

---

## 12. Integrador: biblioteca con objetos, menú y archivos

### Orden

Implementa una biblioteca pequeña que:

1. Represente cada libro como un objeto con código, título, autor y estado.
2. Permita prestar y devolver libros, rechazando acciones inválidas.
3. Guarde el catálogo en `biblioteca_demo.txt` y lo cargue al iniciar.
4. Muestre un menú para listar libros, buscar por palabra, prestar, devolver y salir.
5. No se detenga si se ingresa una opción o un código que no sea entero.

Cada línea del archivo usa `|` como separador y termina con `1` si está disponible o `0` si está prestado. Para mantener este formato simple, no ingreses el carácter `|` en los títulos ni autores.

### Solución

```python
NOMBRE_ARCHIVO = "biblioteca_demo.txt"


class Libro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        autor: str,
        disponible: bool = True,
    ):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self) -> None:
        if not self.disponible:
            raise ValueError("El libro ya está prestado.")
        self.disponible = False

    def devolver(self) -> None:
        if self.disponible:
            raise ValueError("El libro ya está disponible.")
        self.disponible = True

    def serializar(self) -> str:
        estado = "1" if self.disponible else "0"
        return f"{self.codigo}|{self.titulo}|{self.autor}|{estado}"

    @classmethod
    def desde_linea(cls, linea: str) -> "Libro":
        campos = linea.strip().split("|")
        if len(campos) != 4 or campos[3] not in {"0", "1"}:
            raise ValueError(f"Registro de libro inválido: {linea.rstrip()}")
        return cls(
            codigo=int(campos[0]),
            titulo=campos[1],
            autor=campos[2],
            disponible=(campos[3] == "1"),
        )

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.codigo:>3} | {self.titulo:<25} | {self.autor:<20} | {estado}"


def guardar_libros(libros: list[Libro]) -> None:
    """Reemplaza el archivo con el estado actual del catálogo."""
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        for libro in libros:
            archivo.write(libro.serializar() + "\n")


def cargar_libros() -> list[Libro]:
    """Carga el catálogo o crea uno inicial si todavía no existe el archivo."""
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            return [
                Libro.desde_linea(linea)
                for linea in archivo
                if linea.strip()
            ]
    except FileNotFoundError:
        return [
            Libro(1, "Python para todos", "Autor A"),
            Libro(2, "Aprende Java", "Autor B"),
            Libro(3, "Bases de datos", "Autor C"),
        ]


def buscar_por_codigo(libros: list[Libro], codigo: int) -> Libro | None:
    """Devuelve el libro con ese código o None si no existe."""
    return next((libro for libro in libros if libro.codigo == codigo), None)


def mostrar_libros(libros: list[Libro]) -> None:
    for libro in libros:
        print(libro)


def main() -> None:
    libros = cargar_libros()

    while True:
        print("\n1. Mostrar libros")
        print("2. Buscar por título")
        print("3. Prestar")
        print("4. Devolver")
        print("0. Guardar y salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            palabra = input("Palabra a buscar: ").strip().lower()
            encontrados = [
                libro for libro in libros
                if palabra in libro.titulo.lower()
            ]
            if encontrados:
                mostrar_libros(encontrados)
            else:
                print("No se encontraron libros.")
        elif opcion in {"3", "4"}:
            try:
                codigo = int(input("Código del libro: "))
            except ValueError:
                print("El código debe ser un número entero.")
                continue

            libro = buscar_por_codigo(libros, codigo)
            if libro is None:
                print("No existe un libro con ese código.")
                continue

            try:
                if opcion == "3":
                    libro.prestar()
                    print("Préstamo registrado.")
                else:
                    libro.devolver()
                    print("Devolución registrada.")
            except ValueError as error:
                print(error)
        elif opcion == "0":
            guardar_libros(libros)
            print("Catálogo guardado. Hasta pronto.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
```

**Practica:** clases, atributos, métodos, `self`, `__str__`, métodos de clase, excepciones, búsqueda, listas, comprensiones, menú con `while`, decisiones, entrada, conversión, lectura y escritura de archivos, `with`, `encoding` y `FileNotFoundError`.

---

## Resumen de cobertura

| Contenido de los notebooks | Ejercicios |
|---|---|
| `print`, `input`, conversiones, operadores, `if` y f-strings | 1 |
| Tipos, cadenas, `Decimal`, listas, tuplas, diccionarios y conjuntos | 2 y 3 |
| `while`, `for`, `range`, contadores, acumuladores, `break` y `continue` | 4 y 5 |
| `enumerate`, `zip`, matrices, ciclos anidados, `sorted`, `lambda`, `any` y `all` | 3, 4 y 6 |
| Funciones, retornos, valores por defecto, `*args`, `**kwargs` y `assert` | 7 y 11 |
| `try`, `except`, `else`, `finally`, `raise` y excepciones propias | 8 y 12 |
| `open`, modos `"r"`, `"w"`, `"a"`, `with` y errores de archivo | 9 y 12 |
| Clases, objetos, atributos, métodos y `__str__` | 10 y 12 |
| Interés, amortización y lógica de un sistema | 1, 11 y 12 |

### Nota sobre versiones de Python

Las anotaciones `list[Tipo]`, `dict[Clave, Valor]` y `TipoA | TipoB` usadas en los últimos ejemplos requieren Python 3.10 o posterior. Si tu instalación es anterior, puedes quitar las anotaciones o usar tipos de `typing`.
