import random


MASTER_ACHIEVEMENTS: list = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set:

    num_achievements: int = random.randint(5, 10)

    chosen: list = random.sample(MASTER_ACHIEVEMENTS, num_achievements)

    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set = gen_player_achievements()
    bob: set = gen_player_achievements()
    charlie: set = gen_player_achievements()
    dylan: set = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct: set = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")

    common: set = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print("")

    master_set: set = set(MASTER_ACHIEVEMENTS)
    print(f"Alice is missing: {master_set.difference(alice)}")
    print(f"Bob is missing: {master_set.difference(bob)}")
    print(f"Charlie is missing: {master_set.difference(charlie)}")
    print(f"Dylan is missing: {master_set.difference(dylan)}")


if __name__ == "__main__":
    main()
