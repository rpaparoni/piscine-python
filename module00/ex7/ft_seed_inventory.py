def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    units = {
        "packets": "packets available",
        "grams": "grams total",
        "area": "square meters"
    }
    if unit in units:
        if unit == "area":
            print(f"{seed_type} seeds: covers {quantity} {units[unit]}")
        else:
            print(f"{seed_type} seeds: {quantity} {units[unit]}")
    else:
        print("Unknown unit type")


""" import sys
if __name__ == "__main__":
    # sys.argv[0] = nombre del script
    # sys.argv[1] = primer argumento, etc.
    seed_type = sys.argv[1]
    quantity = int(sys.argv[2])
    unit = sys.argv[3]

ft_seed_inventory(seed_type, quantity, unit) """
