count = 50
codes = []
zero = 0

with open('input.txt') as f:
    codes = f.readlines()

for code in codes:
    code = code.strip()
    
    if not code:
        continue

    amount = int(code[1:])
    start = count
    
    if code[0] == 'R':
        count = (count + amount) % 100
        zero += (start + (amount % 100)) // 100 + amount // 100
    elif code[0] == 'L':
        start = (100 - start) % 100
        count = (count - amount) % 100
        zero += (start + (amount % 100)) // 100 + amount // 100


print(zero)
