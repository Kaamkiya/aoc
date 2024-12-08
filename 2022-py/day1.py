with open('day1.txt', 'r') as f:
    calories = f.read().split('\n\n')

elf_calories = []

for c in calories:
    elf_calories.append(sum([int(i) for i in c.strip().split('\n')]))

print('Part 1:', max(elf_calories))

print('Part 2:', sum(sorted(elf_calories)[::-1][:3]))
