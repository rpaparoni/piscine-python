def secure_archive(filen: str, action: str = "r", content: str = "") -> tuple:
    try:
        with open(filen, action) as vault_file:

            if action == "r":

                read_content: str = vault_file.read()

                return (True, read_content)

            elif action == "w":

                vault_file.write(content)
                return (True, "Content successfully written to file")

    except Exception as error:
        return (False, f"{error}")
    return (False, "Invalid action")

def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test.txt"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("test2.txt"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", "texto texto texto"))


if __name__ == "__main__":
    main()
