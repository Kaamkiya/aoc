with open("2022/_inputs/day4.txt", "r") as f:
    data = [line.split(",") for line in f.read().splitlines()]


def list_in_list(a, b):
    return (a[len(a) - 1] >= b[len(b) - 1] and a[0] <= b[0]) or (
        b[len(b) - 1] >= a[len(a) - 1] and b[0] <= a[0]
    )


def lists_overlap(a, b):
    for n in a:
        if n in b:
            return True
    return False


part1 = 0
part2 = 0

for left, right in data:
    l1, l2 = map(int, left.split("-"))
    r1, r2 = map(int, right.split("-"))

    leftlist = list(range(l1, l2 + 1))
    rightlist = list(range(r1, r2 + 1))

    if list_in_list(leftlist, rightlist):
        part1 += 1

    if lists_overlap(leftlist, rightlist):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
