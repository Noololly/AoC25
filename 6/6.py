from math import prod

sums = []
calc = []
total = 0

with open('inputs.txt') as f:
    lines = [line.strip() for line in f]

for line in lines:
    sums.append([])
    s = ""
    for char in line:
        if char.isdigit() or char in ['+', '*']:
            s += char
        elif s:
            sums[-1].append(s)
            s = ""
    if s:
        sums[-1].append(s)

for i in range(len(sums[0])): # i is calculation number
    calc.append([])
    for j in range(len(sums)): # j is the layer
        calc[i].append(sums[j][i])

for c in calc:
    a = []
    for n in range(len(c) - 1):
        a.append(int(c[n])) # make a list of ints to process
    if c[-1] == '+':
        total += sum(a)
    else:
        total += prod(a)

print(total)