from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} damage"


def teleport(target: str, power: int) -> str:
    return f"{target} has been teleported {power} km away"


def invulnerability(target: str, power: int) -> str:
    return f"{target} now have {power} more defense"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]

    return sequence_spell


if __name__ == "__main__":
    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    res1, res2 = combo("Dragon", 20)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_tp = power_amplifier(teleport, 10)
    print(f"Original: {teleport('Wich', 10)}")
    print(f"Amplified (10x): {mega_tp('Wich', 10)}")

    print("\nTesting conditional caster...")
    dragon_fireball = conditional_caster(is_dragon, fireball)
    print(f"Targeting Dragon: {dragon_fireball('Dragon', 50)}")
    print(f"Targeting Goblin: {dragon_fireball('Goblin', 50)}")

    print("\nTesting spell sequence...")
    multi_cast = spell_sequence([fireball, heal])
    print(f"Sequence results: {multi_cast('Dragon', 15)}")
