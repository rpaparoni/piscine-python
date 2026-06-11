def input_temperature(temp_str: str) -> int:
    n: int = int(temp_str)
    error: str

    if n < 0:
        error = f"{n}°C is too cold for plants (min 0°C)"
        raise ValueError(error)
    elif n > 40:
        error = f"{n}°C is too hot for plants (max 40°C)"
        raise ValueError(error)

    print(f"Temperature is now {n}°C")
    return n


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    temp: int = 0
    print("\nInput data is '25'")
    try:
        temp: int = input_temperature("25")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nInput data is 'abc'")
    try:
        temp = input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nInput data is '100'")
    try:
        temp = input_temperature("100")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nInput data is '-50'")
    try:
        temp = input_temperature("-50")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    if isinstance(temp, int):
        print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
