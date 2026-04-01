def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    print("\nInput data is '25'")
    try:
        temp_valid: int = input_temperature("25")
        print(f"Temperature is now {temp_valid}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nInput data is 'abc'")
    try:
        temp_invalid: int = input_temperature("abc")
        print(f"Temperature is now {temp_invalid}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
