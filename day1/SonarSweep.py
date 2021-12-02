INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    depths = f.readlines()

count = 0
for i in range(1, len(depths)):
    if int(depths[i - 1]) < int(depths[i]):
        count += 1

print(count)