with open("_inputs/day9.txt") as f:
    data = f.read().strip()

disk = []
n = 0
for i, c in enumerate(data):
    c = int(c)
    if i % 2 == 0:
        disk += [n] * c
        n += 1
    else:
        disk += [None] * c
    

# Part 1
i = 0
while i < len(disk):
    if disk[i] is None:
        last = disk.pop()
        if last is None:
            continue

        disk[i] = last
    i += 1

print(sum(i * v for i, v in enumerate(disk)))
