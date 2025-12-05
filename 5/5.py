db = []
ranges = []
ingredients = []
split = 0
fresh = 0

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
    ranges.append(start)
    ranges.append(end)

for ingredient in ingredients:
    for i in range(0, len(ranges), 2):
        if ranges[i] <= ingredient <= ranges[i + 1]:
            fresh += 1
            break

print(fresh)