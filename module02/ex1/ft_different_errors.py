def garden_operations() -> None:
    text: str = "abc"

    print("Testing ValueError...")
    try:
        int(text)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        open(missing.txt)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
