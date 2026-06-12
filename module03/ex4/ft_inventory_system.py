import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    # 1. Parsing de los argumentos de la terminal
    args: list = sys.argv[1:]
    inventory: dict = {}

    i: int = 0
    while i < len(args):
        arg: str = args[i]
        parts: list = arg.split(':')

        # Si no hay exactamente dos partes (nombre y cantidad), sintaxis inválida
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        else:
            item_name: str = parts[0]
            val_str: str = parts[1]

            # Comprobamos si el objeto ya está en nuestra "taquilla"
            if item_name in inventory:
                print(f"Redundant item '{item_name}' - discarding")
            else:
                try:
                    qty: int = int(val_str)
                    inventory[item_name] = qty
                except ValueError as error:
                    # Atrapamos la queja automática de int()
                    print(f"Quantity error for '{item_name}': {error}")
        i += 1

    # 2. Mostramos el inventario final válido
    print(f"Got inventory: {inventory}")

    # 3. Lista de los nombres de los objetos (las "llaves" de la taquilla)
    item_names: list = list(inventory.keys())
    print(f"Item list: {item_names}")

    # 4. Cálculos totales usando sum() y dict.values()
    total_items: int = len(item_names)

    # Si por algún casual no entrara ningún objeto válido, evitamos que el programa explote
    if total_items > 0:
        total_qty: int = sum(inventory.values())
        print(f"Total quantity of the {total_items} items: {total_qty}")

        # 5. Porcentajes de cada objeto
        j: int = 0
        while j < total_items:
            current_item: str = item_names[j]
            qty_val: int = inventory[current_item]

            # (cantidad / total) * 100 y redondeado a 1 decimal
            pct: float = round((qty_val / total_qty) * 100, 1)
            print(f"Item {current_item} represents {pct}%")
            j += 1

        # 6. Calcular el más abundante y el menos abundante
        # Asumimos al principio que el primero es el mayor y el menor a la vez
        most_abundant: str = item_names[0]
        least_abundant: str = item_names[0]
        max_qty: int = inventory[most_abundant]
        min_qty: int = inventory[least_abundant]

        k: int = 1
        while k < total_items:
            current_item = item_names[k]
            current_qty: int = inventory[current_item]

            # Usamos '>' y '<' estrictos. Así, si hay un empate, 
            # se quedará con el primero que encontró, clavando lo que pide el subject.
            if current_qty > max_qty:
                max_qty = current_qty
                most_abundant = current_item

            if current_qty < min_qty:
                min_qty = current_qty
                least_abundant = current_item

            k += 1

        print(f"Item most abundant: {most_abundant} with quantity {max_qty}")
        print(f"Item least abundant: {least_abundant} with quantity {min_qty}")

        # 7. Añadimos el nuevo objeto mágico usando update()
        inventory.update({'magic_item': 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
