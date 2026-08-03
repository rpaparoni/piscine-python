# Conceptos Clave: Pydantic & Validación de Datos (Módulo 09)

Este documento resume los conceptos fundamentales que necesitas dominar para defender con éxito el módulo "Cosmic Data", centrado en la validación de datos usando **Pydantic (v2)**.

---

## 1. ¿Qué es Pydantic y por qué lo usamos?
Pydantic es la librería más utilizada en Python para la validación de datos y la gestión de configuraciones. 
En lugar de escribir decenas de condicionales (`if`) para comprobar si un dato es correcto (por ejemplo, si una edad es un número o si un texto está vacío), Pydantic automatiza este proceso basándose en las **anotaciones de tipo** (`type hints`) de Python.

**Sus superpoderes principales son:**
*   **Validación estricta:** Bloquea los datos que no cumplen las reglas y lanza errores detallados (`ValidationError`).
*   **Conversión automática (Coerción):** Si Pydantic espera un número entero y recibe el texto `"42"`, es lo suficientemente inteligente para convertirlo automáticamente al número `42`. Lo mismo ocurre con las fechas (convierte strings a objetos `datetime`).

---

## 2. Herramientas Base: `BaseModel` y `Field`

### `BaseModel`
Es la clase fundacional de Pydantic. Para crear un modelo de validación, tu clase debe heredar de `BaseModel`. Esto le otorga a tu clase todas las funcionalidades de validación automática.

### `Field`
Es una función que permite añadir reglas de validación específicas a un atributo individual de tu modelo, más allá de su simple tipo de dato.
*   **Límites numéricos:** `ge` (mayor o igual que), `le` (menor o igual que), `gt` (estrictamente mayor que), `lt` (estrictamente menor que).
*   **Límites de texto:** `min_length`, `max_length`.
*   **Valores por defecto:** `default=True` (si el usuario no introduce el dato, se asume este valor).
*   **Campos Obligatorios (`...`):** Usar `Field(...)` (los tres puntos o *Ellipsis*) indica que ese campo es estrictamente obligatorio y no tiene un valor por defecto.

---

## 3. Tipos Especiales de Datos

### `Enum`
Sirve para restringir una variable a un conjunto cerrado de opciones predefinidas. En el Ejercicio 1, lo usamos para asegurar que el `contact_type` solo pudiera ser `radio`, `visual`, `physical` o `telepathic`. Evita que entren datos inesperados por errores tipográficos.

### `Optional`
Importado del módulo `typing`, se usa para indicar que un campo puede recibir un valor del tipo especificado o simplemente estar vacío (`None`). Por ejemplo, `Optional[str]` significa que el campo espera un texto, pero si no se proporciona nada, el sistema lo aceptará como válido.

---

## 4. Validaciones Complejas: `@model_validator`

A veces, las validaciones de `Field` no son suficientes, especialmente cuando una regla **depende de la combinación de dos o más variables**. 

Para esto usamos el decorador `@model_validator(mode='after')` de Pydantic v2.
*   **`mode='after'`:** Indica que esta validación personalizada debe ejecutarse *después* de que Pydantic haya comprobado y convertido los tipos de datos básicos.
*   **La lógica:** Dentro de la función decorada, usamos condicionales `if` normales de Python. Si detectamos que los datos rompen una regla de negocio, lanzamos un `ValueError`.
*   **El retorno:** Si el modelo pasa todas las comprobaciones sin levantar ningún error, la función debe devolver `self` (el propio objeto validado).

---

## 5. Modelos Anidados (Nested Models)

Un concepto avanzado que aparece en el Ejercicio 2. Pydantic permite que un modelo de datos contenga a otro modelo de datos.
Por ejemplo, si tienes un modelo `CrewMember` (que valida a un astronauta individual) y un modelo `SpaceMission` (que valida la misión general), puedes definir que la misión contenga una lista de astronautas:
`crew: List[CrewMember]`

La gran ventaja del anidamiento es que Pydantic validará primero, y de forma automática, a cada uno de los miembros individuales de esa lista. Si un solo astronauta tiene datos incorrectos, la misión entera será rechazada antes de aplicar reglas más complejas.

---

## 6. Manejo de Errores: `ValidationError`

Cuando Pydantic detecta que un dato incumple las reglas, lanza una excepción llamada `ValidationError`. 
En el mundo real (y en las funciones `main()` de los ejercicios), nunca dejamos que este error "rompa" el programa. Lo capturamos usando un bloque `try...except ValidationError as e` para poder mostrar por pantalla un mensaje limpio y controlado indicando exactamente qué falló.
