class Plant:
    def __init__(self, name: str, size: int, age: int):
        self.name: int = name
        self.size: int = size
        self.age: int = age


if __name__ == "__main__":

    plant_1 = Plant('Rose', 25, 30)
    plant_2 = Plant('Sunflower', 80, 45)
    plant_3 = Plant('Cactus', 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{plant_1.name}: {plant_1.size}cm, {plant_1.age} days old")
    print(f"{plant_2.name}: {plant_2.size}cm, {plant_2.age} days old")
    print(f"{plant_3.name}: {plant_3.size}cm, {plant_3.age} days old")
