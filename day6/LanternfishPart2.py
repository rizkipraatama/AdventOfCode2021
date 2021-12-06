from collections import defaultdict
INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    input = [x.split(",") for x in f]
    initialFishList = [int(x) for x in input[0]]
initialFish = {i:initialFishList.count(i) for i in initialFishList}

for i in range(256):
    temp = defaultdict(int)
    for key, value in sorted(initialFish.items()):
        if key == 0:
            temp[6] += value
            temp[8] = value
        else:
            temp[key-1] += value
    initialFish = temp

print(sum(initialFish.values()))
