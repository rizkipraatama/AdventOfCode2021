import numpy as np
from skimage.draw import line

INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    print([[x.strip().split(" -> ")] for x in f])
    coordinates = [[[int(k) for k in c.split(",")] for c in x.strip().split(" -> ")] for x in f]

overlappingLines = np.zeros((10,10), dtype=np.uint8)
rr, cc = line(1, 3, 1, 5)
overlappingLines[rr,cc] = 1
print (overlappingLines)