# 1. EL ABUELO
class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self, amount: int) -> None:
        self.height += amount


# 2. EL PADRE
class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = True


# 3. EL HIJO (El más especializado)
class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, color: str, points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points: int = points


# 4. EL MANAGER Y SUS HERRAMIENTAS
class GardenManager:
    # La clase anidada (nuestra calculadora de bolsillo)
    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            if height >= 0:
                return True
            return False

    def __init__(self, owner_name: str) -> None:
        self.owner: str = owner_name
        self.plants: list = []  # Lista vacía para guardar las plantas

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    @classmethod
    def create_garden_network(cls) -> int:
        return 2

    def generate_report(self) -> None:
        print(f"--- {self.owner}'s Garden Report ---")
        i: int = 0
        while i < len(self.plants):
            planta_actual = self.plants[i]
            # Rompemos el string para no pasar de 79 caracteres
            print(
                f"Plant: {planta_actual.name}, "
                f"Height: {planta_actual.height}cm"
            )
            i += 1
        print("---------------------------")


# 5. EL BLOQUE DE PRUEBAS (La zona de acción)
if __name__ == "__main__":
    print("=== Garden Analytics Platform ===\n")

    # Probamos el @classmethod (se llama usando el nombre de la clase)
    network_size: int = GardenManager.create_garden_network()
    print(f"Network created with {network_size} gardens")

    # Probamos el @staticmethod (validamos una altura de 150)
    is_valid: bool = GardenManager.GardenStats.validate_height(150)
    print(f"Height validation test: {is_valid}\n")

    # Creamos el jardín y un par de plantas diferentes
    manager: GardenManager = GardenManager("Alice")
    rosa_campeona: PrizeFlower = PrizeFlower("Champion Rose", 40, "Red", 95)
    arbolito: Plant = Plant("Oak Sapling", 20)

    # Las plantamos
    manager.add_plant(rosa_campeona)
    manager.add_plant(arbolito)

    # Las hacemos crecer un poco
    print("\nGrowing plants...")
    rosa_campeona.grow(5)
    arbolito.grow(10)

    # Sacamos el reporte final con nuestro bucle while
    print()
    manager.generate_report()
