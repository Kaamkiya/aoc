import re

with open("_inputs/day3.txt", "r") as f:
    data = f.read()

part1 = sum(
    int(match.group(1)) * int(match.group(2))
    for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", data)
)

part2 = 0
should_add = True
for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)", data):
    if match.group(0) == "do()":
        should_add = True
    elif match.group(0) == "don't()":
        should_add = False
    elif should_add:
        part2 += int(match.group(1)) * int(match.group(2))

print("Part 1:", part1)
print("Part 2:", part2)
