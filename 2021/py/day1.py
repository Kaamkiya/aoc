with open("2021/_inputs/day1.txt", "r") as f:
    depths = [int(i) for i in f.read().splitlines()]

part1 = 0

for i, d in enumerate(depths):
    if i == 0:
        continue

    if d > depths[i - 1]:
        part1 += 1

sums = []
part2 = 0

for i in range(len(depths)):
    if i + 3 > len(depths):
        break
    sums.append(sum(depths[i : i + 3]))

for i, s in enumerate(sums):
    if i == 0:
        continue
    if s > sums[i - 1]:
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
