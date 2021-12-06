INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    input = [x.split(",") for x in f]
    initialFish = [int(x) for x in input[0]]

for i in range(256):
    for j in range(len(initialFish)):
        if initialFish[j] == 0:
            initialFish[j] = 6
            initialFish.append(8)
        else:
            initialFish[j] -= 1
print(len(initialFish))
