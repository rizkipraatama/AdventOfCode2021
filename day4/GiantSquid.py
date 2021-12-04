INPUT_FILE = "input.txt"
from more_itertools import chunked
import numpy as np

with open(INPUT_FILE, "r") as f:
    lines = [x.strip() for x in f]

bingoRandomNumber = [int(x) for x in lines[0].split(",")]
boards = [np.array([[int(x) for x in c.split()] for c in b[1:]]) for b in chunked(lines[1:], 6)]

def CheckWinning(board, numbers):
    for row in board:
        if all(n in numbers for n in row):
            return True
    for col in board.T:
        if all(n in numbers for n in col):
            return True
    return False

winnerIndexes = []
numberFoundIndexes = []

for idx in range(5, len(bingoRandomNumber)+1):
    for boardIndex, board in enumerate(boards):
        if boardIndex not in winnerIndexes and CheckWinning(board, set(bingoRandomNumber[:idx])):
            winnerIndexes.append(boardIndex)
            numberFoundIndexes.append(idx)
    if len(winnerIndexes) == len(boards):
        break

print(sum([n for n in boards[winnerIndexes[0]].flatten() if n not in bingoRandomNumber[:numberFoundIndexes[0]]]) * bingoRandomNumber[numberFoundIndexes[0]-1])