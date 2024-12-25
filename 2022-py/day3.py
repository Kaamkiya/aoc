from string import ascii_letters

with open("day3.txt", "r") as f:
    rucksacks = f.read().splitlines()

part1 = 0
part2 = 0

for r in rucksacks:
    compartment1 = r[: len(r) // 2]
    compartment2 = r[len(r) // 2 :]
    for c in compartment1:
        if c in compartment2:
            part1 += ascii_letters.index(c) + 1
            break

for i in range(0, len(rucksacks), 3):
    elves = rucksacks[i : i + 3]
    print(elves)
    for c in elves[0]:
        if c in elves[1] and c in elves[2]:
            part2 += ascii_letters.index(c) + 1
            break

print("Part 1:", part1)
print("Part 2:", part2)
