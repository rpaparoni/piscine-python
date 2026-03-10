class Plant:
    def __init__(self, name: str, size: int, age: int) -> None:
        self.name: int = name
        self.size: int = size
        self.age: int = age

    def get_info(self) -> str:
        return f"{self.name} ({self.size}cm, {self.age} days)"


if __name__ == "__main__":

    plants_list: list = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]

    print("=== Plant Factory Output ===")

    i: int = 0
    while i < 5:
        new = Plant(plants_list[i][0], plants_list[i][1], plants_list[i][2])
        print(f"Created: {new.get_info()}")
        i += 1

    print(f"Total plants created: {i}")
