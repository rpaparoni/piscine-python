def water_plants(plant_list: list) -> None:

    i: int = 0

    print("Opening watering system")
    try:
        while i < len(plant_list):
            if plant_list[i] is None:
                raise ValueError
            print(f"Watering {plant_list[i]}")
            i += 1
    except ValueError:
        print(f"Error: Cannot water {plant_list[i]} - invalid plant!")
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:

    good_list: list = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    bad_list: list = [
        "tomato",
        None
    ]
    water_plants(good_list)
    water_plants(bad_list)


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
