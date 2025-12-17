with open("2025/_inputs/day1.txt") as f:
    instructions = [(row[0], int(row[1:])) for row in f.read().splitlines()]

dial = 50
part1 = 0

for (direction, amount) in instructions:
    if dial == 0: part1 += 1

    if direction == "L":
        dial = (dial - amount) % 100
    else:
        dial = (dial + amount) % 100

print(part1)
