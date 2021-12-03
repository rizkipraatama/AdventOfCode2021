INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    depths = f.readlines()

oxygenGeneratorSetting = []
co2ScrubberSetting = []
for j in range(0, len(depths[0].strip())):
    total1 = 0
    total0 = 0
    for i in range(len(depths)):
        if (depths[i][j] == '1'):
            total1+=1
        else:
            total0+=1
    
    if (total1 >= total0):
        depths = [x for x in depths if x[j] == '1']
    else:
        depths = [x for x in depths if x[j] != '1']
	oxygenGeneratorSetting = depths[0]

with open(INPUT_FILE, "r") as f:
    depths = f.readlines()
for j in range(0, len(depths[0].strip())):
    total1 = 0
    total0 = 0
    for i in range(len(depths)):
        if (depths[i][j] == '1'):
            total1+=1
        else:
            total0+=1

    if (total1 >= total0):
        depths = [x for x in depths if x[j] != '1']
    else:
        depths = [x for x in depths if x[j] == '1']
    if depths:
            co2ScrubberSetting = depths[0]

print(int(oxygenGeneratorSetting, 2))
print(int(co2ScrubberSetting, 2))
print(int(co2ScrubberSetting, 2) * int(oxygenGeneratorSetting, 2))