
INPUT_FILE = "input.txt"
with open(INPUT_FILE) as f:
    heightmap = []
    for line in f.read().splitlines():
        heightmap.append([int(i) for i in line])

height = len(heightmap)
width = len(heightmap[0])

def neighbors(j, i):
    return set([(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(height-1)), i), (j, i+1 - 2*(i==(width-1)))])

lowPoints = []
for j in range(height):
    for i in range(width):
        if all([heightmap[j][i] < heightmap[y][x] for y, x in neighbors(j, i)]):
            lowPoints.append((j, i))

def size(j, i, visited):
    if (j, i) not in visited:
        visited.append((j, i))
        return 1 + sum([size(y, x, visited) if 9 > heightmap[y][x] > heightmap[j][i] else 0 for y, x in neighbors(j, i)])
    else:
        return 0

sizes = []
for p in lowPoints:
    sizes.append(size(p[0], p[1], []))

sizes = sorted(sizes)[-3:]
print(sizes[0] * sizes[1] * sizes[2])