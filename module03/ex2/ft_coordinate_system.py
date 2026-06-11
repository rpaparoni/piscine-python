import math


def get_player_pos() -> tuple:
    # Bucle infinito hasta que el usuario introduzca datos válidos
    valid: bool = False
    while not valid:
        user_input: str = input("Enter new coordinates as floats in format 'x,y,z': ")

        # Usamos el split normal, mucho más directo y limpio
        parts: list = user_input.split(',')

        # Si al cortar por las comas no nos quedan exactamente 3 trozos, está mal
        if len(parts) != 3:
            print("Invalid syntax")
        else:
            try:
                # Probamos la conversión a float uno por uno
                param: str = parts[0]
                x: float = float(parts[0])

                param = parts[1]
                y: float = float(parts[1])

                param = parts[2]
                z: float = float(parts[2])

                # Si llegamos aquí sin explotar, devolvemos la tupla ganadora
                return (x, y, z)

            except ValueError as error:
                # Capturamos el error oficial y limpiamos los espacios con strip()
                clean_param: str = param.strip()
                print(f"Error on parameter '{clean_param}': {error}")


def calc_distance(p1: tuple, p2: tuple) -> float:
    # Fórmula de distancia euclidiana 3D
    # (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2
    dx: float = (p2[0] - p1[0]) ** 2
    dy: float = (p2[1] - p1[1]) ** 2
    dz: float = (p2[2] - p1[2]) ** 2

    return math.sqrt(dx + dy + dz)


def main() -> None:
    print("=== Game Coordinate System ===")

    # 1. Primer set de coordenadas
    print("Get a first set of coordinates")
    p1: tuple = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    # 2. Distancia al centro exacto (0, 0, 0)
    center: tuple = (0.0, 0.0, 0.0)
    dist_to_center: float = calc_distance(center, p1)

    # Redondeamos a 4 decimales con la herramienta round()
    print(f"Distance to center: {round(dist_to_center, 4)}")

    # 3. Segundo set de coordenadas
    print("\nGet a second set of coordinates")
    p2: tuple = get_player_pos()

    # 4. Distancia final entre los dos puntos
    dist_between: float = calc_distance(p1, p2)
    print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    main()
