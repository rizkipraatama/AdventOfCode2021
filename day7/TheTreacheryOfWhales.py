INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    input = [x.split(",") for x in f]
    horizontalPosition = [int(x) for x in input[0]]

minimumPosition = min(horizontalPosition)
maximumPosition = max(horizontalPosition)

minimumFuel = float("inf")

for i in range(minimumPosition, maximumPosition):
    fuel = 0
    for j in horizontalPosition:
        usedFuel = abs(j - i)
        fuel += usedFuel
    if fuel < minimumFuel:
        minimumFuel = fuel


print(minimumFuel)