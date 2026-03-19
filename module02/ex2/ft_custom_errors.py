# los errores van dentro de la clase
class GardenError(Exception):
    def __init__(self, text: str) -> None:
        super().__init__(text)


class PlantError(GardenError):
    def __init__(self, text: str) -> None:
        super().__init__(text)


class WaterError(GardenError):
    def __init__(self, text: str) -> None:
        super().__init__(text)

# test_error_types()
if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    print("\nAll custom error types work correctly!")
