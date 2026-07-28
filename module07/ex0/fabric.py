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


class CreatureFactory(abc.ABC):
    """
    Plano maestro para las fábricas de criaturas.
    """
    @abc.abstractmethod
    def create_base(self) -> Creature:
        """
        Debe devolver la versión base de la criatura.
        """
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        """
        Debe devolver la versión evolucionada de la criatura.
        """
        pass