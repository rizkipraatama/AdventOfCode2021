INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    depths = [int(line) for line in f]

count = 0
for i in range(3, len(depths)):
    left = depths[i - 3] + depths[i - 2] + depths[i - 1]
    right = depths[i - 2] + depths[i - 1] + depths[i]
    if left < right:
        count += 1

print(count)