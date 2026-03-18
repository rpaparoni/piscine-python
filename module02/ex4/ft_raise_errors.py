def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:

    error: str

    try:
        if plant_name is None:
            error = "Error: Plant name cannot be empty!"
            raise ValueError(error)
        elif water_level > 10:
            error = (
                f"Error: Water level {water_level} "
                "is too high (max 10)"
            )
            raise ValueError(error)
        elif sunlight_hours < 2:
            error = (
                f"Error: Sunlight hours {sunlight_hours} "
                "is too low (min 2)"
            )
            raise ValueError(error)
    except ValueError as error:
        print(error)
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:

    print("Testing good values...")
    check_plant_health('tomato', 10, 10)
    print("\nTesting empty plant name...")
    check_plant_health(None, 10, 10)
    print("\nTesting bad water level...")
    check_plant_health('carrot', 15, 10)
    print("\nTesting bad sunlight hours...")
    check_plant_health('beens', 10, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
