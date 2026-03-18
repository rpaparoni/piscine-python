class GardenManager:
    def __init__(self) -> None:
        self.inventory: dict = {}

    def add_plant(self, plant_list: list) -> None:
        error: str

        try:
            if plant_list[0] is None:
                error = "Error: Plant name cannot be empty!"
                raise ValueError(error)
        except ValueError as error:
            print(error)
        else:
            name: str = plant_list[0]
            self.inventory[name] = [plant_list[1], plant_list[2]]
            print(f"Added {name} successfully")

    def check_plants(self, plant_name: str) -> None:
        error: str

        try:
            if plant_list[1] > 10:
                error = (
                    f"Error: Water level {plant_list[1]} "
                    "is too high (max 10)"
                )
                raise ValueError(error)
            elif plant_list[2] < 2:
                error = (
                    f"Error: Sunlight hours {plant_list[2]} "
                    "is too low (min 2)"
                )
                raise ValueError(error)
        except ValueError as error:
            print(error)
        else:
            print(f"{self.inventory[plant_name]} healthy")


def test_garden_management() -> None:

    garden = GardenManager()
    tomato: list = ['tomato', 5, 8]

    print("Adding plants to garden...")
    GardenManager.add_plant(garden, tomato)
    print("\nChecking plant health...")
    GardenManager.check_plants()

if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
