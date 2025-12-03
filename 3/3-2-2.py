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
    digits_to_keep = 12
    digits_to_remove = len(bank) - digits_to_keep

    result = []
    removed = 0

    for i in range(len(bank)):
        while removed < digits_to_remove and len(result) > 0 and i < len(bank) and result[-1] < bank[i]:
            result.pop()
            removed += 1
        result.append(bank[i])
    result = result[:12]
    value = int(''.join(map(str, result)))
    joltage += value

print(joltage)
