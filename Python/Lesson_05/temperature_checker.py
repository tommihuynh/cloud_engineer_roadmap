temperature = float(input("Temperature (C): "))

if temperature <0:
    print("Freezing")
elif temperature <15:
    print("cold")
elif temperature <25:
    print("Warm")
else:
    print("hot")
