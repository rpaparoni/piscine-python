from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.ability import HealCapability, TransformCapability


class StrategyError(Exception):
    def __init__(self, creature_name: str, strategy_name: str) -> None:
        self.message = f"Invalid Creature '{creature_name}' "
        "for this {strategy_name} strategy"
        super().__init__(self.message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            StrategyError(creature.name, "normal")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature.name, "aggressive")

        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature.name, "defensive")

        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
