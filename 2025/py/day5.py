with open("2025/_inputs/day5.txt") as f:
    (ranges, ids) = f.read().split("\n\n")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges.splitlines()]
    ids = [int(id) for id in ids.splitlines()]

fresh_count = 0

for id in ids:
    for (lower, upper) in ranges:
        if lower <= id <= upper:
            fresh_count += 1
            break # exit inner loop

print(fresh_count)
