# Guía de estudio — POO II con Python

Esta guía recorre los notebooks disponibles en el orden en que construyen los conocimientos: desde las primeras instrucciones hasta clases y archivos. Las explicaciones describen los conceptos y ejemplos que aparecen en los materiales; los repasos se identifican como tales para evitar estudiar lo mismo dos veces. Al final hay ejercicios nuevos por tema y retos que combinan varios.

## Cómo usar la guía

1. Estudia un apartado y abre el notebook correspondiente para ejecutar sus ejemplos.
2. Antes de ejecutar una celda, predice qué hará. Luego compara tu predicción con el resultado.
3. Prueba entradas distintas y observa qué cambia.
4. Resuelve los ejercicios finales sin copiar las soluciones ya incluidas en los notebooks.

En Jupyter, las celdas comparten variables y estado. Si una variable conserva un valor inesperado, reinicia el kernel y vuelve a ejecutar las celdas en orden.

---

## 1. Introducción a Python

**Notebook:** [POO II - 1.1 Introducción a Python](<POO II - 1.1 Introduccion a Python.ipynb>)

### Python y Java

Los conceptos de programación son los mismos que ya se conocen de Java —variables, condiciones, ciclos y objetos—, pero cambia la forma de escribirlos. Python usa sangría para delimitar bloques, no llaves; normalmente no necesita punto y coma; y permite asignar un valor sin declarar antes el tipo de la variable. Por convención, los nombres compuestos se escriben en `snake_case`, por ejemplo `saldo_inicial`.

### Salida, comentarios y variables

- `print(valor)` muestra información. Puede recibir varios valores; `sep` cambia el separador y `end` cambia lo que se imprime al final.
- `#` inicia un comentario de una línea. Las cadenas entre triples comillas pueden documentar código.
- Una asignación como `edad = 20` asocia un nombre a un valor. `type(edad)` permite consultar el tipo actual.
- Python tiene tipado dinámico: una variable puede referirse a valores de tipos distintos, aunque suele ser más claro mantener un tipo coherente.
- Se pueden asignar varios valores a la vez: `a, b = 1, 2`; también intercambiar dos variables con `a, b = b, a`.

### Entrada, conversión y formato

`input()` siempre devuelve texto (`str`), incluso si se ingresan dígitos. Para calcular con la entrada se convierte, por ejemplo, con `int(input(...))` o `float(input(...))`. Si el texto no representa un número compatible, la conversión falla; ese problema se aborda en el notebook de excepciones.

Una f-string, escrita como `f"Saldo: {saldo}"`, inserta valores dentro del texto. El formato `:.2f` limita la presentación a dos decimales. Concatenar una cadena con un número requiere convertir el número a texto; usar f-strings suele ser más legible.

### Operadores y decisiones

- Aritmética: `+`, `-`, `*`, `/`, `//` (división entera), `%` (residuo) y `**` (potencia).
- Comparaciones: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Lógica: `and`, `or`, `not`. El incremento se escribe, por ejemplo, `contador += 1`.
- Python permite encadenar comparaciones como `7 <= nota <= 10`.
- `if`, `elif` y `else` eligen una rama. La condición termina en `:` y el bloque se indenta. La expresión `"Activo" if saldo > 0 else "Inactivo"` es una forma breve de escoger entre dos valores.

El caso de plazo fijo une entradas, conversiones, decisiones, una tasa y una fórmula de interés simple. Es importante validar el monto antes de calcular: una condición de negocio (por ejemplo, monto mínimo) no es lo mismo que un error de conversión de entrada.

---

## 2. Variables, tipos y colecciones

**Notebook:** [POO II - 1.2 Variables y Tipos de Datos](<POO II - 1.2 Variables y Tipos de Datos .ipynb>)

### Tipos básicos y números

- `int`: enteros de tamaño arbitrario.
- `float`: números de punto flotante; su representación binaria puede producir pequeñas diferencias, como `0.1 + 0.2`.
- `bool`: `True` o `False`.
- `str`: texto; un carácter también es una cadena, no hay un tipo `char` independiente.
- `None`: ausencia de valor. Se comprueba idiomáticamente con `valor is None`.

`round()` sirve para presentar o redondear resultados, pero no convierte por sí solo todos los cálculos financieros en aritmética decimal exacta. Para dinero, el notebook presenta `Decimal`; se construye desde texto (`Decimal("0.10")`) para evitar introducir el error binario del `float`. También aparecen funciones integradas como `abs`, `max`, `min`, `sum` y `divmod`.

### Cadenas (`str`)

Las cadenas son inmutables: métodos como `.upper()` producen una nueva cadena; para guardar el cambio hay que reasignarla. Los índices empiezan en cero; los negativos cuentan desde el final. El *slicing* `texto[inicio:fin]` incluye `inicio` y excluye `fin`; se puede omitir uno de los extremos y usar un paso, como `[::-1]` para invertir.

Métodos y operaciones practicados:

- `.strip()`, `.upper()`, `.lower()`, `.title()`, `.replace()` y `.split()`.
- `.startswith()`, `.isdigit()`, `.count()`, `.find()` y la prueba `"parte" in texto`.
- F-strings con alineación, separador de miles, decimales y porcentajes, como `f"{saldo:>10,.2f}"` y `f"{tasa:.1%}"`.

Los datos que identifican algo —cédulas, teléfonos, códigos— normalmente se guardan como texto aunque contengan dígitos. Así no se pierde un cero inicial y no se realizan operaciones matemáticas accidentalmente.

### Colecciones

| Tipo | Características y uso |
|---|---|
| `list` | Ordenada, mutable y permite repetidos. Útil para una secuencia que puede crecer o cambiar. |
| `tuple` | Ordenada e inmutable. Útil para datos agrupados que no se modificarán. |
| `dict` | Asocia claves únicas a valores; permite consultar, agregar y actualizar por clave. |
| `set` | Elementos únicos; útil para quitar duplicados y calcular unión, intersección o diferencia. No se debe depender de un orden de presentación. |

En listas se trabajan operaciones como `append`, `insert`, `remove`, `pop`, el acceso por índice, `len`, `sorted` y `in`. En diccionarios aparecen el acceso con corchetes, `.get(clave, valor_por_defecto)`, `.keys()` y la actualización de campos. Para una tupla se puede desempaquetar `a, b = datos`. Para conjuntos se usan operadores como `&` (intersección), `|` (unión), `-` (diferencia) y `^` (diferencia simétrica). `{}` crea un diccionario vacío; para un conjunto vacío se usa `set()`.

### Mutabilidad y referencias

Listas, diccionarios y conjuntos son mutables. Si `b = a` y `a` es una lista, ambas variables se refieren al mismo objeto; modificarlo mediante una se ve desde la otra. `.copy()` crea una copia superficial independiente para los cambios directos. `==` compara contenido; `is` comprueba identidad del objeto.

El notebook integra estos tipos en una ficha de socio con una lista de diccionarios de cuentas. Una comprensión como `[cuenta["saldo"] for cuenta in cuentas]` obtiene una lista de saldos sin escribir un ciclo independiente.

---

## 3. Decisiones y ciclos — Parte 1

**Notebook base:** [POO II - 1.3 Estructuras repetitivas - Parte 1](<POO II - 1.3 Estructuras repetitivas - Parte 1.ipynb>)

### `while`, contadores y acumuladores

`while condicion:` repite mientras la condición sea verdadera. Conviene cuando no se sabe de antemano cuántas repeticiones harán falta, por ejemplo, pedir un monto hasta que sea válido o ahorrar hasta alcanzar una meta.

- Un **contador** registra cuántas vueltas u operaciones hubo; normalmente aumenta de uno en uno.
- Un **acumulador** guarda un total que cambia en cada vuelta. Para sumas suele iniciar en `0`; para productos, en `1`.
- Hay que actualizar el estado que controla el ciclo. Si no se modifica una condición que sigue siendo verdadera, puede producirse un ciclo infinito.
- `while True` junto con `break` permite repetir al menos una vez y salir cuando se cumple una condición, como ingresar `"salir"`.

### `for` y `range`

`for` recorre una secuencia o colección. `range(inicio, fin, paso)` genera números; el límite final no se incluye. Por eso `range(1, 11)` recorre del 1 al 10. Un paso negativo permite contar hacia atrás.

Para recorrer una lista se recomienda `for deposito in depositos`. Si también hace falta la posición, `enumerate(depositos, start=1)` entrega posición y elemento. Esto suele ser más claro que recorrer índices manualmente.

### Control del ciclo

- `break` sale inmediatamente del ciclo.
- `continue` omite el resto de la vuelta actual y pasa a la siguiente.
- El `else` asociado a un ciclo se ejecuta si este termina sin haber salido mediante `break`. Es útil en una búsqueda para indicar que no se encontró el elemento.

Los ejemplos aplican estos patrones a depósitos, tablas de multiplicar, interés compuesto, validación de montos, retiros y una meta de ahorro que se alcanza después de un número variable de meses.

---

## 4. Diccionarios, ciclos anidados y comprensiones — Parte 2

**Notebook:** [POO II - 1.3 Estructuras repetitivas - Parte 2](<POO II - 1.3 Estructuras repetitivas - Parte 2.ipynb>)

### Recorrer y procesar datos

- `for clave in diccionario` recorre claves; `.values()` recorre valores; `.items()` entrega pares clave-valor.
- `diccionario.get(clave, 0)` permite contar elementos: se lee el conteo previo o cero y se incrementa.
- Una lista de diccionarios representa registros, por ejemplo, varios socios con nombre, saldo y estado.
- `zip(lista_a, lista_b)` empareja elementos y termina cuando acaba la colección más corta.
- `sorted(datos, key=..., reverse=True)` ordena y devuelve una lista nueva; `reversed(datos)` permite recorrer al revés. En el ejemplo, una función `lambda` usada como `key` indica qué campo determina el orden.

No se deben agregar o quitar claves a un diccionario mientras se está iterando sobre él. Si hace falta cambiar su estructura, se puede recorrer una copia o construir otro diccionario.

### Ciclos anidados y matrices

Un ciclo dentro de otro ejecuta todas las vueltas internas por cada vuelta externa. Si hay 3 filas y 4 columnas, se procesan 12 posiciones. Una lista de listas representa una matriz: el primer índice elige la fila y el segundo la columna.

Los ejemplos calculan totales por fila y por columna, construyen una tabla de depósitos por trimestre y buscan valores. `break` solo termina el ciclo más interno; una bandera permite que el ciclo externo también se detenga.

### Patrones y comprensiones

Los problemas con ciclos suelen consistir en contar, acumular, buscar, hallar extremos o filtrar. El notebook contrasta ciclos explícitos con herramientas como `sum`, `max`, `min`, `in`, `any` y `all`.

Una comprensión de lista tiene la forma `[expresion for elemento in coleccion if condicion]`. La condición filtra elementos; un `if/else` dentro de la expresión transforma cada elemento. También hay comprensiones de diccionarios `{clave: valor for ...}` y conjuntos `{expresion for ...}`. Si solo se necesita agregar o buscar un resultado, una expresión generadora como `sum(x for x in datos if ...)` evita crear una lista intermedia.

Una comprensión no es mejor si se vuelve difícil de leer o si necesita varios pasos, `break`, `print` o manejo de errores; en esos casos, es preferible un ciclo normal.

### Aplicaciones

La tabla de amortización introduce el sistema francés: calcula una cuota fija y, en cada período, separa el interés del capital amortizado. El cajero de consola combina `while`, decisiones, validación básica, movimientos y listas de tuplas. Esos mismos programas luego se reorganizan con funciones y manejo de excepciones.

---

## 5. Repasos de estructuras repetitivas

Estos archivos no agregan una unidad teórica nueva; sirven para practicar los contenidos de la sección anterior.

### Repaso completo

**Notebook:** [POO II - 1.3 Estructuras repetitivas - Repaso](<POO II - 1.3 Estructuras repetitivas - Repaso.ipynb>)

Repite prácticamente la explicación de la Parte 1: decisiones, `while`, contadores y acumuladores, `range`, recorridos, `enumerate`, `break`, `continue` y `else`. Incluye los problemas de clasificar edades, sumar pares e impares, procesar retiros y limitar intentos de una clave. El ejemplo de depósitos usa ocho valores, y la validación del crédito recoge edad, estado y deuda.

### Hoja de práctica

**Notebook:** [POO II - 1.3 Estructuras repetitivas - Repaso2](<POO II - 1.3 Estructuras repetitivas - Repaso2.ipynb>)

Es una práctica guiada: tiene celdas con consignas para completar y algunas soluciones para los ejercicios del final. Trabaja recorridos de listas, clasificación con `if`, `while` con validación y centinela, `range`, sumas, promedios, cuenta regresiva y Fibonacci. La actualización simultánea `a, b = b, a + b` permite avanzar la serie de Fibonacci sin una variable temporal adicional.

---

## 6. Ejercicios intermedios de los temas 1.1 y 1.2

**Notebook:** [POO II - 30 Ejercicios intermedios 1.1 y 1.2](<POO II - 30 Ejercicios intermedios 1.1 y 1.2.ipynb>)

Este cuaderno no introduce una unidad nueva; propone quince problemas de cálculos y formato y quince de cadenas, colecciones y tipos. Está pensado para practicar antes de incorporar condiciones y ciclos como herramientas principales.

### Bloque A: entrada, operaciones y presentación

Los problemas incluyen una factura con descuento e IVA, convertir segundos a `HH:MM:SS` usando `//` y `%`, notas ponderadas, interés simple, distancia entre puntos, conversiones de moneda, edades aproximadas, reparto de una cuenta, IMC, rol de pagos, velocidad, interés compuesto, consumo de combustible, separación e inversión de dígitos y conversión de puntajes.

La idea común es traducir cada enunciado a pasos: leer, convertir, calcular variables intermedias y presentar. El formato numérico de las f-strings controla decimales, porcentajes, alineación y separadores; no cambia el valor que se está calculando.

### Bloque B: texto, colecciones y datos compuestos

Los ejercicios practican:

- limpiar registros con `split`, `strip`, `join`, `title` y `lower`;
- construir usuario, correo e iniciales desde nombres;
- ocultar y agrupar números con *slicing*;
- analizar frases con `split`, `count`, `max(..., key=len)`, `replace` y rebanadas;
- generar códigos con `zfill`;
- editar listas y diccionarios, ordenar y resumir datos;
- acceder a listas de diccionarios y matrices;
- operar con conjuntos y tuplas;
- representar dinero con `Decimal`;
- validar condiciones simples mediante expresiones booleanas;
- explicar la diferencia entre alias y copia;
- convertir una línea de texto en una ficha con un diccionario anidado.

---

## 7. Funciones

**Notebook:** [POO II - 1.4 Funciones](<POO II - 1.4 Funciones.ipynb>)

### Definir, llamar y devolver

`def nombre(parametros):` define una función; llamarla ejecuta su bloque. Las funciones permiten nombrar una tarea y reutilizarla sin duplicar código.

- `print` muestra un resultado; `return` lo entrega a quien llamó la función para guardarlo, compararlo o usarlo en otro cálculo.
- Si una función no ejecuta `return`, el resultado devuelto es `None`.
- `return` termina la función, por lo que puede haber varios retornos para distintas ramas.

### Parámetros y resultados

Los argumentos pueden pasarse por posición o por nombre. Los parámetros con valor por defecto son opcionales y deben ubicarse después de los parámetros obligatorios. Evita usar listas o diccionarios mutables como valores por defecto: se comparten entre llamadas. El patrón seguro es usar `None` y crear la colección dentro de la función.

`return a, b` devuelve una tupla que puede desempaquetarse en dos variables. Una función también puede devolver `None` como señal de que no encontró un registro.

### Ámbito y herramientas adicionales

Una variable local se crea dentro de la función. Una variable global se define afuera; es posible leerla dentro, pero modificarla con `global` suele hacer el programa más difícil de probar. Es más claro pasar el valor como argumento y devolver el nuevo estado.

- `*args` reúne argumentos posicionales extra en una tupla.
- `**kwargs` reúne argumentos nombrados extra en un diccionario.
- Un docstring documenta la función. Las anotaciones (`monto: float -> float`) describen los tipos esperados, pero no fuerzan por sí solas esos tipos en tiempo de ejecución.
- `lambda` crea una función breve de una expresión. Es común usarla como clave de ordenamiento; para transformaciones y filtros simples, las comprensiones suelen ser más legibles.
- `assert` permite comprobar resultados esperados durante pruebas pequeñas.

El cajero del notebook se separa en funciones que validan, depositan, retiran, muestran el menú y coordinan las operaciones. Esa separación facilita probar cada regla por separado.

---

## 8. Excepciones

**Notebook:** [POO II - 1.5 Excepciones y archivos - Parte 1](<POO II - 1.5 Excepciones y archivos - Parte 1 (1).ipynb>)

Una excepción es un error que ocurre mientras se ejecuta el programa. Si no se maneja, Python detiene la ejecución y muestra un *traceback*. El tipo de excepción orienta la causa:

- `ValueError`: valor no aceptable para una operación, como convertir `"cien"` a `float`.
- `TypeError`: operación entre tipos incompatibles.
- `ZeroDivisionError`: división por cero.
- `IndexError` y `KeyError`: índice o clave inexistente.
- `NameError` y `AttributeError`: nombre o atributo no disponible.
- `FileNotFoundError`: se intenta abrir un archivo inexistente.

### Manejar y lanzar errores

El código que podría fallar se coloca dentro de `try`. Cada `except` debe capturar el tipo esperado y responder con un mensaje útil o recuperar el flujo. Se pueden capturar varios tipos en una tupla. Los casos específicos deben ir antes que los generales.

- `else` se ejecuta solo si el bloque `try` no produjo una excepción.
- `finally` se ejecuta tanto si hubo excepción como si no.
- `raise` lanza una excepción para avisar a quien llamó a la función que no se pudo completar una operación.
- Se puede definir una excepción propia heredando de `Exception`.

Para pedir datos repetidamente, el cuaderno combina `while True`, conversión dentro de `try/except`, validación de rango y `continue` o `return`. En una función que valida una regla de negocio, `raise ValueError(...)` deja que quien llama decida cómo presentar el error.

Evita `except:` vacío y `except: pass`: ocultan errores de programación. Usa excepciones específicas y limita el bloque `try` a las instrucciones que realmente pueden fallar.

**Alcance del archivo:** aunque el nombre del notebook menciona archivos, su contenido se centra en excepciones. El material concreto de lectura y escritura de archivos está en el notebook incluido dentro de `1.5. Archivos.zip`, descrito en la siguiente sección.

---

## 9. Archivos de texto

**Material:** notebook [POO II - 1.5 Archivos básicos - Ejercicios](<1.5. Archivos.zip>) y archivos de datos que están dentro del mismo ZIP.

### Abrir, leer y escribir

`open(nombre, modo, encoding="utf-8")` abre un archivo. El patrón `with open(...) as archivo:` cierra el archivo automáticamente al terminar el bloque, incluso si ocurre un error.

| Modo | Uso | Efecto |
|---|---|---|
| `"r"` | Leer | Falla con `FileNotFoundError` si no existe. |
| `"w"` | Escribir desde cero | Crea el archivo o reemplaza su contenido. |
| `"a"` | Agregar | Escribe al final sin borrar el contenido previo; lo crea si no existe. |

`write()` no agrega saltos de línea automáticamente; se escribe `"\n"` cuando se necesita terminar una línea. `read()` obtiene el contenido completo. Se puede recorrer el archivo con `for linea in archivo`, o usar `readlines()` para obtener una lista de líneas. Cada línea puede incluir `\n`, que `strip()` quita en los ejemplos.

Los datos leídos son texto. Para cálculos hay que convertir campos, por ejemplo `float(datos[1])`. El cuaderno enseña un formato sencillo de registros separados por comas: escribe una línea por registro y la divide con `split(",")`. Si el archivo no existe, `try/except FileNotFoundError` permite mostrar un mensaje y continuar.

Los ejercicios incrementales practican crear, leer, contar líneas, agregar productos, guardar tablas, buscar registros, calcular promedios, copiar solo aprobados y leer archivos con seguridad. El proyecto de biblioteca pide combinar estas operaciones con menú, funciones, validación y excepciones para persistir libros y préstamos.

---

## 10. Programación orientada a objetos básica

**Notebook:** [POO II - 1.6 POO con Python - Básico](<POO II - 1.6 POO con Python - Basico.ipynb>)

Una **clase** describe un tipo de objeto; un **objeto** es una instancia concreta que conserva sus propios datos. La comparación del notebook es un molde y las galletas que se hacen con él.

- `class Libro:` define la clase. `pass` permite dejar temporalmente el cuerpo vacío.
- `__init__` inicializa los datos al crear cada objeto.
- `self` representa la instancia actual, equivalente conceptual a `this` en Java. Python lo pasa automáticamente al llamar un método.
- Los **atributos** describen lo que tiene el objeto; se accede a ellos con punto, por ejemplo `libro.titulo`.
- Los **métodos** describen lo que hace el objeto. Pueden leer o modificar sus atributos y devolver valores con `return`.

El estado de cada instancia es independiente: prestar un libro cambia ese objeto, no los demás. Se pueden guardar muchos objetos de la misma clase en una lista y recorrerlos con `for`. El método especial `__str__` define una representación legible para `print(objeto)`, de manera similar al propósito de `toString()` en Java.

Los ejercicios del notebook aplican clases y métodos a mascotas, personas, círculos, contadores, productos, cuentas de ahorro, estudiantes y libros. El sistema de biblioteca es el reto más amplio.

---

## 11. Mapa general de los archivos revisados

| Material | Qué aporta |
|---|---|
| [Introducción a Python](<POO II - 1.1 Introduccion a Python.ipynb>) | Sintaxis inicial, entrada/salida, variables, operadores y decisiones. |
| [Variables y tipos](<POO II - 1.2 Variables y Tipos de Datos .ipynb>) | Tipos, cadenas, colecciones, mutabilidad y datos anidados. |
| [Estructuras repetitivas — Parte 1](<POO II - 1.3 Estructuras repetitivas - Parte 1.ipynb>) | Decisiones, `while`, `for`, `range` y control de ciclos. |
| [Estructuras repetitivas — Parte 2](<POO II - 1.3 Estructuras repetitivas - Parte 2.ipynb>) | Diccionarios, ciclos anidados, matrices, patrones y comprensiones. |
| [Repaso](<POO II - 1.3 Estructuras repetitivas - Repaso.ipynb>) | Repite Parte 1 con ejemplos de aplicación. |
| [Repaso 2](<POO II - 1.3 Estructuras repetitivas - Repaso2.ipynb>) | Hoja guiada de ejercicios sobre ciclos. |
| [30 ejercicios intermedios](<POO II - 30 Ejercicios intermedios 1.1 y 1.2.ipynb>) | Aplicación de cálculos, formato, texto y colecciones. |
| [Funciones](<POO II - 1.4 Funciones.ipynb>) | Modularización, parámetros, retornos, ámbito y pruebas. |
| [Excepciones](<POO II - 1.5 Excepciones y archivos - Parte 1 (1).ipynb>) | Captura y lanzamiento de errores. |
| [Archivos básicos (dentro del ZIP)](<1.5. Archivos.zip>) | Lectura, escritura, anexado y proyecto integrador de biblioteca. |
| [POO básica](<POO II - 1.6 POO con Python - Basico.ipynb>) | Clases, objetos, atributos, métodos y `__str__`. |

### Aclaraciones útiles al estudiar

- En el notebook introductorio se anuncia un ejemplo de concatenación que debería producir `TypeError`, pero la celda convierte el saldo con `str()` y por tanto no produce ese error. Para observarlo, se tendría que quitar esa conversión.
- En el ejercicio de cuatro errores de sintaxis de ese mismo notebook, el punto y coma final y los paréntesis alrededor de la condición son válidos en Python (aunque no sean necesarios). Los problemas que impiden ejecutar el ejemplo son las llaves y la falta de `:`.
- En el ejercicio 7 del notebook de 30 ejercicios, el año en que se cumplen 65 debe calcularse como `anio_nacimiento + 65`; la solución escrita usa `anio_actual + 65`, que no corresponde al enunciado.
- Los repasos de ciclos son material repetido y de práctica, no temas nuevos. El repaso 2 contiene varias celdas para completar; no todas las consignas tienen una solución desarrollada en el propio cuaderno.

---

# Ejercicios propuestos

Intenta resolverlos primero sin mirar otros códigos. Para cada uno, prueba al menos un caso normal y un caso límite.

## A. Un ejercicio para cada tema

### 1. Fundamentos: simulador de plazo fijo

Pide nombre del socio, monto y meses. Rechaza montos menores a $100. Aplica una tasa anual de 4 % para menos de 6 meses, 5,5 % de 6 a 11 meses y 7 % desde 12 meses. Calcula el interés simple y muestra capital, interés y total en una f-string con dos decimales.

### 2. Tipos y colecciones: depurar un registro

Dado el texto `"  0102030405 ;  ana pérez ;  120.50 ; ahorros "`, crea un diccionario con cédula como texto, nombre limpio en formato título, saldo como decimal y tipo de cuenta en minúsculas. Usa una lista para guardar tres registros. Muestra el total de saldos y los tipos de cuenta sin repetir.

### 3. Ciclos Parte 1: depósitos hasta una meta

Comienza con saldo cero. Pide depósitos hasta que la persona escriba `0`; rechaza los montos negativos, cuenta solo depósitos válidos y acumula el saldo. Al final informa cuántos depósitos se aceptaron y el total.

### 4. Ciclos Parte 2: resumen por cuenta

Dado un diccionario de cuentas y saldos, imprime cada par alineado, calcula el total y encuentra la cuenta de mayor saldo recorriendo el diccionario. Crea además un diccionario nuevo solo con las cuentas cuyo código empieza por `"AH"`.

### 5. Repasos de ciclos

Usa una lista de edades. Clasifica cada edad como menor, adulto o adulto mayor y muestra el número de personas por grupo. Después, pide hasta tres intentos de una clave y muestra si se permitió el acceso o se agotaron los intentos.

### 6. Ejercicios intermedios 1.1 y 1.2

Pide las ventas de cuatro productos. Guarda los nombres y los precios en estructuras adecuadas, calcula el subtotal, aplica un descuento del 8 % y un impuesto del 12 % sobre el subtotal descontado. Presenta el detalle alineado; calcula el total y el promedio de precio. Usa dos decimales en la salida.

### 7. Funciones

Escribe `calcular_resumen(movimientos)` que reciba una lista de montos y devuelva una tupla con total, promedio, máximo y mínimo. Si la lista está vacía, decide y documenta un resultado seguro. Escribe al menos tres `assert` para probar lista normal, un solo elemento y lista vacía.

### 8. Excepciones

Escribe `leer_monto_positivo()` que solicite un valor hasta recibir un número mayor que cero. Maneja texto no numérico con `ValueError` y vuelve a preguntar. Escribe también `retirar(saldo, monto)` que lance `ValueError` si el monto no es positivo o supera el saldo.

### 9. Archivos

Crea `movimientos.txt` con una línea por operación, cada línea con tipo y monto separados por coma. Luego vuelve a leerlo, convierte los montos a número, suma los depósitos y muestra el total de retiros. Si el archivo no existe al leer, presenta un mensaje claro.

### 10. POO básica

Crea una clase `Cuenta` con titular, número y saldo. Implementa `depositar`, `retirar` y `__str__`. El depósito debe ser positivo; el retiro no puede superar el saldo. Crea dos cuentas y comprueba que operar en una no altera el saldo de la otra.

## B. Ejercicios que mezclan temas

### 11. Cajero modular con historial

Implementa un menú que se repita hasta elegir salir. Separa las acciones en funciones. Permite consultar saldo, depositar y retirar; valida montos con excepciones y guarda cada movimiento en una lista. Al salir, imprime el historial y el saldo final.

**Combina:** entrada/salida, condiciones, ciclos, listas, funciones y excepciones.

### 12. Reporte de socios desde archivo

Lee un archivo con una línea por socio y campos separados por coma: nombre, cédula, tipo de cuenta y saldo. Limpia los campos, convierte saldo a número, almacena cada registro como diccionario y muestra una tabla. Calcula el saldo total, filtra cuentas de ahorro y maneja el caso de archivo inexistente.

**Combina:** archivos, cadenas, conversiones, colecciones, ciclos, formato y excepciones.

### 13. Biblioteca con objetos y persistencia

Modela un `Libro` con código, título, autor y estado. Implementa métodos para prestar y devolver solo cuando la transición sea válida. Guarda y carga los libros desde un archivo de texto. Añade un menú que permita listar, buscar, prestar, devolver y salir; captura errores de entrada y códigos inexistentes.

**Combina:** clases, objetos, métodos, listas, archivos, decisiones, ciclos y excepciones.

### 14. Crédito con tabla de amortización

Escribe una función que reciba monto, tasa anual y número de meses. Valida las entradas, calcula la cuota fija y devuelve una lista de diccionarios con cuota, interés, capital y saldo por período. Imprime la tabla y verifica que el saldo final sea aproximadamente cero.

**Combina:** funciones, ciclos, diccionarios, cálculos, validación y formato.

## C. Lista de comprobación antes de entregar

- ¿Convertí lo que devuelve `input()` antes de hacer cálculos?
- ¿Elegí texto para identificadores con ceros iniciales?
- ¿Usé `==` para comparar valores y `is None` para comprobar ausencia?
- ¿Mis ciclos avanzan y tienen una condición de salida?
- ¿Distingo `print` de `return`?
- ¿Capturo errores específicos y no oculto fallos con `except:` vacío?
- ¿Uso `with open(...)` para que los archivos se cierren automáticamente?
- ¿Cada objeto conserva su propio estado?
- ¿Probé entradas límite: vacío, cero, negativo, valor inexistente y valor no numérico?
