import math

with open("_inputs/day2.txt", "r") as f:
    lines = [[int(i) for i in l.split(" ")] for l in f.read().splitlines()]


def safe(levels):
    diffs = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
    safe_count = all([1 <= abs(diff) <= 3 for diff in diffs])
    safe_sign = all(
        [math.copysign(1, diff) == math.copysign(1, diffs[0]) for diff in diffs]
    )
    return safe_count and safe_sign


part1 = 0
part2 = 0

for line in lines:
    if safe(line):
        part1 += 1
        part2 += 1
    else:
        for _, val in enumerate(line):
            level = line[:]
            level.remove(val)
            if safe(level):
                part2 += 1
                break

print("Part 1:", part1)
print("Part 2:", part2)
