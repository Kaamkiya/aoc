with open("_inputs/day4.txt", "r") as f:
    data = f.read().splitlines()

directions = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]

part1 = 0

for y, row in enumerate(data):
    for x, _ in enumerate(row):
        for _, (dy, dx) in enumerate(directions):
            if not (0 <= y + 3 * dy < len(data) and 0 <= x + 3 * dx < len(data[0])):
                continue

            if (
                data[y][x] == "X"
                and data[y + dy][x + dx] == "M"
                and data[y + dy * 2][x + dx * 2] == "A"
                and data[y + dy * 3][x + dx * 3] == "S"
            ):
                part1 += 1

part2 = 0

for y, row in enumerate(data):
    for x, cell in enumerate(row):
        find = ["S", "M"]
        if cell in find:
            # Not a very elegant solution but it works.
            find.remove(cell)
            other = find[0]

            find = ["S", "M"]

            if (x + 2 < len(row)) and (y + 2 < len(data)):
                cell1 = cell
                cell2 = row[x + 2]
                cell3 = data[y + 2][x]
                cell4 = data[y + 2][x + 2]
                if cell1 in find and cell2 in find:
                    if cell3 in find and cell3 != cell2:
                        if cell4 in find and cell4 != cell1:
                            if data[y + 1][x + 1] == "A":
                                part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
