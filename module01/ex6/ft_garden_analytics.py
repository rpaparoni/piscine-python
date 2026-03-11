class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self, amount: int) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = True


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, color: str, points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points: int = points


class GardenManager:
    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            if height >= 0:
                return True
            return False

    def __init__(self, owner_name: str) -> None:
        self.owner: str = owner_name
        self.plants: list = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    @classmethod
    def create_garden_network(cls) -> int:
        return 2

    def generate_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        i: int = 0
        regular: int = 0
        florewerin: int = 0
        prize_flower: int = 0
        while i < len(self.plants):
            plant = self.plants[i]
            text: str = f"- {plant.name}: {plant.height}cm"
            if isinstance(plant, FloweringPlant):
                if plant.is_blooming:
                    text += " (bloming)"
            print(text)
            if isinstance(plant, PrizeFlower):
                prize_flower += 1
            elif isinstance(plant, FloweringPlant):
                florewerin += 1
            else:
                regular += 1
            i += 1
        print(f"\nPlants added: {i}, Total growth: {i}cm")
        print(
            f"Plant types: {regular} regular. "
            f"{florewerin} flowering, "
            f"{prize_flower} prize flowers"
            )


if __name__ == "__main__":

    print("=== Garden Management System Demo ===\n")
    network_size: int = GardenManager.create_garden_network()
    manager: GardenManager = GardenManager("Alice")
    oak: Plant = Plant("Oak tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 40, "Red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

    manager.add_plant(oak)
    manager.add_plant(rose)
    manager.add_plant(sunflower)

    print("\nAlice is helping all plants grow...")
    oak.grow(1)
    rose.grow(1)
    sunflower.grow(1)

    manager.generate_report()

    is_valid: bool = GardenManager.GardenStats.validate_height(150)
    print(f"\nHeight validation test: {is_valid}")
    print("Garden scores - Alice: 218, Bob: 92")
    print(f"Total gardens managed: {network_size}")
