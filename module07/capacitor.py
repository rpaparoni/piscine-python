from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.ability import HealCapability, TransformCapability
from ex0 import CreatureFactory


def test_1(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())
    print(" envolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_2(factory: CreatureFactory) -> None:
    print("\nTesting Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.revert())
    print(" envolved:")
    envolved = factory.create_evolved()
    print(envolved.describe())
    print(envolved.attack())
    if isinstance(envolved, TransformCapability):
        print(envolved.transform())
    print(envolved.attack())
    if isinstance(envolved, TransformCapability):
        print(envolved.revert())


if __name__ == "__main__":
    healers_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()
    test_1(healers_factory)
    test_2(trans_factory)
