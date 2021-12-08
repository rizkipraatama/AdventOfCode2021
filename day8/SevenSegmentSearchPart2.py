from itertools import permutations

with open("input.txt") as f:
    input = f.readlines()

mapNumber = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

sumAllOutput = 0
for line in input:
    pattern, output = line.split(" | ")
    pattern = pattern.split()
    output = output.split()
   
    for permutation in permutations("abcdefg"):
        allPossibleWords = str.maketrans("abcdefg", "".join(permutation))
        pattern_ = ["".join(sorted(code.translate(allPossibleWords))) for code in pattern]
        output_ = ["".join(sorted(code.translate(allPossibleWords))) for code in output]
        if all(code in mapNumber for code in pattern_):
            sumAllOutput += int("".join(str(mapNumber[code]) for code in output_))
            break

print(sumAllOutput)