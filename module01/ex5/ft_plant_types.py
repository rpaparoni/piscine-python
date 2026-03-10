class Plant:
    def __init__(self, name: str, size: int, age: int) -> None:
        self.name: int = name
        self.size: int = size
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, size: int, age: int, color: str) -> None:
        super().__init__(name, size, age)
        self.color: str = color

    def bloom(self) -> None:
        print("Rose is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, size: int, age: int, d: int, s: int) -> None:
        super().__init__(name, size, age)
        self.diameter: int = d
        self.square_meters: int = s

    def produce_shade(self) -> None:
        print(f"Oak provides {self.square_meters} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, size: int, age: int, s: str, n: str) -> None:
        super().__init__(name, size, age)
        self.harvest_season: str = s
        self.nutritional_value: str = n


if __name__ == "__main__":

    plant_1 = Flower("Rose", 25, 30, "red")
    plant_2 = Tree("Oak", 500, 1825, 50, 78)
    plant_3 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print("=== Garden Plant Types ===\n")

    print(
        f"{plant_1.name} (Flower): {plant_1.size}cm, "
        f"{plant_1.age} days, {plant_1.color} color"
    )
    plant_1.bloom()

    print(
        f"{plant_2.name} (Tree): {plant_2.size}cm, "
        f"{plant_2.age} days, {plant_2.diameter}cm diameter"
    )
    plant_2.produce_shade()

    print(
        f"{plant_3.name} (Vegetable): {plant_3.size}cm, "
        f"{plant_3.age} days, {plant_3.harvest_season} harvest"
    )
    print(f"{plant_3.name} is rich in {plant_3.nutritional_value}")
