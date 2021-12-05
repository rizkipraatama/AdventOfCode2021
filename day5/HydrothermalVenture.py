import numpy as np
from skimage.draw import line

INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    coordinates = [[[int(k) for k in c.split(",")] for c in x.strip().split(" -> ")] for x in f]

overlappingLines = np.zeros((1000,1000), dtype=np.uint8)

for ((x1, y1), (x2, y2)) in coordinates:
    if x1 == x2 or y1 == y2:
        rr, cc = line(x1, y1, x2, y2)
        overlappingLines[rr, cc] += 1
print(len(overlappingLines[overlappingLines > 1]))