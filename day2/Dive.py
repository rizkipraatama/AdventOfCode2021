INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    depths = f.readlines()

currentHorizontal = 0
currentDepth = 0
for i in range(0, len(depths)):
    splittedInput = depths[i].split(" ")
    if (splittedInput[0] == "forward"):
        currentHorizontal += int(splittedInput[1])
    elif(splittedInput[0] == "down"):
        currentDepth += int(splittedInput[1])
    elif(splittedInput[0] == "up"):
        currentDepth -= int(splittedInput[1])
print(currentHorizontal * currentDepth)