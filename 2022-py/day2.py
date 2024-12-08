with open('day2.txt', 'r') as f:
    data = [line.split() for line in f.read().splitlines()]

other_move = [a for (a, _) in data]
my_move = [b for (_, b) in data]

part1 = 0

for i, move in enumerate(my_move):
    match move:
        case 'X':
            part1 += 1
            match other_move[i]:
                case 'A': part1 += 3
                case 'C': part1 += 6
        case 'Y':
            part1 += 2
            match other_move[i]:
                case 'A': part1 += 6
                case 'B': part1 += 3
        case 'Z':
            part1 += 3
            match other_move[i]:
                case 'B': part1 += 6
                case 'C': part1 += 3

part2 = 0

for i, move in enumerate(my_move):
    match move:
        case 'X':
            match other_move[i]:
                case 'A': part2 += 3
                case 'B': part2 += 1
                case 'C': part2 += 2
        case 'Y':
            part2 += 3
            match other_move[i]:
                case 'A': part2 += 1
                case 'B': part2 += 2
                case 'C': part2 += 3
        case 'Z':
            part2 += 6
            match other_move[i]:
                case 'A': part2 += 2
                case 'B': part2 += 3
                case 'C': part2 += 1


print('Part 1:', part1)
print('Part 2:', part2)
