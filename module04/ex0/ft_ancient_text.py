import sys


def read_ancient_fragment(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file_to_read = open(filename, "r")
        print("---\n")

        text = file_to_read.read()
        print(f"{text}")

        file_to_read.close()
        print("\n---")
        print(f"File '{filename}' closed.")

    except Exception as error:
        print(f"Error opening file '{filename}': {error}")


def main() -> None:
    if len(sys.argv) == 2:
        file_argument: str = sys.argv[1]
        read_ancient_fragment(file_argument)
    else:
        print("Usage: python3 ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
