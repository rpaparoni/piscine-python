import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    i: int = 1
    number_of_arguments: int = len(sys.argv) - 1
    if number_of_arguments == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {number_of_arguments}")
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {number_of_arguments + 1}")
