from collections import defaultdict

with open("2021/_inputs/day2.txt", "r") as f:
    inp = f.read().splitlines()
    commands = defaultdict(list)
    raw_commands = []
    for line in inp:
        cmd, amount = line.split()
        raw_commands.append((cmd, int(amount)))
        commands[cmd].append(int(amount))

depth = sum(commands["down"]) - sum(commands["up"])
forward = sum(commands["forward"])

print("Part 1:", depth * forward)

depth = 0
forward = 0
aim = 0

for cmd, amount in raw_commands:
    match cmd:
        case "down":
            aim += amount
        case "up":
            aim -= amount
        case "forward":
            forward += amount
            depth += aim * amount

print("Part 2:", depth * forward)
