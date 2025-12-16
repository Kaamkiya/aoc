with open("2025/_inputs/day2.txt") as f:
    data = [(int(pair.split("-")[0]), int(pair.split("-")[1])) for pair in f.read().split(",")]

part1 = 0
part2 = 0

for (lower, upper) in data:
    for n in range(lower, upper+1):
        string_n = str(n)
        half_a = string_n[:len(string_n)//2]
        half_b = string_n[len(string_n)//2:]

        if half_a == half_b:
            part1 += n

        for divisor in range(1, len(string_n)):
            if len(string_n) % divisor == 0:
                if (
                    string_n ==
                    (len(string_n)//divisor) * string_n[:divisor]
                ):
                    part2 += n
                    break

print("Part 1", part1)
print("Part 2", part2)
