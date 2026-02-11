class Plants:
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age


plant_1 = Plants('Rose', 25, 30)
plant_2 = Plants('Sunflower', 80, 45)
plant_3 = Plants('Cactus', 15, 120)

print("=== Garden Plant Registry ===")
print(f"{plant_1.name}: {plant_1.size}cm, {plant_1.age} days old")
print(f"{plant_2.name}: {plant_2.size}cm, {plant_2.age} days old")
print(f"{plant_3.name}: {plant_3.size}cm, {plant_3.age} days old")
