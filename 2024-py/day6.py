with open('day6.txt', 'r') as f:
    grid = [list(line) for line in f.read().splitlines()]

directions = ((0, -1), # left
            (1, 0), # up
            (0, 1), # right
            (-1, 0)) # down
guard_x = 0
guard_y = 0
guard_dir_idx = 1
guard_dir = directions[guard_dir_idx]
positions_visited = set()

part1 = 0

for i, line in enumerate(grid):
    guard_y = i
    if '^' in line:
        guard_x = line.index('^')
        break

while True:
    dy = guard_dir[0]
    dx = guard_dir[1]
    ny = guard_y - dy
    nx = guard_x + dx

    if (not (0 <= guard_x < len(grid[0]))) or (not (0 <= guard_y < len(grid))):
        break

    if grid[ny][nx] == '#':
        guard_dir_idx += 1
        if guard_dir_idx > 3: guard_dir_idx = 0
        guard_dir = directions[guard_dir_idx]
    else:
        guard_x = nx
        guard_y = ny
    
    positions_visited.add((guard_x, guard_y))

print(len(positions_visited))
