def ft_water_reminder():
    days = input("Days since last watering: ")
    days = int(days)
    if (days > 2):
        print("Plants are fine")
    else:
        print("Plant is ready to harvest!")
