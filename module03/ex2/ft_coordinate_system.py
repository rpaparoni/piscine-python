import math


def get_player_pos() -> tuple:
    valid: bool = False
    while not valid:
        user_input: str = input("Enter new coordinates as"
                                "floats in format 'x,y,z': ")

        parts: list = user_input.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
        else:
            try:
                param: str = parts[0]
                x: float = float(parts[0])

                param = parts[1]
                y: float = float(parts[1])

                param = parts[2]
                z: float = float(parts[2])

                return (x, y, z)

            except ValueError as error:
                clean_param: str = param.strip()
                print(f"Error on parameter '{clean_param}': {error}")
    return (0.0, 0.0, 0.0)


def calc_distance(p1: tuple, p2: tuple) -> float:

    dx: float = (p2[0] - p1[0]) ** 2
    dy: float = (p2[1] - p1[1]) ** 2
    dz: float = (p2[2] - p1[2]) ** 2

    result: float = math.sqrt(dx + dy + dz)
    return result


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    p1: tuple = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    center: tuple = (0.0, 0.0, 0.0)
    dist_to_center: float = calc_distance(center, p1)

    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("\nGet a second set of coordinates")
    p2: tuple = get_player_pos()

    dist_between: float = calc_distance(p1, p2)
    print("Distance between the 2 sets of coordinates: ")
    print(f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
