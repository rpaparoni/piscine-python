import random

# Creamos la lista maestra fuera para poder usarla en ambas funciones
MASTER_ACHIEVEMENTS: list = [
    "Crafting Genius", "World Savior", "Master Explorer", 
    "Collector Supreme", "Untouchable", "Boss Slayer", 
    "Strategist", "Unstoppable", "Speed Runner", "Survivor", 
    "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set:
    # Elegimos cuántos cromos le van a tocar a este jugador (por ej. entre 5 y 10)
    num_achievements: int = random.randint(5, 10)
    
    # random.sample coge N elementos aleatorios de la lista sin repetir ninguno
    chosen: list = random.sample(MASTER_ACHIEVEMENTS, num_achievements)
    
    # Lo convertimos a un Set (el álbum oficial) y lo devolvemos
    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    
    # 1. Generamos los 4 jugadores que pide el PDF
    alice: set = gen_player_achievements()
    bob: set = gen_player_achievements()
    charlie: set = gen_player_achievements()
    dylan: set = gen_player_achievements()
    
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    
    # 2. Union: Todos los cromos distintos que han salido en la partida
    all_distinct: set = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")
    
    # 3. Intersection: Los cromos que tienen TODOS sin excepción
    common: set = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}\n")
    
    # 4. Difference entre jugadores: Lo que tiene uno y no tiene NADIE más
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print("")
    # 5. Difference con la lista maestra: Lo que le falta a cada uno para el 100%
    master_set: set = set(MASTER_ACHIEVEMENTS)
    print(f"Alice is missing: {master_set.difference(alice)}")
    print(f"Bob is missing: {master_set.difference(bob)}")
    print(f"Charlie is missing: {master_set.difference(charlie)}")
    print(f"Dylan is missing: {master_set.difference(dylan)}")


if __name__ == "__main__":
    main()
