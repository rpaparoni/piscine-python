class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, amount: int) -> None:
        if amount >= 0:
            self._height = amount
            print(f"Height updated: {amount}cm [OK]")
        else:
            print(f"height {amount}cm [REJECTED]")

    def set_age(self, amount: int) -> None:
        if amount >= 0:
            self._age = amount
            print(f"Age updated: {amount} days [OK]")
        else:
            print("[REJECTED]")


if __name__ == "__main__":

    rose = SecurePlant('Rose', 0, 0)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)

    print("\nInvalid operation attempted: ", end="")
    rose.set_height(-5)
    print("Security: Negative height rejected\n")
    print(f"Current plant: {rose.name} ", end="")
    print(f"({rose.get_height()}cm, {rose.get_age()} days)")
