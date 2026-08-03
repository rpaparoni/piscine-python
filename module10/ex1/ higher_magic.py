from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return f"Combined spell result: {spell1()}, {spell2()}"


if __name__ == "__main__":
    print("Testing spell combiner...")
    print(f"{spell_combiner()}")
