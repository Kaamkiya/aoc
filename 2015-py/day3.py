with open("day3.txt", "r") as f:
    data = f.read()

santa_x = 0
santa_y = 0
part1 = set((0, 0))

for move in data:
    match move:
        case "^":
            santa_y += 1
        case "v":
            santa_y -= 1
        case "<":
            santa_x -= 1
        case ">":
            santa_x += 1

    part1.add((santa_x, santa_y))

robo_x = 0
robo_y = 0
santa_x = 0
santa_y = 0
is_santa = True
part2 = set()

for move in data:
    match move:
        case "^":
            if is_santa:
                santa_y += 1
            else:
                robo_y += 1
        case "v":
            if is_santa:
                santa_y -= 1
            else:
                robo_y -= 1
        case "<":
            if is_santa:
                santa_x -= 1
            else:
                robo_x -= 1
        case ">":
            if is_santa:
                santa_x += 1
            else:
                robo_x += 1

    is_santa = not is_santa

    part2.add((santa_x, santa_y))
    part2.add((robo_x, robo_y))

print("Part 1:", len(part1))
print("Part 2:", len(part2))
