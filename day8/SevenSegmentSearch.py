input = [
    {
        'pattern': line.split('|')[0].strip().split(' '),
        'output': line.split('|')[1].strip().split(' ')
    }
    for line in open('input.txt').readlines()
]

totalDigitAppears = 0
for line in input:
    for digit in line['output']:
        if len(digit) in (2, 3, 4, 7):
            totalDigitAppears += 1

print(totalDigitAppears)