with open("2015-inputs/day2.txt", "r") as f:
    data = [[int(i) for i in line.split("x")] for line in f.read().splitlines()]

total_wrap = 0  # Part 1
total_ribbon = 0  # Part 2


def smallest_area(a1, a2, a3):
    if a3 > a1 < a2:
        return a1
    if a2 < a3:
        return a2
    return a3


def smallest_perimeter(l, w, h):
    return min([2 * (l + w), 2 * (w + h), 2 * (l + h)])


for l, w, h in data:
    total_wrap += 2 * w * l + 2 * w * h + 2 * h * l + smallest_area(l * w, w * h, h * l)
    total_ribbon += smallest_perimeter(l, w, h) + w * l * h

print("Total wrapping paper:", total_wrap)
print("Total ribbon:", total_ribbon)
