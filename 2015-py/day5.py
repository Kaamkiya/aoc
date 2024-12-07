with open('day5.txt', 'r') as f:
    words = f.read().splitlines()

part1 = 0

def is_nice(word):
    vowel_count = 0
    for char in word.lower():
        if char in 'aeiou': vowel_count += 1

    if vowel_count < 3: return False

    if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word:
        return False

    for i in range (len(word)-1):
        if word[i] == word[i+1]:
            return True

    return False

for word in words:
    if is_nice(word):
        part1 += 1

print('Part 1:', part1)
