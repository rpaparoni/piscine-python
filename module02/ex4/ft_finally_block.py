class GardenError(Exception):
    def __init__(self, text: str = "Unknown garden error") -> None:
        super().__init__(text)


class PlantError(GardenError):
    def __init__(self, text: str = "Unknown garden error") -> None:
        super().__init__(text)


def water_plants(plant_name: str) -> None:
    error: str

    if plant_name != plant_name.capitalize():
        error = f" Invalid plant name to water: {plant_name}"
        raise PlantError(error)
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    try:
        water_plants("Tomato")
        water_plants("Lettuce")
        water_plants("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants...")
    try:
        water_plants("Tomato")
        water_plants("lettuce")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
