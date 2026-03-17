def check_temperature(temp_str) -> None:
    try:
        n: int = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        return
    if (n < 0):
        print(f"Error: {n}°C is too cold for plants (min 0°C)")
    elif (n > 40):
        print(f"Error: {n}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {n}°C is perfect for plants!")


def test_temperature_input() -> None:
    print("Testing temperature: 25")
    check_temperature('25')
    print()
    print("Testing temperature: abc")
    check_temperature('abc')
    print()
    print("Testing temperature: 100")
    check_temperature('100')
    print()
    print("Testing temperature: -50")
    check_temperature('-50')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
