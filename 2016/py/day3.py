with open("2016/_inputs/day3.txt") as f:
    triangles = [[int(i) for i in r.split()] for r in f.read().splitlines()]

count = 0

for t in triangles:
    if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
        count += 1

print(count)
