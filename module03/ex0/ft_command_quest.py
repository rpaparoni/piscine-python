import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    i: int = 0
    number_of_arguments: int = len(sys.argv)
    if number_of_arguments == 1:
        print("No arguments provided!")
    elif number_of_arguments > 2:
        sys.argv[0] = "ft\\_command\\_quest.py"
    print(f"Arguments received: ")
    while i < len(sys.argv):
        print(f"")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {number_of_arguments}")
