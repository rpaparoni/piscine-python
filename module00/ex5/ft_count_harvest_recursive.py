def ft_count_harvest_recursive(day=1, total_days=None):
    if total_days is None:
        total_days = int(input("Days until harvest: "))
    if day <= total_days:
        print(f"Day {day}" if day < total_days
              else f"Day {day}\nHarvest time!")
        ft_count_harvest_recursive(day + 1, total_days)
