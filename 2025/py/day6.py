import math

with open("2025/_inputs/day6.txt") as f:
    data = [row.split() for row in f.read().splitlines()]

# data is now a table, eg:
# [[23, 328, 51,  64],
#  [45, 64,  387, 23],
#  [6,  98,  215, 314],
#  [*,  +,   *,   +]]
# I need to read it the other way, though.
# If I have the rows, how do I read the columns?
# I suppose there's only four rows. That means I can do data[0][i] * data[1][i] * data[2][i]

part1 = 0

for i, operand in enumerate(data[4]):
    terms = [int(data[0][i]), int(data[1][i]), int(data[2][i]), int(data[3][i])]

    if operand == "+":
        part1 += sum(terms)
    elif operand == "*":
        part1 += math.prod(terms)

print(part1)
