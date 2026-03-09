class Plant:
    def __init__(self, name: str, size: int, age: int) -> None:
        self.name = name
        self.size = size
        self.age = age

    def grow_size(self, amount: int) -> None:
        self.size += amount

    def grow_age(self, amount: int) -> None:
        self.age += amount

    def get_info(self) -> None:
        print(f"{self.name}: {int(self.size)}cm, {self.age} days old")


if __name__ == "__main__":

    plant_1 = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    Plant.get_info(plant_1)
    Plant.grow_age(plant_1, 6)
    Plant.grow_size(plant_1, 6)
    print("=== Day 7 ===")
    Plant.get_info(plant_1)
    print("Growth this week: +6cm")
