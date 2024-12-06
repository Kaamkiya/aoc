from functools import cmp_to_key

with open('day5.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

rule_lines = []
update_lines = []
for line in data:
    if '|' in line:
        rule_lines.append(line)
    elif ',' in line:
        update_lines.append(line)

rules = {}
part1 = 0

last_line = 0

for line in rule_lines:
    (a, b) = [int(i) for i in line.strip().split('|')]

    if not rules.get(a)
    rules.append([a, int(rule[1])])

def correct_order(pages):
    for [before, after] in rules:
        if before not in pages or after not in pages:
            continue
        a = pages.index(before)
        b = pages.index(after)

        if a > b:
            return False
    return True

# Part 1

for line in update_lines:
    pages = [int(i) for i in line.split(',')]
    if correct_order(pages):
        part1 += pages[len(pages)//2]

print('Part 1:', part1)
