from sys import base_prefix, prefix, executable
from os import path
from site import getsitepackages


def is_this_the_matrix() -> None:

    if base_prefix != prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(
            f"Current Python: {executable}\n"
            f"Virtual Environment: {path.basename(prefix)}\n"
            f"Environment Path: {prefix}\n"
            "\nSUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
            "\nPackage installation path:\n"
            f"{getsitepackages()[0]}"
            )
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {executable}")
        print("Virtual Environment: None detected")

        print(
            "\nTo enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
            )


if __name__ == "__main__":
    is_this_the_matrix()
