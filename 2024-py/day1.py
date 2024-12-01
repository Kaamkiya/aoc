with open('day1.txt', 'r') as f:
    contents = f.read().splitlines()

lines = [x.split('   ') for x in contents]
left = [int(a) for (a, _) in lines]
right = [int(b) for (_, b) in lines]

left.sort()
right.sort()

total = 0
similarity = 0

for i, a in enumerate(left):
    b = right[i]

    diff = abs(a-b)
    total += diff

    similarity += a * right.count(a)

print('Part 1: Total diff:', total)
print('Part 2: similarity:', similarity)
