with open("2025/_inputs/day1.txt") as f:
    instructions = [(row[0], int(row[1:])) for row in f.read().splitlines()]

dial = 50
zero_count = 0

for (direction, amount) in instructions:
    if dial == 0: zero_count += 1

    print(dial)

    if direction == "L":
        dial = (dial - amount) % 100
    else:
        dial = (dial + amount) % 100

print(zero_count)
