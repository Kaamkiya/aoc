with open('day4.txt', 'r') as f:
    data = f.read().splitlines()

directions = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]

part1 = 0
find = "XMAS"

for y, row in enumerate(data):
    for x, _ in enumerate(row):
        for _, (dy, dx) in enumerate(directions):
            if not (0 <= y + 3 * dy < len(data) and 0 <= x + 3 * dx < len(data[0])):
                continue

            if (data[y][x] == 'X' and
                data[y+dy][x+dx] == 'M' and
                data[y+dy*2][x+dx*2] == 'A' and
                data[y+dy*3][x+dx*3] == 'S'):
                part1 += 1

print('Part 1:', part1)
