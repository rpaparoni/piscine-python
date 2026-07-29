from ex0 import CreatureFactory, Creature
from .ability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self):
        return f"{self.name} heals itself and others for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", " Grass/Fairy")

    def attack(self):
        return f"{self.name} uses Petal Dance!"

    def heal(self):
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.is_trans = False

    def attack(self):
        if self.is_trans is False:
            return f"{self.name} atacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self):
        self.is_trans = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.is_trans = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_trans = False

    def attack(self):
        if self.is_trans is False:
            return f"{self.name} atacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        self.is_trans = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        self.is_trans = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
