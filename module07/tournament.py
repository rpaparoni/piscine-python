from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            fighter1 = factory1.create_base()
            fighter2 = factory2.create_base()

            print("\n* Battle *")
            print(fighter1.describe())
            print(" vs.")
            print(fighter2.describe())
            print(" now fight!")

            try:
                strategy1.act(fighter1)
                strategy2.act(fighter2)
            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggro_strat = AggressiveStrategy()
    def_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive)]")
    roster_basic: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, normal_strat),
        (heal_factory, def_strat)
    ]
    battle(roster_basic)

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    roster_error: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, aggro_strat),
        (heal_factory, def_strat)
    ]
    battle(roster_error)

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    roster_multiple: list[tuple[CreatureFactory, BattleStrategy]] = [
        (aqua_factory, normal_strat),
        (heal_factory, def_strat),
        (transform_factory, aggro_strat)
    ]
    battle(roster_multiple)
