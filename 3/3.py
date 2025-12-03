banks = []
with open('inputs.txt') as f:
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
    if not bank:
        continue

    max_value = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            value = bank[i] * 10 + bank[j]
            max_value = max(max_value, value)
    
    
    joltage += max_value

print(joltage)
