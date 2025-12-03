banks = []
with open('test.txt') as f:
    lines = f.readlines()

n = 0
for line in lines:
    line = line.strip()
    banks.append([])
    for char in line:
        banks[n].append(int(char))
    n += 1


joltage = 0

for bank in banks:
    max_value = 0

    for i in range(len(bank)-3):
        for j in range(i+1, len(bank)-2):
            for k in range(j+1, len(bank)-1):
                result = []
                for pos in range(len(bank)):
                    if pos != i and pos != j and pos != k:
                        result.append(bank[pos])
                
                value = int(''.join(map(str, result)))
                if value > max_value:
                    max_value = value
    
    joltage += max_value

print(joltage)
