from alchemy.potions import strength_potion
from ..elements import create_air
import elements


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
        f"'{strength_potion()}' mixed with '{elements.create_fire()}'"
    )
