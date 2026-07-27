import abc


class Creature(abc.ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self._name: str = name
        self._type: str = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

