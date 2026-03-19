def garden_operations() -> None:
    text: str = "abc"
    dic: dict = {"rose": "red"}

    print("Testing ValueError...")
    try:
        int(text)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        dic["tree"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    print("Testing multiple errors together...")
    try:
        int(text) / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

# test_error_types() 
if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")
