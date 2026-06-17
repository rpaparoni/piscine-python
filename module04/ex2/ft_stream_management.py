import sys
import typing


def archive_creation(filename: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file_to_read: typing.IO = open(filename, "r")
        print("---\n")

        original_lines: list = []
        for line in file_to_read:
            print(line, end="")
            original_lines += [line]

        file_to_read.close()
        print("\n\n---")
        print(f"File '{filename}' closed.\n")

        print("Transform data:")
        print("---\n")
        new_content: str = ""

        for line in original_lines:
            if line.endswith("\n"):
                new_line: str = line[:-1] + "#\n"
            else:
                new_line: str = line + "#\n"

            print(new_line, end="")
            new_content += new_line

        print("\n---")
        print("Enter new file name (or empty): ", end="")

        sys.stdout.flush()
        raw_input: str = sys.stdin.readline()
        new_filename = raw_input.strip()

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            new_file: typing.IO = open(new_filename, "w")
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{new_filename}'.")
    except Exception as error:
        print(f"Error opening file '{filename}': {error}")


def main() -> None:
    if len(sys.argv) == 2:
        file_argument: str = sys.argv[1]
        archive_creation(file_argument)
    else:
        print("Usage: python3 ft_archive_creation.py <file>")


if __name__ == "__main__":
    main()