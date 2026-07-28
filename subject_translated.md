# DataDeck: Abstract Card Architecture

## Introducción

¡Bienvenido, aspirante a Arquitecto de Mazos, al mundo de DataDeck!

Imagina esto: estás diseñando un juego de cartas basado en criaturas inspirado en juegos populares de recolección de monstruos. Tus cartas no son objetos estáticos; son entidades de datos dinámicas que se agrupan en familias y poseen capacidades que se utilizan de forma estratégica. El reto es: ¿cómo crear un sistema lo suficientemente flexible como para manejar miles de tipos de cartas diferentes manteniendo un código limpio y mantenible?

¡El secreto está en los **Abstract Programming Patterns** (Patrones de Programación Abstracta)! Anteriormente ya has manipulado clases abstractas y polimorfismo. Ahora utilizaremos patrones más avanzados: *abstract factories* (fábricas abstractas), *capabilities* (capacidades adicionales) y *strategy patterns* (patrones de estrategia).

---

## Instrucciones Generales

*   Debe escribirse en **Python 3.10** o superior.
*   Debe seguir el estándar de código **flake8**.
*   Todo el código debe tener type annotations, verificables con **mypy**.
*   Clases estándar, colecciones y funciones built-in están autorizadas (salvo `eval()` y `exec()`).
*   No usar librerías externas.
*   Es **OBLIGATORIO** incluir un archivo `__init__.py` en cada carpeta de ejercicio. Los scripts de prueba estarán en la raíz del repositorio.

---

## Ejercicio 0: Creature Factory

*   **Directorio:** `ex0/`
*   **Archivos a entregar:** `battle.py`, `ex0/` como un paquete con todos sus archivos necesarios.
*   **Autorizados:** `builtins`, tipos estándar, `import typing`, `import abc`.

Vamos a empezar creando las cartas básicas de `Creature`. Como sabrás, se clasifican en familias y pueden evolucionar. Este ejercicio se centra en el patrón de diseño **abstract factory**. Debes implementar en la carpeta `ex0/`:

*   Una clase abstracta `Creature` que almacena los atributos para el nombre y tipo, un método abstracto `attack` y un método concreto `describe` que devuelva un mensaje estándar usando el nombre y tipo.
*   Las siguientes clases concretas que heredan de `Creature`: `Flameling`, `Pyrodon`, `Aquabub`, y `Torragon`. Su método `attack` devolverá un mensaje de string apropiado (ver ejemplo).
*   Una clase abstracta `CreatureFactory` que te permitirá crear a la `Creature` base y a la `Creature` evolucionada de la misma familia, usando los métodos abstractos `create_base` y `create_evolved`.
*   Las clases concretas `FlameFactory` y `AquaFactory` (que heredan de `CreatureFactory`), que manejarán la creación de las versiones base y evolucionada para cada familia (respectivamente `Flameling` y `Pyrodon` para `FlameFactory`, y `Aquabub` y `Torragon` para `AquaFactory`).
*   Tu paquete `ex0` **no puede exponer** las clases concretas `Creature` de forma directa, sólo debe exponer las *factories*.

El script `battle.py` (en la raíz) probará tu paquete:
1.  Instancia `FlameFactory` y `AquaFactory`.
2.  Usa una única función que reciba el objeto *factory* y verifique que puede crear la versión base y evolucionada, y que pueden ser descritas y atacar.
3.  Usa otra función que reciba ambas fábricas y haga pelear a las criaturas base.

---

## Ejercicio 1: Capabilities

*   **Directorio:** `ex1/`
*   **Archivos a entregar:** `capacitor.py`, `ex1/` como paquete.
*   **Autorizados:** `builtins`, tipos estándar, `import typing`, `import abc`.

¡Vamos a añadir capacidades a nuestras criaturas! Como algún día estas capacidades podrían aplicar a otras cosas, **las clases abstractas de capacidades no deben heredar de la clase base `Creature`**.

En el paquete `ex1/` implementarás:
*   Una clase abstracta `HealCapability` que define un método abstracto `heal` (puede tomar un parámetro "target" si lo deseas).
*   Una clase abstracta `TransformCapability` que define los métodos abstractos `transform` y `revert`. Usa un atributo para que el estado persista y afecte a la implementación de `attack` de una criatura con esta capacidad.
*   Los métodos de estas capacidades solo devolverán strings descriptivos.
*   Clases concretas que heredan de **ambas**, `Creature` y `HealCapability`: `Sproutling` y `Bloomelle` (misma familia, expuestas a través de `HealingCreatureFactory`).
*   Clases concretas que heredan de **ambas**, `Creature` y `TransformCapability`: `Shiftling` y `Morphagon` (misma familia, expuestas a través de `TransformCreatureFactory`).
*   Igual que antes, no expongas las criaturas directamente, solo las *factories*. (Usa el paquete `ex0` como base).

Script `capacitor.py` (en la raíz) prueba el funcionamiento llamando a las fábricas y métodos nuevos (`heal`, `transform`, `revert`).

---

## Ejercicio 2: Abstract Strategy

*   **Directorio:** `ex2/`
*   **Archivos a entregar:** `tournament.py`, `ex2/` como paquete.
*   **Autorizados:** `builtins`, tipos estándar, `import typing`, `import abc`.

Necesitamos código de batalla capaz de entender las capacidades de cada criatura usando el **abstract strategy pattern**.

En el paquete `ex2/` implementarás:
*   Una clase abstracta `BattleStrategy` que define los métodos abstractos `act` e `is_valid`. `is_valid` devuelve un `bool` indicando si la `Creature` es apta para esa estrategia, y el método `act` será llamado por el script del torneo.
*   Tres clases concretas que heredan de `BattleStrategy`:
    *   `NormalStrategy`: para cualquier `Creature`, simplemente usa `attack`.
    *   `AggressiveStrategy`: para cualquier `Creature` con capacidad de transformación (hace `transform`, `attack`, `revert`).
    *   `DefensiveStrategy`: para cualquier `Creature` con capacidad de curación (hace `attack`, luego `heal`).
*   Si se prueba una combinación criatura-estrategia inválida, `is_valid` devuelve `False`. Si se llama a `act` en una combinación inválida, se levanta una excepción con un mensaje claro.

El script `tournament.py` creará las fábricas y estrategias, y utilizará una función `battle` que reciba los oponentes como tuplas `(CreatureFactory, BattleStrategy)`, haciéndolos pelear todos contra todos gestionando los errores correctamente.
