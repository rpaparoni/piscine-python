class WaterError(Exception):
    def __init__(self, text: str) -> None:
        super().__init__(text)


class GardenManager:
    def __init__(self) -> None:
        self.inventory: dict = {}

    def add_plant(self, plant_list: list) -> None:
        error: str

        try:
            if plant_list[0] is None:
                error = "Error adding plant: Plant name cannot be empty!"
                raise ValueError(error)
        except ValueError as error:
            print(error)
        else:
            name: str = plant_list[0]
            self.inventory[name] = [plant_list[1], plant_list[2]]
            print(f"Added {name} successfully")

    def water_plants(self) -> None:
        plants: list = list(self.inventory.keys())
        i: int = 0

        try:
            print("Opening watering system")
            while i < len(plants):
                print(f"Watering {plants[i]} - success")
                i += 1
        except ValueError:
            print("there is not a plant")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants(self, plant_name: str) -> None:
        error: str

        try:
            data: list = self.inventory[plant_name]

            if data[0] > 10:
                error = (
                    f"Error checking {plant_name}: Water level {data[0]} "
                    "is too high (max 10)"
                )
                raise ValueError(error)
            elif data[1] < 2:
                error = (
                    f"Error: Sunlight hours {data[1]} "
                    "is too low (min 2)"
                )
                raise ValueError(error)
        except KeyError:
            print(f"Error: {plant_name} is not in the garden!")
        except ValueError as error:
            print(error)
        else:
            print(
                f"{plant_name}: healthy "
                f"(water: {data[0]}, sun: {data[1]})"
            )


def test_garden_management() -> None:

    garden = GardenManager()
    tomato: list = ['tomato', 5, 8]
    lettuce: list = ['lettuce', 15, 8]
    empty: list = [None]

    print("Adding plants to garden...")
    garden.add_plant(tomato)
    garden.add_plant(lettuce)
    garden.add_plant(empty)
    print("\nWatering plants...")
    GardenManager.water_plants(garden)
    print("\nChecking plant health...")
    GardenManager.check_plants(garden, tomato[0])
    GardenManager.check_plants(garden, lettuce[0])
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught  GardenError: {error}")
    finally:
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
    print("\nGarden management system test complete!")