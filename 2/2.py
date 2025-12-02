def invalid_check(s):
    n = str(s)
    length = len(n)
    
    if length < 2:
        return False
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = n[:pattern_len]
            is_valid_pattern = True
            
            for position in range(0, length, pattern_len):
                chunk = n[position:position+pattern_len]
                            
                if chunk != pattern:
                    is_valid_pattern = False
                    break
    
            if is_valid_pattern and (length // pattern_len >= 2):
                return True
    return False

def count_invalid(start, end):
    total = 0
    invalid_ids = []
    for num in range(start, end + 1):
        if invalid_check(num):
            total += num
            invalid_ids.append(num)
    print(f"Range {start}-{end}: Found {invalid_ids}, Sum: {total}")
    return total

with open('inputs.txt') as f:
    content = f.read()


lines = content.split(',')

count = 0

for line in lines:
     line = line.strip()
     if not line:
          continue
     
     parts = line.split('-')
     start = int(parts[0])
     end = int(parts[1])

     count += count_invalid(start, end)

print(count)
