
INPUT_FILE = "input.txt"
with open(INPUT_FILE) as f:
    heightmap = []
    for line in f.read().splitlines():
        heightmap.append([int(i) for i in line])

height = len(heightmap)
width = len(heightmap[0])

def neighbors(j, i):
    return set([(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(height-1)), i), (j, i+1 - 2*(i==(width-1)))])

riskLevel = 0
for j in range(height):
    for i in range(width):
        if all([heightmap[j][i] < heightmap[y][x] for y, x in neighbors(j, i)]):
            riskLevel += 1 + heightmap[j][i]

print(riskLevel)