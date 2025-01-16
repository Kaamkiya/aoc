from collections import defaultdict

with open("2024-inputs/day1.txt", "r") as f:
    contents = f.read().splitlines()

lines = [x.split("   ") for x in contents]
left = [int(a) for (a, _) in lines]
right = [int(b) for (_, b) in lines]

left.sort()
right.sort()

total = 0
similarity = 0

counts = defaultdict(int)

for a in right:
    counts[a] += 1

for i, a in enumerate(left):
    b = right[i]

    diff = abs(a - b)
    total += diff

    similarity += a * counts[a]

print("Part 1: Total diff:", total)
print("Part 2: similarity:", similarity)
