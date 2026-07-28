from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory


def test_1(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" envolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_2(factory: CreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())


if __name__ == "__main__":
    healers_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()
    test_1(healers_factory)
    test_2(trans_factory)
