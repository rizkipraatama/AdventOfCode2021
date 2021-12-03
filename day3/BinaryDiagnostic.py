INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    depths = f.readlines()

gammaRate = ''
epsilonRate = ''
for j in range(0, len(depths[0].strip())):
    total1 = 0
    total0 = 0
    for i in range(0, len(depths)):
        if (depths[i][j] == '1'):
            total1+=1
        else:
            total0+=1
    if (total1 > total0):
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'

print(int(gammaRate, 2) * int(epsilonRate, 2))
