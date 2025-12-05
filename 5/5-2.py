db = []
ranges = []
ingredients = []
split = 0
total = 0

with open('inputs.txt') as f:
    db = f.readlines()

for i, line in enumerate(db):
    line = line.strip()
    if line == '':
        split = i
        break

for i in range(split + 1, len(db)):
    ingredients.append(int(db[i].strip()))

db = [line.strip() for line in db[:split]]

for r in db:
    parts = r.split('-')
    start = int(parts[0])
    end = int(parts[1])
    ranges.append((start, end))

ranges.sort()
sorted = [ranges[0]]
for i in range(1, len(ranges)):
    if ranges[i][0] <= sorted[-1][1]:
        sorted[-1] = (sorted[-1][0], max(sorted[-1][1], ranges[i][1]))
    else:
        sorted.append(ranges[i])

for start, end in sorted:
    total += (end - start + 1)

print(total)